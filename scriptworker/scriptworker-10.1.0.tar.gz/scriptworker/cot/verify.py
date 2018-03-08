"""Chain of Trust artifact verification.

Attributes:
    ACTION_MACH_COMMANDS (tuple): the allowlisted mach commands for an action task,
        ignoring options.
    DECISION_MACH_COMMANDS (tuple): the allowlisted mach commands for a decision task,
        ignoring options.
    DECISION_TASK_TYPES (tuple): the decision task types.
    PARENT_TASK_TYPES (tuple): the parent task types.
    log (logging.Logger): the log object for this module.

"""
import aiohttp
import argparse
import asyncio
from copy import deepcopy
import dictdiffer
from frozendict import frozendict
import jsone
import logging
import os
import pprint
import shlex
import sys
import tempfile
from scriptworker.artifacts import (
    download_artifacts,
    get_artifact_url,
    get_optional_artifacts_per_task_id,
    get_single_upstream_artifact_full_path,
)
from scriptworker.config import read_worker_creds, apply_product_config
from scriptworker.constants import DEFAULT_CONFIG
from scriptworker.context import Context
from scriptworker.exceptions import CoTError, DownloadError, ScriptWorkerGPGException
from scriptworker.gpg import get_body, GPG
from scriptworker.log import contextual_log_handler
from scriptworker.task import (
    get_action_name,
    get_and_check_project,
    get_and_check_tasks_for,
    get_commit_message,
    get_decision_task_id,
    get_parent_task_id,
    get_repo,
    get_revision,
    get_task_id,
    get_worker_type,
    is_try,
    is_action,
)
from scriptworker.utils import (
    add_enumerable_item_to_dict,
    get_hash,
    get_loggable_url,
    get_results_and_future_exceptions,
    format_json,
    load_json_or_yaml,
    load_json_or_yaml_from_url,
    makedirs,
    match_url_path_callback,
    match_url_regex,
    raise_future_exceptions,
    remove_empty_keys,
    rm,
)
from taskcluster.exceptions import TaskclusterFailure

log = logging.getLogger(__name__)


# XXX Remove all mach command hardcodes when all trees are 59+
DECISION_MACH_COMMANDS = ((
    './mach', 'taskgraph', 'decision'
), )
ACTION_MACH_COMMANDS = ((
    './mach', 'taskgraph', 'add-tasks'
), (
    './mach', 'taskgraph', 'backfill'
), (
    './mach', 'taskgraph', 'action-callback'
))
DECISION_TASK_TYPES = ('decision', )
PARENT_TASK_TYPES = ('decision', 'action')


# ChainOfTrust {{{1
class ChainOfTrust(object):
    """The master Chain of Trust, tracking all the various ``LinkOfTrust``s.

    Attributes:
        context (scriptworker.context.Context): the scriptworker context
        decision_task_id (str): the task_id of self.task's decision task
        parent_task_id (str): the task_id of self.task's parent task
        links (list): the list of ``LinkOfTrust``s
        name (str): the name of the task (e.g., signing)
        task_id (str): the taskId of the task
        task_type (str): the task type of the task (e.g., decision, build)
        worker_impl (str): the taskcluster worker class (e.g., docker-worker) of the task

    """

    def __init__(self, context, name, task_id=None):
        """Initialize ChainOfTrust.

        Args:
            context (scriptworker.context.Context): the scriptworker context
            name (str): the name of the task (e.g., signing)
            task_id (str, optional): the task_id of the task.  If None, use
                ``get_task_id(context.claim_task)``.  Defaults to None.

        """
        self.name = name
        self.context = context
        self.task_id = task_id or get_task_id(context.claim_task)
        self.task = context.task
        self.task_type = guess_task_type(name, self.task)
        self.worker_impl = guess_worker_impl(self)  # this should be scriptworker
        self.decision_task_id = get_decision_task_id(self.task)
        self.parent_task_id = get_parent_task_id(self.task)
        self.links = []

    def dependent_task_ids(self):
        """Get all ``task_id``s for all ``LinkOfTrust`` tasks.

        Returns:
            list: the list of ``task_id``s

        """
        return [x.task_id for x in self.links]

    def is_try(self):
        """Determine if any task in the chain is a try task.

        Returns:
            bool: True if a task is a try task.

        """
        result = is_try(self.task, source_env_prefix=self.context.config['source_env_prefix'])
        for link in self.links:
            if link.is_try:
                result = True
                break
        return result

    def get_link(self, task_id):
        """Get a ``LinkOfTrust`` by task id.

        Args:
            task_id (str): the task id to find.

        Returns:
            LinkOfTrust: the link matching the task id.

        Raises:
            CoTError: if no ``LinkOfTrust`` matches.

        """
        links = [x for x in self.links if x.task_id == task_id]
        if len(links) != 1:
            raise CoTError("No single Link matches task_id {}!\n{}".format(task_id, self.dependent_task_ids()))
        return links[0]

    def is_decision(self):
        """Determine if the chain is a decision task.

        Returns:
            bool: whether it is a decision task.

        """
        return self.task_type in DECISION_TASK_TYPES

    def get_all_links_in_chain(self):
        """Return all links in the chain of trust, including the target task.

        By default, we're checking a task and all its dependencies back to the
        tree, so the full chain is ``self.links`` + ``self``. However, we also
        support checking the decision task itself. In that case, we populate
        the decision task as a link in ``self.links``, and we don't need to add
        another check for ``self``.

        Returns:
            list: of all ``LinkOfTrust``s to verify.

        """
        if self.is_decision() and self.get_link(self.task_id):
            return self.links
        return [self] + self.links


# LinkOfTrust {{{1
class LinkOfTrust(object):
    """Each LinkOfTrust represents a task in the Chain of Trust and its status.

    Attributes:
        context (scriptworker.context.Context): the scriptworker context
        decision_task_id (str): the task_id of self.task's decision task
        parent_task_id (str): the task_id of self.task's parent task
        is_try (bool): whether the task is a try task
        name (str): the name of the task (e.g., signing.decision)
        task_id (str): the taskId of the task
        task_graph (dict): the task graph of the task, if this is a decision task
        task_type (str): the task type of the task (e.g., decision, build)
        worker_impl (str): the taskcluster worker class (e.g., docker-worker) of the task

    """

    _task = None
    _cot = None
    _task_graph = None
    status = None

    def __init__(self, context, name, task_id):
        """Initialize ChainOfTrust.

        Args:
            context (scriptworker.context.Context): the scriptworker context
            name (str): the name of the task (e.g., signing)
            task_id (str): the task_id of the task

        """
        self.name = name
        self.context = context
        self.task_id = task_id

    def _set(self, prop_name, value):
        prev = getattr(self, prop_name)
        if prev is not None:
            raise CoTError(
                "LinkOfTrust {}: re-setting {} to {} when it is already set to {}!".format(
                    str(self.name), prop_name, value, prev
                )
            )
        return setattr(self, prop_name, value)

    @property
    def task(self):
        """dict: the task definition.

        When set, we also set ``self.decision_task_id``, ``self.parent_task_id``,
        ``self.worker_impl``, and ``self.is_try`` based on the task definition.

        """
        return self._task

    @task.setter
    def task(self, task):
        self._set('_task', task)
        self.task_type = guess_task_type(self.name, self.task)
        self.decision_task_id = get_decision_task_id(self.task)
        self.parent_task_id = get_parent_task_id(self.task)
        self.worker_impl = guess_worker_impl(self)
        self.is_try = is_try(self.task, source_env_prefix=self.context.config['source_env_prefix'])

    @property
    def cot(self):
        """dict: the chain of trust json body."""
        return self._cot

    @cot.setter
    def cot(self, cot):
        cot_task_id = cot.get('taskId')
        if cot_task_id != self.task_id:
            raise CoTError("Chain of Trust artifact taskId {} doesn't match task taskId {}!".format(cot_task_id, self.task_id))
        self._set('_cot', cot)

    @property
    def task_graph(self):
        """dict: the decision task graph, if this is a decision task."""
        return self._task_graph

    @task_graph.setter
    def task_graph(self, task_graph):
        self._set('_task_graph', task_graph)

    @property
    def cot_dir(self):
        """str: the local path containing this link's artifacts."""
        return self.get_artifact_full_path(path='.')

    def get_artifact_full_path(self, path):
        """str: the full path where an artifact should be located."""
        return get_single_upstream_artifact_full_path(self.context, self.task_id, path)


# raise_on_errors {{{1
def raise_on_errors(errors, level=logging.CRITICAL):
    """Raise a CoTError if errors.

    Helper function because I had this code block everywhere.

    Args:
        errors (list): the error errors
        level (int, optional): the log level to use.  Defaults to logging.CRITICAL

    Raises:
        CoTError: if errors is non-empty

    """
    if errors:
        log.log(level, "\n".join(errors))
        raise CoTError("\n".join(errors))


# guess_worker_impl {{{1
def guess_worker_impl(link):
    """Given a task, determine which worker implementation (e.g., docker-worker) it was run on.

    Currently there are no task markers for taskcluster-worker.  Those need to
    be populated here once they're ready.

    * docker-worker: ``task.payload.image`` is not None
    * check for scopes beginning with the worker type name.
    * generic-worker: ``task.payload.osGroups`` is not None
    * generic-worker: ``task.payload.mounts`` is not None

    Args:
        link (LinkOfTrust or ChainOfTrust): the link to check.

    Returns:
        str: the worker type.

    Raises:
        CoTError: on inability to determine the worker implementation

    """
    worker_impls = []
    task = link.task
    name = link.name
    errors = []

    if task['payload'].get("image"):
        worker_impls.append("docker-worker")
    if task['provisionerId'] in link.context.config['scriptworker_provisioners']:
        worker_impls.append("scriptworker")
    if task['workerType'] in link.context.config['scriptworker_worker_types']:
        worker_impls.append("scriptworker")
    if task['payload'].get("mounts") is not None:
        worker_impls.append("generic-worker")
    if task['payload'].get("osGroups") is not None:
        worker_impls.append("generic-worker")

    for scope in task['scopes']:
        if scope.startswith("docker-worker:"):
            worker_impls.append("docker-worker")

    if not worker_impls:
        errors.append("guess_worker_impl: can't find a worker_impl for {}!\n{}".format(name, task))
    if len(set(worker_impls)) > 1:
        errors.append("guess_worker_impl: too many matches for {}: {}!\n{}".format(name, set(worker_impls), task))
    raise_on_errors(errors)
    log.debug("{} {} is {}".format(name, link.task_id, worker_impls[0]))
    return worker_impls[0]


# get_valid_worker_impls {{{1
def get_valid_worker_impls():
    """Get the valid worker_impls, e.g. docker-worker.

    No longer a constant, due to code ordering issues.

    Returns:
        frozendict: maps the valid worker_impls (e.g., docker-worker) to their
            validation functions.

    """
    # TODO support taskcluster worker
    return frozendict({
        'docker-worker': verify_docker_worker_task,
        'generic-worker': verify_generic_worker_task,
        'scriptworker': verify_scriptworker_task,
    })


# guess_task_type {{{1
def guess_task_type(name, task_defn):
    """Guess the task type of the task.

    Args:
        name (str): the name of the task.

    Returns:
        str: the task_type.

    Raises:
        CoTError: on invalid task_type.

    """
    parts = name.split(':')
    task_type = parts[-1]
    if task_type == 'parent':
        if is_action(task_defn):
            task_type = 'action'
        else:
            task_type = 'decision'
    if task_type not in get_valid_task_types():
        raise CoTError(
            "Invalid task type for {}!".format(name)
        )
    return task_type


# get_valid_task_types {{{1
def get_valid_task_types():
    """Get the valid task types, e.g. signing.

    No longer a constant, due to code ordering issues.

    Returns:
        frozendict: maps the valid task types (e.g., signing) to their validation functions.

    """
    return frozendict({
        'scriptworker': verify_scriptworker_task,
        'balrog': verify_balrog_task,
        'beetmover': verify_beetmover_task,
        'bouncer': verify_bouncer_task,
        'build': verify_build_task,
        'l10n': verify_build_task,
        'repackage': verify_build_task,
        'action': verify_parent_task,
        'decision': verify_parent_task,
        'docker-image': verify_docker_image_task,
        'pushapk': verify_pushapk_task,
        'shipit': verify_shipit_task,
        'signing': verify_signing_task,
        'partials': verify_partials_task,
    })


# check_interactive_docker_worker {{{1
def check_interactive_docker_worker(link):
    """Given a task, make sure the task was not defined as interactive.

    * ``task.payload.features.interactive`` must be absent or False.
    * ``task.payload.env.TASKCLUSTER_INTERACTIVE`` must be absent or False.

    Args:
        link (LinkOfTrust): the task link we're checking.

    Returns:
        list: the list of error errors.  Success is an empty list.

    """
    errors = []
    log.info("Checking for {} {} interactive docker-worker".format(link.name, link.task_id))
    try:
        if link.task['payload']['features'].get('interactive'):
            errors.append("{} is interactive: task.payload.features.interactive!".format(link.name))
        if link.task['payload']['env'].get('TASKCLUSTER_INTERACTIVE'):
            errors.append("{} is interactive: task.payload.env.TASKCLUSTER_INTERACTIVE!".format(link.name))
    except KeyError:
        errors.append("check_interactive_docker_worker: {} task definition is malformed!".format(link.name))
    return errors


# verify_docker_image_sha {{{1
def verify_docker_image_sha(chain, link):
    """Verify that pre-built docker shas are in allowlists.

    Decision and docker-image tasks use pre-built docker images from docker hub.
    Verify that these pre-built docker image shas are in the allowlists.

    Args:
        chain (ChainOfTrust): the chain we're operating on.
        link (LinkOfTrust): the task link we're checking.

    Raises:
        CoTError: on failure.

    """
    cot = link.cot
    task = link.task
    errors = []

    if not cot:
        log.warn('Chain of Trust for {} does not exist. See above log for more details. \
Skipping docker image sha verification'.format(task['taskId']))
        return

    if isinstance(task['payload'].get('image'), dict):
        # Using pre-built image from docker-image task
        docker_image_task_id = task['extra']['chainOfTrust']['inputs']['docker-image']
        log.debug("Verifying {} {} against docker-image {}".format(
            link.name, link.task_id, docker_image_task_id
        ))
        if docker_image_task_id != task['payload']['image']['taskId']:
            errors.append("{} {} docker-image taskId isn't consistent!: {} vs {}".format(
                link.name, link.task_id, docker_image_task_id,
                task['payload']['image']['taskId']
            ))
        else:
            path = task['payload']['image']['path']
            # we need change the hash alg everywhere if we change, and recreate
            # the docker images...
            image_hash = cot['environment']['imageArtifactHash']
            alg, sha = image_hash.split(':')
            docker_image_link = chain.get_link(docker_image_task_id)
            upstream_sha = docker_image_link.cot['artifacts'].get(path, {}).get(alg)
            if upstream_sha is None:
                errors.append("{} {} docker-image docker sha {} is missing! {}".format(
                    link.name, link.task_id, alg,
                    docker_image_link.cot['artifacts'][path]
                ))
            elif upstream_sha != sha:
                errors.append("{} {} docker-image docker sha doesn't match! {} {} vs {}".format(
                    link.name, link.task_id, alg, sha, upstream_sha
                ))
            else:
                log.debug("Found matching docker-image sha {}".format(upstream_sha))
    else:
        # Using downloaded image from docker hub
        task_type = link.task_type
        image_hash = cot['environment']['imageHash']
        # Use the decision docker_image_allowlist for action tasks.
        if task_type == 'action':
            task_type = 'decision'
        if image_hash not in link.context.config['docker_image_allowlists'][task_type]:
            errors.append("{} {} docker imageHash {} not in the allowlist!\n{}".format(
                link.name, link.task_id, image_hash, cot
            ))
        else:
            log.debug("Found allowlisted image_hash {}".format(image_hash))
    raise_on_errors(errors)


# find_sorted_task_dependencies {{{1
def find_sorted_task_dependencies(task, task_name, task_id):
    """Find the taskIds of the chain of trust dependencies of a given task.

    Args:
        task (dict): the task definition to inspect.
        task_name (str): the name of the task, for logging and naming children.
        task_id (str): the taskId of the task.

    Returns:
        list: tuples associating dependent task ``name`` to dependent task ``taskId``.

    """
    log.info("find_sorted_task_dependencies {} {}".format(task_name, task_id))

    cot_input_dependencies = [
        _craft_dependency_tuple(task_name, task_type, task_id)
        for task_type, task_id in task['extra'].get('chainOfTrust', {}).get('inputs', {}).items()
    ]

    upstream_artifacts_dependencies = [
        _craft_dependency_tuple(task_name, artifact_dict['taskType'], artifact_dict['taskId'])
        for artifact_dict in task.get('payload', {}).get('upstreamArtifacts', [])
    ]

    dependencies = [*cot_input_dependencies, *upstream_artifacts_dependencies]
    dependencies = _sort_dependencies_by_name_then_task_id(dependencies)

    # bug 1396517 - Decision tasks are standalone; don't point at another task
    # even if the taskGroupId doesn't match.
    # XXX remove this workaround when all trees are 59+
    task_type = guess_task_type(task_name, task)
    if task_type in DECISION_TASK_TYPES:
        parent_task_id = task_id
        parent_task_type = 'decision'
    else:
        parent_task_id = get_parent_task_id(task) or get_decision_task_id(task)
        parent_task_type = 'parent'
    # make sure we deal with the decision task first, or we may populate
    # signing:build0:decision before signing:decision
    parent_tuple = _craft_dependency_tuple(task_name, parent_task_type, parent_task_id)
    dependencies.insert(0, parent_tuple)

    log.info('found dependencies: {}'.format(dependencies))
    return dependencies


def _craft_dependency_tuple(task_name, task_type, task_id):
    return ('{}:{}'.format(task_name, task_type), task_id)


def _sort_dependencies_by_name_then_task_id(dependencies):
    return sorted(dependencies, key=lambda dep: '{}_{}'.format(dep[0], dep[1]))


# build_task_dependencies {{{1
async def build_task_dependencies(chain, task, name, my_task_id):
    """Recursively build the task dependencies of a task.

    Args:
        chain (ChainOfTrust): the chain of trust to add to.
        task (dict): the task definition to operate on.
        name (str): the name of the task to operate on.
        my_task_id (str): the taskId of the task to operate on.

    Raises:
        CoTError: on failure.

    """
    log.info("build_task_dependencies {} {}".format(name, my_task_id))
    if name.count(':') > chain.context.config['max_chain_length']:
        raise CoTError("Too deep recursion!\n{}".format(name))
    sorted_dependencies = find_sorted_task_dependencies(task, name, my_task_id)

    for task_name, task_id in sorted_dependencies:
        if task_id not in chain.dependent_task_ids():
            link = LinkOfTrust(chain.context, task_name, task_id)
            json_path = link.get_artifact_full_path('task.json')
            try:
                task_defn = await chain.context.queue.task(task_id)
                link.task = task_defn
                chain.links.append(link)
                # write task json to disk
                makedirs(os.path.dirname(json_path))
                with open(json_path, 'w') as fh:
                    fh.write(format_json(task_defn))
                await build_task_dependencies(chain, task_defn, task_name, task_id)
            except TaskclusterFailure as exc:
                raise CoTError(str(exc))


# download_cot {{{1
async def download_cot(chain):
    """Download the signed chain of trust artifacts.

    Args:
        chain (ChainOfTrust): the chain of trust to add to.

    Raises:
        DownloadError: on failure.

    """
    mandatory_artifact_tasks = []
    optional_artifact_tasks = []
    # only deal with chain.links, which are previously finished tasks with
    # signed chain of trust artifacts.  ``chain.task`` is the current running
    # task, and will not have a signed chain of trust artifact yet.
    for link in chain.links:
        task_id = link.task_id
        url = get_artifact_url(chain.context, task_id, 'public/chainOfTrust.json.asc')
        parent_dir = link.cot_dir
        coroutine = asyncio.ensure_future(
            download_artifacts(
                chain.context, [url], parent_dir=parent_dir,
                valid_artifact_task_ids=[task_id]
            )
        )

        if is_task_required_by_any_mandatory_artifact(chain, task_id):
            mandatory_artifact_tasks.append(coroutine)
        else:
            optional_artifact_tasks.append(coroutine)

    mandatory_artifacts_paths = await raise_future_exceptions(mandatory_artifact_tasks)
    succeeded_optional_artifacts_paths, failed_optional_artifacts = \
        await get_results_and_future_exceptions(optional_artifact_tasks)

    if failed_optional_artifacts:
        error_messages = '\n'.join([' * {}'.format(failure) for failure in failed_optional_artifacts])
        log.warn('Could not download {} "chainOfTrust.json.asc". Although, they were not needed by \
any mandatory artifact. Continuing CoT verifications. Errors gotten: {}'.format(len(failed_optional_artifacts), error_messages))

    paths = mandatory_artifacts_paths + succeeded_optional_artifacts_paths
    for path in paths:
        sha = get_hash(path[0])
        log.debug("{} downloaded; hash is {}".format(path[0], sha))


# download_cot_artifact {{{1
async def download_cot_artifact(chain, task_id, path):
    """Download an artifact and verify its SHA against the chain of trust.

    Args:
        chain (ChainOfTrust): the chain of trust object
        task_id (str): the task ID to download from
        path (str): the relative path to the artifact to download

    Returns:
        str: the full path of the downloaded artifact

    Raises:
        CoTError: on failure.

    """
    link = chain.get_link(task_id)
    log.debug("Verifying {} is in {} cot artifacts...".format(path, task_id))
    if not link.cot:
        log.warn('Chain of Trust for "{}" in {} does not exist. See above log for more details. \
Skipping download of this artifact'.format(path, task_id))
        return

    if path not in link.cot['artifacts']:
        raise CoTError("path {} not in {} {} chain of trust artifacts!".format(path, link.name, link.task_id))
    url = get_artifact_url(chain.context, task_id, path)
    loggable_url = get_loggable_url(url)
    log.info("Downloading Chain of Trust artifact:\n{}".format(loggable_url))
    await download_artifacts(
        chain.context, [url], parent_dir=link.cot_dir, valid_artifact_task_ids=[task_id]
    )
    full_path = link.get_artifact_full_path(path)
    for alg, expected_sha in link.cot['artifacts'][path].items():
        if alg not in chain.context.config['valid_hash_algorithms']:
            raise CoTError("BAD HASH ALGORITHM: {}: {} {}!".format(link.name, alg, full_path))
        real_sha = get_hash(full_path, hash_alg=alg)
        if expected_sha != real_sha:
            raise CoTError("BAD HASH: {}: Expected {} {}; got {}!".format(link.name, alg, expected_sha, real_sha))
        log.debug("{} matches the expected {} {}".format(full_path, alg, expected_sha))
    return full_path


# download_cot_artifacts {{{1
async def download_cot_artifacts(chain):
    """Call ``download_cot_artifact`` in parallel for each "upstreamArtifacts".

    Optional artifacts are allowed to not be downloaded.

    Args:
        chain (ChainOfTrust): the chain of trust object

    Returns:
        list: list of full paths to downloaded artifacts. Failed optional artifacts
        aren't returned

    Raises:
        CoTError: on chain of trust sha validation error, on a mandatory artifact
        DownloadError: on download error on a mandatory artifact

    """
    upstream_artifacts = chain.task['payload'].get('upstreamArtifacts', [])
    all_artifacts_per_task_id = get_all_artifacts_per_task_id(chain, upstream_artifacts)

    mandatory_artifact_tasks = []
    optional_artifact_tasks = []
    for task_id, paths in all_artifacts_per_task_id.items():
        for path in paths:
            coroutine = asyncio.ensure_future(download_cot_artifact(chain, task_id, path))

            if is_artifact_optional(chain, task_id, path):
                optional_artifact_tasks.append(coroutine)
            else:
                mandatory_artifact_tasks.append(coroutine)

    mandatory_artifacts_paths = await raise_future_exceptions(mandatory_artifact_tasks)
    succeeded_optional_artifacts_paths, failed_optional_artifacts = \
        await get_results_and_future_exceptions(optional_artifact_tasks)

    if failed_optional_artifacts:
        log.warn('Could not download {} artifacts: {}'.format(len(failed_optional_artifacts), failed_optional_artifacts))

    return mandatory_artifacts_paths + succeeded_optional_artifacts_paths


def is_task_required_by_any_mandatory_artifact(chain, task_id):
    """Tells whether a task has only optional artifacts or not.

    Args:
        chain (ChainOfTrust): the chain of trust object
        task_id (str): the id of the aforementioned task

    Returns:
        bool: True if task has one or several mandatory artifacts

    """
    upstream_artifacts = chain.task['payload'].get('upstreamArtifacts', [])
    all_artifacts_per_task_id = get_all_artifacts_per_task_id(chain, upstream_artifacts)
    optional_artifacts_per_task_id = get_optional_artifacts_per_task_id(upstream_artifacts)

    all_artifacts = all_artifacts_per_task_id.get(task_id, [])
    optional_artifacts = optional_artifacts_per_task_id.get(task_id, [])
    mandatory_artifacts = set(all_artifacts) - set(optional_artifacts)
    return bool(mandatory_artifacts)


def is_artifact_optional(chain, task_id, path):
    """Tells whether an artifact is flagged as optional or not.

    Args:
        chain (ChainOfTrust): the chain of trust object
        task_id (str): the id of the aforementioned task

    Returns:
        bool: True if artifact is optional

    """
    upstream_artifacts = chain.task['payload'].get('upstreamArtifacts', [])
    optional_artifacts_per_task_id = get_optional_artifacts_per_task_id(upstream_artifacts)
    return path in optional_artifacts_per_task_id.get(task_id, [])


def get_all_artifacts_per_task_id(chain, upstream_artifacts):
    """Return every artifact to download, including the Chain Of Trust Artifacts.

    Args:
        chain (ChainOfTrust): the chain of trust object
        upstream_artifacts: the list of upstream artifact definitions

    Returns:
        dict: list of paths to downloaded artifacts ordered by taskId

    """
    all_artifacts_per_task_id = {}
    for link in chain.links:
        # Download task-graph.json for decision+action task cot verification
        if link.task_type in PARENT_TASK_TYPES:
            add_enumerable_item_to_dict(
                dict_=all_artifacts_per_task_id, key=link.task_id, item='public/task-graph.json'
            )
        # Download actions.json for decision+action task cot verification
        if link.task_type in DECISION_TASK_TYPES:
            add_enumerable_item_to_dict(
                dict_=all_artifacts_per_task_id, key=link.task_id, item='public/actions.json'
            )
            add_enumerable_item_to_dict(
                dict_=all_artifacts_per_task_id, key=link.task_id, item='public/parameters.yml'
            )

    if upstream_artifacts:
        for upstream_dict in upstream_artifacts:
            add_enumerable_item_to_dict(
                dict_=all_artifacts_per_task_id, key=upstream_dict['taskId'], item=upstream_dict['paths']
            )

    return all_artifacts_per_task_id


# verify_cot_signatures {{{1
def verify_cot_signatures(chain):
    """Verify the signatures of the chain of trust artifacts populated in ``download_cot``.

    Populate each link.cot with the chain of trust json body.

    Args:
        chain (ChainOfTrust): the chain of trust to add to.

    Raises:
        CoTError: on failure.

    """
    for link in chain.links:
        path = link.get_artifact_full_path('public/chainOfTrust.json.asc')
        gpg_home = os.path.join(chain.context.config['base_gpg_home_dir'], link.worker_impl)
        gpg = GPG(chain.context, gpg_home=gpg_home)
        log.debug("Verifying the {} {} chain of trust signature against {}".format(
            link.name, link.task_id, gpg_home
        ))
        try:
            with open(path, "r") as fh:
                contents = fh.read()
        except OSError as exc:
            if is_task_required_by_any_mandatory_artifact(chain, link.task_id):
                raise CoTError("Can't read mandatory {}: {}!".format(path, str(exc)))
            else:
                log.warn("Could not read optional {}. Continuing. Error gotten: {}!".format(path, str(exc)))
                continue
        try:
            body = get_body(
                gpg, contents,
                verify_sig=chain.context.config['verify_cot_signature']
            )
        except ScriptWorkerGPGException as exc:
            raise CoTError("GPG Error verifying chain of trust for {}: {}!".format(path, str(exc)))
        link.cot = load_json_or_yaml(
            body, exception=CoTError,
            message="{} {}: Invalid cot json body! %(exc)s".format(link.name, link.task_id)
        )
        unsigned_path = link.get_artifact_full_path('chainOfTrust.json')
        log.debug("Good.  Writing json contents to {}".format(unsigned_path))
        with open(unsigned_path, "w") as fh:
            fh.write(format_json(link.cot))


# verify_task_in_task_graph {{{1
def verify_task_in_task_graph(task_link, graph_defn, level=logging.CRITICAL):
    """Verify a given task_link's task against a given graph task definition.

    This is a helper function for ``verify_link_in_task_graph``; this is split
    out so we can call it multiple times when we fuzzy match.

    Args:
        task_link (LinkOfTrust): the link to try to match
        graph_defn (dict): the task definition from the task-graph.json to match
            ``task_link`` against
        level (int, optional): the logging level to use on errors. Defaults to logging.CRITICAL

    Raises:
        CoTError: on failure

    """
    ignore_keys = ("created", "deadline", "expires", "dependencies", "schedulerId")
    errors = []
    runtime_defn = deepcopy(task_link.task)
    # dependencies
    # Allow for a subset of dependencies in a retriggered task.  The current use case
    # is release promotion: we may hit the expiration deadline for a task (e.g. pushapk),
    # and a breakpoint task in the graph may also hit its expiration.  To kick off
    # the pushapk task, we can clone the task, update timestamps, and remove the
    # breakpoint dependency.
    bad_deps = set(runtime_defn['dependencies']) - set(graph_defn['task']['dependencies'])
    # it's OK if a task depends on the decision task
    bad_deps = bad_deps - {task_link.decision_task_id}
    if bad_deps:
        errors.append("{} {} dependencies don't line up!\n{}".format(
            task_link.name, task_link.task_id, bad_deps
        ))
    # payload - eliminate the 'expires' key from artifacts because the datestring
    # will change
    runtime_defn['payload'] = _take_expires_out_from_artifacts_in_payload(runtime_defn['payload'])
    graph_defn['task']['payload'] = _take_expires_out_from_artifacts_in_payload(graph_defn['task']['payload'])

    # test all non-ignored key/value pairs in the task defn
    for key, value in graph_defn['task'].items():
        if key in ignore_keys:
            continue
        if value != runtime_defn[key]:
            errors.append("{} {} {} differs!\n graph: {}\n task: {}".format(
                task_link.name, task_link.task_id, key,
                format_json(value), format_json(runtime_defn[key])
            ))
    raise_on_errors(errors, level=level)


def _take_expires_out_from_artifacts_in_payload(payload):
    returned_payload = deepcopy(payload)
    artifacts = returned_payload.get('artifacts', None)
    if artifacts is None:
        return returned_payload
    elif type(artifacts) not in (dict, list):
        raise CoTError('Unsupported type of artifacts. Found: "{}". Expected: dict, list or undefined. Payload: {}'.format(
            type(artifacts), payload
        ))

    artifacts_iterable = artifacts.values() if isinstance(artifacts, dict) else artifacts
    for artifact_definition in artifacts_iterable:
        if isinstance(artifact_definition, dict) and 'expires' in artifact_definition:
            del(artifact_definition['expires'])

    return returned_payload


# verify_link_in_task_graph {{{1
def verify_link_in_task_graph(chain, decision_link, task_link):
    """Compare the runtime task definition against the decision task graph.

    If the ``task_link.task_id`` is in the task graph, match directly against
    that task definition.  Otherwise, "fuzzy match" by trying to match against
    any definition in the task graph.  This is to support retriggers, where
    the task definition stays the same, but the datestrings and taskIds change.

    Args:
        chain (ChainOfTrust): the chain we're operating on.
        decision_link (LinkOfTrust): the decision task link
        task_link (LinkOfTrust): the task link we're testing

    Raises:
        CoTError: on failure.

    """
    log.info("Verifying the {} {} task definition is part of the {} {} task graph...".format(
        task_link.name, task_link.task_id, decision_link.name, decision_link.task_id
    ))
    if task_link.task_id in decision_link.task_graph:
        graph_defn = deepcopy(decision_link.task_graph[task_link.task_id])
        verify_task_in_task_graph(task_link, graph_defn)
        log.info("Found {} in the graph; it's a match".format(task_link.task_id))
        return
    # Fall back to fuzzy matching to support retriggers: the taskId and
    # datestrings will change but the task definition shouldn't.
    for task_id, graph_defn in decision_link.task_graph.items():
        log.debug("Fuzzy matching against {} ...".format(task_id))
        try:
            verify_task_in_task_graph(task_link, graph_defn, level=logging.DEBUG)
            log.info("Found a {} fuzzy match with {} ...".format(task_link.task_id, task_id))
            return
        except CoTError:
            pass
    else:
        raise_on_errors(["Can't find task {} {} in {} {} task-graph.json!".format(
            task_link.name, task_link.task_id, decision_link.name, decision_link.task_id
        )])


# verify_decision_command {{{1
def verify_decision_command(decision_link, mach_commands=DECISION_MACH_COMMANDS):
    r"""Verify the decision command for a decision task.

    This is deprecated, but still very much in use.
    Let's stop needing it.

    Some example commands::

        "/builds/worker/bin/run-task",
        "--vcs-checkout=/builds/worker/checkouts/gecko",
        "--",
        "bash",
        "-cx",
        "cd /builds/worker/checkouts/gecko &&
        ln -s /builds/worker/artifacts artifacts &&
        ./mach --log-no-times taskgraph decision --pushlog-id='83445' --pushdate='1478146854'
        --project='mozilla-inbound' --message=' ' --owner='cpeterson@mozilla.com' --level='3'
        --base-repository='https://hg.mozilla.org/mozilla-central'
        --head-repository='https://hg.mozilla.org/integration/mozilla-inbound/'
        --head-ref='e7023fe48f7c48e33ef3b91747647f0873e306d6'
        --head-rev='e7023fe48f7c48e33ef3b91747647f0873e306d6'
        --revision-hash='e3e8f6327079496707658adc381c142c6575b280'\n"

        "/builds/worker/bin/run-task",
        "--vcs-checkout=/builds/worker/checkouts/gecko",
        "--",
        "bash",
        "-cx",
        "cd /builds/worker/checkouts/gecko &&
        ln -s /builds/worker/artifacts artifacts &&
        ./mach --log-no-times taskgraph decision --pushlog-id='0' --pushdate='0' --project='date'
        --message='try: -b o -p foo -u none -t none' --owner='amiyaguchi@mozilla.com' --level='2'
        --base-repository=$GECKO_BASE_REPOSITORY --head-repository=$GECKO_HEAD_REPOSITORY
        --head-ref=$GECKO_HEAD_REF --head-rev=$GECKO_HEAD_REV --revision-hash=$GECKO_HEAD_REV
        --triggered-by='nightly' --target-tasks-method='nightly_linux'\n"

    This is very firefox-centric and potentially fragile, but decision tasks are
    important enough to need to monitor.  The ideal fix would maybe be to simplify
    the commandline if possible.

    Args:
        chain (ChainOfTrust): the chain we're operating on.
        decision_link (LinkOfTrust): the decision link to test.
        mach_commands (tuple): a tuple of tuples, specifying the allowlisted
            mach commands for a decision task, ignoring options.

    Raises:
        CoTError: on chain of trust verification error.

    """
    log.info("Verifying {} {} command...".format(decision_link.name, decision_link.task_id))
    errors = []
    command = decision_link.task['payload']['command']
    allowed_args = ('--', 'bash', '/bin/bash', '-cx')
    # /home/worker is an old path, before https://bugzilla.mozilla.org/show_bug.cgi?id=1338651#c195
    if command[0] not in('/home/worker/bin/run-task', '/builds/worker/bin/run-task'):
        errors.append("{} {} command must start with /builds/worker/bin/run-task!".format(
            decision_link.name, decision_link.task_id
        ))
    for item in command[1:-1]:
        if item in allowed_args:
            continue
        if item.startswith(('--vcs-checkout=', '--sparse-profile=')):
            continue
        if item.startswith(tuple(decision_link.context.config['extra_run_task_arguments'])):
            continue
        errors.append("{} {} illegal option {} in the command!".format(
            decision_link.name, decision_link.task_id, item
        ))
    bash_commands = command[-1].split('&&')
    allowed_commands = ('cd', 'ln')
    for bash_command in bash_commands:
        parts = shlex.split(bash_command)
        non_options = []
        if parts[0] in allowed_commands:
            continue
        for part in parts:
            if part.startswith('--'):
                continue
            non_options.append(part)
        for mach_command in mach_commands:
            if tuple(non_options) == mach_command:
                break
        else:
            errors.append("{} {} Illegal command ``{}``".format(
                decision_link.name, decision_link.task_id, bash_command
            ))
    raise_on_errors(errors)


# get_pushlog_info {{{1
async def get_pushlog_info(decision_link):
    """Get pushlog info for a decision LinkOfTrust.

    Args:
        decision_link (LinkOfTrust): the decision link to get pushlog info about.

    Returns:
        dict: pushlog info.

    """
    source_env_prefix = decision_link.context.config['source_env_prefix']
    repo = get_repo(decision_link.task, source_env_prefix)
    rev = get_revision(decision_link.task, source_env_prefix)
    context = decision_link.context
    pushlog_url = context.config['pushlog_url'].format(
        repo=repo, revision=rev
    )
    log.info("Pushlog url {}".format(pushlog_url))
    file_path = os.path.join(context.config["work_dir"], "{}_push_log.json".format(decision_link.name))
    pushlog_info = await load_json_or_yaml_from_url(
        context, pushlog_url, file_path, overwrite=False
    )
    if len(pushlog_info['pushes']) != 1:
        log.warning("Pushlog error: expected a single push at {} but got {}!".format(
            pushlog_url, pushlog_info['pushes']
        ))
    return pushlog_info


# get_scm_level {{{1
async def get_scm_level(context, project):
    """Get the scm level for a project from ``projects.yml``.

    We define all known projects in ``projects.yml``. Let's make sure we have
    it populated in ``context``, then return the scm level of ``project``.

    SCM levels are an integer, 1-3, matching Mozilla commit levels.
    https://www.mozilla.org/en-US/about/governance/policies/commit/access-policy/

    Args:
        context (scriptworker.context.Context): the scriptworker context
        project (str): the project to get the scm level for.

    Returns:
        str: the level of the project, as a string.

    """
    await context.populate_projects()
    level = context.projects[project]['access'].replace("scm_level_", "")
    return level


# populate_jsone_context {{{1
async def _get_additional_action_jsone_context(parent_link, decision_link):
    params_path = decision_link.get_artifact_full_path('public/parameters.yml')
    parameters = load_json_or_yaml(params_path, is_path=True, file_type='yaml')
    jsone_context = deepcopy(parent_link.task['extra']['action']['context'])
    jsone_context['parameters'] = parameters
    jsone_context['task'] = None
    jsone_context['ownTaskId'] = parent_link.task_id
    return jsone_context


async def _get_additional_hgpush_jsone_context(parent_link, decision_link):
    source_env_prefix = decision_link.context.config['source_env_prefix']
    rev = get_revision(decision_link.task, source_env_prefix)
    pushlog_info = await get_pushlog_info(decision_link)
    pushlog_id = list(pushlog_info['pushes'].keys())[0]
    decision_comment = get_commit_message(decision_link.task)
    push_comment = pushlog_info['pushes'][pushlog_id]['changesets'][0]['desc']
    if decision_comment not in (' ', push_comment):
        raise CoTError(
            "Decision task {} comment doesn't match the push comment!\n"
            "Decision comment: \n{}\nPush comment: \n{}".format(
                decision_link.name, decision_comment, push_comment
            )
        )
    return {
        "push": {
            "revision": rev,
            "comment": decision_comment,
            "owner": pushlog_info['pushes'][pushlog_id]['user'],
            "pushlog_id": pushlog_id,
            "pushdate": pushlog_info['pushes'][pushlog_id]['date'],
        }
    }


async def _get_additional_cron_jsone_context(parent_link, decision_link):
    jsone_context = {}
    source_env_prefix = decision_link.context.config['source_env_prefix']
    rev = get_revision(decision_link.task, source_env_prefix)
    jsone_context['cron'] = load_json_or_yaml(parent_link.task['extra']['cron'])
    # I don't love these hardcodes.
    jsone_context["push"] = {
        "revision": rev,
        "comment": '',
        "owner": 'nobody',
        "pushlog_id": '-1',
        "pushdate": '0',
    }
    return jsone_context


async def populate_jsone_context(chain, parent_link, decision_link, tasks_for):
    """Populate the json-e context to rebuild ``parent_link``'s task definition.

    Args:
        chain (ChainOfTrust): the chain of trust to add to.
        parent_link (LinkOfTrust): the parent link to test.
        decision_link (LinkOfTrust): the parent link's decision task link.
        tasks_for (str): the reason the parent link was created (cron,
            hg-push, action)

    Raises:
        CoTError, KeyError, ValueError: on failure.

    Returns:
        dict: the json-e context.

    """
    task_ids = {
         "default": parent_link.task_id,
         "decision": decision_link.task_id,
    }
    repo = get_repo(decision_link.task, source_env_prefix=decision_link.context.config['source_env_prefix'])
    source_url = get_source_url(decision_link)
    project = get_and_check_project(chain.context.config['valid_vcs_rules'], source_url)
    level = await get_scm_level(chain.context, project)
    log.debug("task_ids: {}".format(task_ids))
    jsone_context = {
        'now': parent_link.task['created'],
        'as_slugid': lambda x: task_ids.get(x, task_ids['default']),
        'tasks_for': tasks_for,
        'repository': {
            'level': level,
            'url': repo,
            'project': project,
        },
        'taskId': None
    }
    if tasks_for == 'action':
        jsone_context.update(
            await _get_additional_action_jsone_context(parent_link, decision_link)
        )
    elif tasks_for == 'hg-push':
        jsone_context.update(
            await _get_additional_hgpush_jsone_context(parent_link, decision_link)
        )
    else:
        jsone_context.update(
            await _get_additional_cron_jsone_context(parent_link, decision_link)
        )
    log.debug("{} json-e context:".format(parent_link.name))
    log.debug(pprint.pformat(jsone_context))
    return jsone_context


# get_jsone_template {{{1
async def get_jsone_template(parent_link, decision_link, tasks_for):
    """Get the appropriate json-e template.

    Args:
        parent_link (LinkOfTrust): the parent link to test.
        decision_link (LinkOfTrust): the parent link's decision task link.
        tasks_for (str): the reason the parent link was created (cron,
            hg-push, action)

    Returns:
        dict: the json-e template.

    """
    if tasks_for == 'action':
        actions_path = decision_link.get_artifact_full_path('public/actions.json')
        all_actions = load_json_or_yaml(actions_path, is_path=True)['actions']
        action_name = get_action_name(parent_link.task)
        tmpl = [d for d in all_actions if d['name'] == action_name][0]['task']
    else:
        context = decision_link.context
        source_url = get_source_url(decision_link)
        tmpl = await load_json_or_yaml_from_url(
            context, source_url, os.path.join(
                context.config["work_dir"], "{}_taskcluster.yml".format(decision_link.name)
            )
        )
        tmpl = tmpl['tasks'][0]
    log.debug("{} json-e template:".format(parent_link.name))
    log.debug(format_json(tmpl))
    return tmpl


# verify_parent_task_definition {{{1
async def verify_parent_task_definition(chain, parent_link):
    """Rebuild the decision/action/cron task definition via json-e.

    This is Chain of Trust verification version 2, aka cotv2.
    Instead of looking at various parts of the parent task's task definition
    and making sure they look well-formed, let's rebuild the task definition
    from the tree and make sure it matches.

    We use the the link with the ``task_id`` of ``parent_link.decision_task_id``
    for a number of the checks here. If ``parent_link`` is a decision or cron
    task, they're the same task. If ``parent_link`` is an action task, this
    will reference the decision task that the action task is based off of.

    Args:
        chain (ChainOfTrust): the chain of trust to add to.
        parent_link (LinkOfTrust): the parent link to test.

    Raises:
        CoTError: on failure.

    """
    log.info("Verifying {} {} definition...".format(parent_link.name, parent_link.task_id))
    decision_link = chain.get_link(parent_link.decision_task_id)
    try:
        tasks_for = get_and_check_tasks_for(
            parent_link.task, '{} {}: '.format(parent_link.name, parent_link.task_id)
        )
        tmpl = await get_jsone_template(parent_link, decision_link, tasks_for)
        jsone_context = await populate_jsone_context(
            chain, parent_link, decision_link, tasks_for
        )
        rebuilt_definition = jsone.render(tmpl, jsone_context)
    except jsone.JSONTemplateError as e:
        log.exception("JSON-e error while rebuilding {} task definition!".format(parent_link.name))
        raise CoTError("JSON-e error while rebuilding {} task definition: {}".format(parent_link.name, str(e)))
    except (KeyError, ValueError) as e:
        msg = "Error while rebuilding {} {} task definition!".format(
            parent_link.name, parent_link.task_id
        )
        log.exception(msg)
        raise CoTError(msg + "\n{}".format(str(e)))

    compare_jsone_task_definition(parent_link, rebuilt_definition)


# compare_jsone_task_definition {{{1
def compare_jsone_task_definition(parent_link, compare_definition):
    """Compare the json-e rebuilt task definition vs the runtime definition.

    Args:
        parent_link (LinkOfTrust): the parent link to test.
        compare_definition (dict): the rebuilt task definition.

    Raises:
        CoTError: on failure.

    """
    try:
        # Rebuilt decision tasks have an extra `taskId`; remove
        if 'taskId' in compare_definition:
            del(compare_definition['taskId'])
        # remove key/value pairs where the value is empty, since json-e drops
        # them instead of keeping them with a None/{}/[] value.
        compare_definition = remove_empty_keys(compare_definition)
        runtime_definition = remove_empty_keys(parent_link.task)
        log.debug("Compare_definition:\n{}".format(format_json(compare_definition)))
        log.debug("Runtime definition:\n{}".format(format_json(runtime_definition)))
        diff = list(dictdiffer.diff(compare_definition, runtime_definition))
        if diff:
            raise AssertionError(pprint.pformat(diff))
        log.info("{}: Good.".format(parent_link.name))
    except (AssertionError, KeyError):
        msg = "{} {}: the rebuilt definition doesn't match the runtime task!".format(
            parent_link.name, parent_link.task_id
        )
        log.exception(msg)
        raise CoTError(msg)


# verify_parent_task {{{1
async def verify_parent_task(chain, link):
    """Verify the parent task Link.

    Action task verification is currently in the same verification function as
    decision tasks, because sometimes we'll have an action task masquerading as
    a decision task, e.g. in templatized actions for release graphs. To make
    sure our guess of decision or action task isn't fatal, we call this
    function; this function uses ``is_action()`` to determine how to verify
    the task.

    Args:
        chain (ChainOfTrust): the chain we're operating on.
        link (LinkOfTrust): the task link we're checking.

    Raises:
        CoTError: on chain of trust verification error.

    """
    worker_type = get_worker_type(link.task)
    if worker_type not in chain.context.config['valid_decision_worker_types']:
        raise CoTError("{} is not a valid decision workerType!".format(worker_type))
    if chain is not link:
        # make sure all tasks generated from this parent task match the published
        # task-graph.json. Not applicable if this link is the ChainOfTrust object,
        # since this task won't have generated a task-graph.json yet.
        path = link.get_artifact_full_path('public/task-graph.json')
        if not os.path.exists(path):
            raise CoTError("{} {}: {} doesn't exist!".format(link.name, link.task_id, path))
        link.task_graph = load_json_or_yaml(
            path, is_path=True, exception=CoTError, message="Can't load {}! %(exc)s".format(path)
        )
        # This check may want to move to a per-task check?
        for target_link in chain.get_all_links_in_chain():
            # Verify the target's task is in the parent task's task graph, unless
            # it's this task or a parent task.
            # (Decision tasks will not exist in a parent task's task-graph.json;
            #  action tasks, which are generated later, will also be missing.)
            # https://github.com/mozilla-releng/scriptworker/issues/77
            if target_link.parent_task_id == link.task_id and \
                    target_link.task_id != link.task_id and \
                    target_link.task_type not in PARENT_TASK_TYPES:
                verify_link_in_task_graph(chain, link, target_link)
    try:
        # Try verifying decision task via json-e (cot v2)
        await verify_parent_task_definition(chain, link)
    except (CoTError, DownloadError, KeyError) as e:
        if chain.context.config['min_cot_version'] > 1:
            raise CoTError(e)
        # Fall back to cot v1.
        # XXX Get rid of the fallback when all trees are Fx59+.
        log.exception("Falling back to non-json-e decision task verification for {}!".format(link.task_id))
        if is_action(link.task):
            mach_commands = ACTION_MACH_COMMANDS
        else:
            mach_commands = DECISION_MACH_COMMANDS
        verify_decision_command(link, mach_commands=mach_commands)
        # log message for easy papertrail parsing
        log.warning("DEPRECATED_DECISION_TASK {} while verifying task {}".format(link.task_id, chain.task_id))


# verify_build_task {{{1
async def verify_build_task(chain, link):
    """Verify the build Link.

    The main points of concern are tested elsewhere:
    The task is the same as the task graph task; the command;
    the docker-image for docker-worker builds; the revision and repo.

    Args:
        chain (ChainOfTrust): the chain we're operating on.
        link (LinkOfTrust): the task link we're checking.

    """
    pass


# verify_docker_image_task {{{1
async def verify_docker_image_task(chain, link):
    """Verify the docker image Link.

    Args:
        chain (ChainOfTrust): the chain we're operating on.
        link (LinkOfTrust): the task link we're checking.

    """
    errors = []
    # workerType
    worker_type = get_worker_type(link.task)
    if worker_type not in chain.context.config['valid_docker_image_worker_types']:
        errors.append("{} is not a valid docker-image workerType!".format(worker_type))
    # XXX remove the command checks once we require json-e cot verification.
    if link.task['payload'].get('command') and link.task['payload']['command'] != ["/bin/bash", "-c", "/home/worker/bin/build_image.sh"]:
        errors.append("{} {} illegal command {}!".format(link.name, link.task_id, link.task['payload']['command']))
    raise_on_errors(errors)


# verify_balrog_task {{{1
async def verify_balrog_task(chain, obj):
    """Verify the balrog trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the balrog task.

    Raises:
        CoTError: on error.

    """
    return await verify_scriptworker_task(chain, obj)


# verify_partials_task {{{1
async def verify_partials_task(chain, obj):
    """Verify the partials trust object.

    The main points of concern are tested elsewhere:
    Runs as a docker-worker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the balrog task.

    Raises:
        CoTError: on error.

    """
    pass


# verify_beetmover_task {{{1
async def verify_beetmover_task(chain, obj):
    """Verify the beetmover trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the beetmover task.

    Raises:
        CoTError: on error.

    """
    return await verify_scriptworker_task(chain, obj)


async def verify_bouncer_task(chain, obj):
    """Verify the bouncer trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the beetmover task.

    Raises:
        CoTError: on error.

    """
    return await verify_scriptworker_task(chain, obj)


# verify_pushapk_task {{{1
async def verify_pushapk_task(chain, obj):
    """Verify the pushapk trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the pushapk task.

    Raises:
        CoTError: on error.

    """
    return await verify_scriptworker_task(chain, obj)


async def verify_shipit_task(chain, obj):
    """Verify the ship-it trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the ship-it task.

    Raises:
        CoTError: on error.

    """
    return await verify_scriptworker_task(chain, obj)


# verify_signing_task {{{1
async def verify_signing_task(chain, obj):
    """Verify the signing trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the signing task.

    Raises:
        CoTError: on error.

    """
    return await verify_scriptworker_task(chain, obj)


# check_num_tasks {{{1
def check_num_tasks(chain, task_count):
    """Make sure there are a specific number of specific task types.

    Currently we only check decision tasks.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        task_count (dict): mapping task type to the number of links.

    Raises:
        CoTError: on failure.

    """
    errors = []
    # hardcode for now.  If we need a different set of constraints, either
    # go by cot_product settings or by task_count['docker-image'] + 1
    min_decision_tasks = 1
    if task_count['decision'] < min_decision_tasks:
        errors.append("{} decision tasks; we must have at least {}!".format(
            task_count['decision'], min_decision_tasks
        ))
    raise_on_errors(errors)


# verify_task_types {{{1
async def verify_task_types(chain):
    """Verify the task type (e.g. decision, build) of each link in the chain.

    Args:
        chain (ChainOfTrust): the chain we're operating on

    Returns:
        dict: mapping task type to the number of links.

    """
    valid_task_types = get_valid_task_types()
    task_count = {}
    for obj in chain.get_all_links_in_chain():
        task_type = obj.task_type
        log.info("Verifying {} {} as a {} task...".format(obj.name, obj.task_id, task_type))
        task_count.setdefault(task_type, 0)
        task_count[task_type] += 1
        # Run tests synchronously for now.  We can parallelize if efficiency
        # is more important than a single simple logfile.
        await valid_task_types[task_type](chain, obj)
    return task_count


# verify_docker_worker_task {{{1
async def verify_docker_worker_task(chain, link):
    """Docker-worker specific checks.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        link (ChainOfTrust or LinkOfTrust): the trust object for the signing task.

    Raises:
        CoTError: on failure.

    """
    if chain != link:
        # These two checks will die on `link.cot` if `link` is a ChainOfTrust
        # object (e.g., the task we're running `verify_cot` against is a
        # docker-worker task). So only run these tests if they are not the chain
        # object.
        check_interactive_docker_worker(link)
        verify_docker_image_sha(chain, link)


# verify_generic_worker_task {{{1
async def verify_generic_worker_task(chain, link):
    """generic-worker specific checks.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        link (ChainOfTrust or LinkOfTrust): the trust object for the signing task.

    Raises:
        CoTError: on failure.

    """
    pass


# verify_scriptworker_task {{{1
async def verify_scriptworker_task(chain, obj):
    """Verify the signing trust object.

    Currently the only check is to make sure it was run on a scriptworker.

    Args:
        chain (ChainOfTrust): the chain we're operating on
        obj (ChainOfTrust or LinkOfTrust): the trust object for the signing task.

    """
    errors = []
    if obj.worker_impl != "scriptworker":
        errors.append("{} {} must be run from scriptworker!".format(obj.name, obj.task_id))
    raise_on_errors(errors)


# verify_worker_impls {{{1
async def verify_worker_impls(chain):
    """Verify the task type (e.g. decision, build) of each link in the chain.

    Args:
        chain (ChainOfTrust): the chain we're operating on

    Raises:
        CoTError: on failure

    """
    valid_worker_impls = get_valid_worker_impls()
    for obj in chain.get_all_links_in_chain():
        worker_impl = obj.worker_impl
        log.info("Verifying {} {} as a {} task...".format(obj.name, obj.task_id, worker_impl))
        # Run tests synchronously for now.  We can parallelize if efficiency
        # is more important than a single simple logfile.
        await valid_worker_impls[worker_impl](chain, obj)


# get_source_url {{{1
def get_source_url(obj):
    """Get the source url for a Trust object.

    Args:
        obj (ChainOfTrust or LinkOfTrust): the trust object to inspect

    Returns:
        str: the source url.

    Raises:
        CoTError: if repo and source are defined and don't match

    """
    source_env_prefix = obj.context.config['source_env_prefix']
    task = obj.task
    log.debug("Getting source url for {} {}...".format(obj.name, obj.task_id))
    repo = get_repo(obj.task, source_env_prefix=source_env_prefix)
    source = task['metadata']['source']
    # XXX We hit this for hooks - still needed? Remove when json-e cot
    # verification is required.
    # XXX .startswith() is not the ideal check here.
    # XXX this will break the new json-e cot verification. We could hardcode
    # a `{repo}/raw-file/{revision}/.taskcluster.yml` path, but that assumes
    # hg.m.o. A better approach may be to let misconfigured hooks break, and
    # either obsolete or fix them.
    if repo and not source.startswith(repo):
        log.warning("{name} {task_id}: {source_env_prefix} {repo} doesn't match source {source}... returning {repo}".format(
            name=obj.name, task_id=obj.task_id, source_env_prefix=source_env_prefix, repo=repo, source=source,
        ))
        return repo
    log.info("{} {}: found {}".format(obj.name, obj.task_id, source))
    return source


# trace_back_to_tree {{{1
async def trace_back_to_tree(chain):
    """Trace the chain back to the tree.

    task.metadata.source: "https://hg.mozilla.org/projects/date//file/a80373508881bfbff67a2a49297c328ff8052572/taskcluster/ci/build"
    task.payload.env.GECKO_HEAD_REPOSITORY "https://hg.mozilla.org/projects/date/"

    Args:
        chain (ChainOfTrust): the chain we're operating on

    Raises:
        CoTError: on error.

    """
    errors = []
    repos = {}
    restricted_privs = None
    rules = {}
    for my_key, config_key in {
        'scopes': 'cot_restricted_scopes',
        'trees': 'cot_restricted_trees'
    }.items():
        rules[my_key] = chain.context.config[config_key]

    # a repo_path of None means we have no restricted privs.
    # a string repo_path may mean we have higher privs
    for obj in [chain] + chain.links:
        source_url = get_source_url(obj)
        repo_path = match_url_regex(
            chain.context.config['valid_vcs_rules'], source_url, match_url_path_callback
        )
        repos[obj] = repo_path
    # check for restricted scopes.
    my_repo = repos[chain]
    for scope in chain.task['scopes']:
        if scope in rules['scopes']:
            log.info("Found privileged scope {}".format(scope))
            restricted_privs = True
            level = rules['scopes'][scope]
            if my_repo not in rules['trees'][level]:
                errors.append("{} {}: repo {} not allowlisted for scope {}!".format(
                    chain.name, chain.task_id, my_repo, scope
                ))
    # verify all tasks w/ same decision_task_id have the same source repo.
    if len(set(repos.values())) > 1:
        for obj, repo in repos.items():
            if obj.decision_task_id == chain.decision_task_id:
                if repo != my_repo:
                    errors.append("{} {} repo {} doesn't match my repo {}!".format(
                        obj.name, obj.task_id, repo, my_repo
                    ))
            # if we have restricted privs, the non-sibling tasks must at least be in
            # a known repo.
            # (Not currently requiring that all tasks have the same privilege level,
            #  in case a docker-image build is run on mozilla-central and that image
            #  is used for a release-priv task, for example.)
            elif restricted_privs and repo is None:
                errors.append("{} {} has no privileged repo on an restricted privilege scope!".format(
                    obj.name, obj.task_id
                ))
    # Disallow restricted privs on is_try.  This may be a redundant check.
    if restricted_privs and chain.is_try():
        errors.append("{} {} has restricted privilege scope, and is_try()!".format(chain.name, chain.task_id))
    raise_on_errors(errors)


# AuditLogFormatter {{{1
class AuditLogFormatter(logging.Formatter):
    """Format the chain of trust log."""

    def format(self, record):
        """Space debug messages for more legibility."""
        if record.levelno == logging.DEBUG:
            record.msg = ' {}'.format(record.msg)
        return super(AuditLogFormatter, self).format(record)


# verify_chain_of_trust {{{1
async def verify_chain_of_trust(chain):
    """Build and verify the chain of trust.

    Args:
        chain (ChainOfTrust): the chain we're operating on

    Raises:
        CoTError: on failure

    """
    log_path = os.path.join(chain.context.config["task_log_dir"], "chain_of_trust.log")
    with contextual_log_handler(
        chain.context, path=log_path, log_obj=log,
        formatter=AuditLogFormatter(
            fmt=chain.context.config['log_fmt'],
            datefmt=chain.context.config['log_datefmt'],
        )
    ):
        try:
            # build LinkOfTrust objects
            await build_task_dependencies(chain, chain.task, chain.name, chain.task_id)
            # download the signed chain of trust artifacts
            await download_cot(chain)
            # verify the signatures and populate the ``link.cot``s
            verify_cot_signatures(chain)
            # download all other artifacts needed to verify chain of trust
            await download_cot_artifacts(chain)
            # verify the task types, e.g. decision
            task_count = await verify_task_types(chain)
            check_num_tasks(chain, task_count)
            # verify the worker_impls, e.g. docker-worker
            await verify_worker_impls(chain)
            await trace_back_to_tree(chain)
        except (DownloadError, KeyError, AttributeError) as exc:
            log.critical("Chain of Trust verification error!", exc_info=True)
            if isinstance(exc, CoTError):
                raise
            else:
                raise CoTError(str(exc))
        log.info("Good.")


# verify_cot_cmdln {{{1
def verify_cot_cmdln(args=None):
    """Test the chain of trust from the commandline, for debugging purposes.

    Args:
        args (list, optional): the commandline args to parse.  If None, use
            ``sys.argv[1:]`` .  Defaults to None.

    """
    args = args or sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="""Verify a given task's chain of trust.

Given a task's `task_id`, get its task definition, then trace its chain of
trust back to the tree.  This doesn't verify chain of trust artifact signatures,
but does run the other tests in `scriptworker.cot.verify.verify_chain_of_trust`.

This is helpful in debugging chain of trust changes or issues.

To use, first either set your taskcluster creds in your env http://bit.ly/2eDMa6N
or in the CREDS_FILES http://bit.ly/2fVMu0A""")
    parser.add_argument('task_id', help='the task id to test')
    parser.add_argument('--task-type', help='the task type to test',
                        choices=sorted(get_valid_task_types().keys()), required=True)
    parser.add_argument('--cleanup', help='clean up the temp dir afterwards',
                        dest='cleanup', action='store_true', default=False)
    parser.add_argument('--cot-product', help='the product type to test', default='firefox')
    opts = parser.parse_args(args)
    tmp = tempfile.mkdtemp()
    log = logging.getLogger('scriptworker')
    log.setLevel(logging.DEBUG)
    logging.basicConfig()
    loop = asyncio.get_event_loop()
    conn = aiohttp.TCPConnector()
    try:
        with aiohttp.ClientSession(connector=conn) as session:
            context = Context()
            context.session = session
            context.credentials = read_worker_creds()
            context.task = loop.run_until_complete(context.queue.task(opts.task_id))
            context.config = dict(deepcopy(DEFAULT_CONFIG))
            context.config.update({
                'cot_product': opts.cot_product,
                'work_dir': os.path.join(tmp, 'work'),
                'artifact_dir': os.path.join(tmp, 'artifacts'),
                'task_log_dir': os.path.join(tmp, 'artifacts', 'public', 'logs'),
                'base_gpg_home_dir': os.path.join(tmp, 'gpg'),
                'verify_cot_signature': False,
            })
            context.config = apply_product_config(context.config)
            cot = ChainOfTrust(context, opts.task_type, task_id=opts.task_id)
            loop.run_until_complete(verify_chain_of_trust(cot))
            log.info(format_json(cot.dependent_task_ids()))
            log.info("{} : {}".format(cot.name, cot.task_id))
            for link in cot.links:
                log.info("{} : {}".format(link.name, link.task_id))
            context.session.close()
        context.queue.session.close()
        loop.close()
    finally:
        if opts.cleanup:
            rm(tmp)
        else:
            log.info("Artifacts are in {}".format(tmp))

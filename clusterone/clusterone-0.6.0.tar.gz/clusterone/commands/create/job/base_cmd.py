import re as regexp
from collections import OrderedDict

import click
from click import Choice
from click.exceptions import BadParameter

from clusterone import ClusteroneClient
from clusterone.client_exceptions import FailedCommitReference, NoProjectCommits
from clusterone.config import Config
from clusterone.utilities import random_job_name, path_to_project, time_limit_to_minutes, path_to_dataset, LazyChoice

#TODO: Refactor this AF
def get_frameworks():
    """
    :return: List of slugs representing framework versions
    """

    client = ClusteroneClient()
    frameworks = client.get_frameworks()
    framework_slugs = [k.get('slug') for k in frameworks]
    return framework_slugs

def get_instance_types():
    """
    :return: List of slugs representing framework versions
    """

    client = ClusteroneClient()
    instance_types = client.get_instance_types()
    instance_type_slugs = [k.get('slug') for k in instance_types]
    return instance_type_slugs

#TODO: Refactor this, so that request for istance types is not made twice
def get_ps_types():
    client = ClusteroneClient()
    instance_types = client.get_instance_types()
    parameter_server_type_slugs = [k['slug'] for k in instance_types if k['gpu'] == 0]
    return parameter_server_type_slugs

FRAMEWORKS = LazyChoice(get_frameworks)
WORKER_INSTANCE_TYPE = LazyChoice(get_instance_types)
PARAMETER_SERVER_INSTANCE_TYPE = LazyChoice(get_ps_types)

def validate_name(context, parameters, value):
    if not regexp.match("^[a-zA-Z0-9_-]+$", value):
        raise BadParameter("Should only contain alphanumeric characters, \"_\", or \"-\".")

    return value

def validate_time_limit(context, parameters, value):
    try:
        return time_limit_to_minutes(value)
    except ValueError:
        raise BadParameter("Please conform to [hours]h[minutes]m format, ex. \"20h12m\".")

def combine_options(*options):
    def wrapper(function):
        for option_decorator in reversed(options):
            function = option_decorator(function)
        return function
    return wrapper

base_options = combine_options(
    click.option(
        '--name',
        default=random_job_name(),
        callback=validate_name,
        help='Name of the job to be created.',
        ),
    click.option(
        '--project',
        'project_path',
        required=True,
        help="Project path to be ran, the format is: \"username/project-name\".",
        ),
    click.option(
        '--commit',
        default='latest',
        help="Hash of commit to be run, default: latest..",
        ),
    click.option(
        '--datasets',
        help="Comma separated list of the datasets to use for the job. e.g. 'clusterone/mnist-training:[GIT COMMIT HASH],clusterone/mnist-val:[GIT COMMIT HASH]'",
        default="",
        ),
    click.option(
        '--module',
        default='main',
        help='Module to run, eg. main.',
        ),
    click.option(
        '--package-path',
        # The project root is represented by API as None
        # TODO: Test if this works
        help='Path to module, default is the project root.',
        ),
    click.option(
        '--python-version',
        type=Choice(['2', '2.7', '3', '3.5']),
        default='2.7',
        help='Python version to use',
        ),
    click.option(
        '--framework',
        type=FRAMEWORKS,
        default="tensorflow-1.3.0",
        help='Framework to be used. Default: tensorflow',
        ),
    #TODO: test passing
    #TODO: test default
    click.option(
        '--package-manager',
        type=Choice(['pip','conda','anaconda']),
        default="pip",
        help='Package manager to use.',
        ),
    click.option(
        '--requirements',
        help="The requirements file to use.",
        ),
    #TODO: Create custom click type time
    # https://github.com/click-contrib/click-datetime ?
    click.option(
        '--time-limit',
        default="48h",
        callback=validate_time_limit,
        help="Time limit for the job in the following format [hours]h[minutes]m, eg. \"22h30m\"."
        ),
    click.option(
        '--description',
        default="",
        help='Job description [optional].'
        )
    )

def base(context, kwargs):

    #config, client = context.config, context.client

    project = path_to_project(kwargs['project_path'], context=context)
    project_id = project['id']

    commit = kwargs['commit']
    commit_ids = [_commit['id'] for _commit in project['commits']]
    if commit == "latest":
        try:
            commit = commit_ids[0]
        except IndexError as exception:
            raise NoProjectCommits()
    elif commit not in commit_ids:
        raise FailedCommitReference()
    commit_to_use = commit

    #TODO: Refactor this like hell!
    #TODO: OMG TEST THIS
    #TODO: OMG MOCK THIS IN OTHER TESTS
    datasets_list = []

    try:
        for raw_dataset_string in kwargs['datasets'].split(','):
            dataset_path, dataset_commit = raw_dataset_string.split(':')
            dataset = path_to_dataset(dataset_path, context=context)
            datasets_list.append(OrderedDict({'dataset': dataset['id'], 'git_commit_hash': dataset_commit}))
    except ValueError as exception:
        pass

    # Caution, this isn't sustainable behavior if we add more Python versions!!!
    python_version = '2.7' if kwargs['python_version'] in ['2.7','2'] else '3.5'

    framework_slug = kwargs['framework']

    package_manager = kwargs['package_manager']
    package_manager = 'conda' if package_manager == 'anaconda' else package_manager

    requirements = kwargs['requirements']
    default_requirements = "requirements.{}".format("txt" if package_manager == 'pip' else "yml")
    requirements = default_requirements if not requirements else requirements

    return {
        'parameters':
        {
            "module": kwargs['module'],
            "package_path": kwargs['package_path'],
            "package_manager": package_manager,
            "requirements": requirements,
            "time_limit": kwargs['time_limit'],
            "datasets_set": datasets_list,
            "code": project_id,
            "code_commit": commit_to_use,
            "framework":{
                "slug": framework_slug
            },
            "python_version": python_version,
        },
        'meta':
        {
            "name": kwargs['name'],
            "description": kwargs['description'],
        }
    }


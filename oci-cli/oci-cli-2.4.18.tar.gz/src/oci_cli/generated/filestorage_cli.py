# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from ..cli_root import cli
from .. import cli_util
from .. import json_skeleton_utils
from .. import retry_utils  # noqa: F401
from .. import custom_types  # noqa: F401
from ..aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('file_storage_group.command_name', 'file_storage'), cls=CommandGroupWithAlias, help=cli_util.override('file_storage_group.help', """The API for the File Storage Service.

You can use the table of contents or the version selector and search tool to explore the File Storage Service API.
"""))
@cli_util.help_option_group
def file_storage_group():
    pass


@click.command(cli_util.override('file_system_group.command_name', 'file-system'), cls=CommandGroupWithAlias, help="""An NFS file system. To allow access to a file system, add it to an export set and associate the export set with a mount target. The same file system can be in multiple export sets and associated with multiple mount targets.

To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see [Getting Started with Policies].""")
@cli_util.help_option_group
def file_system_group():
    pass


@click.command(cli_util.override('export_set_group.command_name', 'export-set'), cls=CommandGroupWithAlias, help="""A set of file systems to export through one or more mount targets. Composed of zero or more export resources.""")
@cli_util.help_option_group
def export_set_group():
    pass


@click.command(cli_util.override('mount_target_group.command_name', 'mount-target'), cls=CommandGroupWithAlias, help="""Provides access to a collection of file systems through one or more VNICs on a specified subnet. The set of file systems is controlled through the referenced export set.""")
@cli_util.help_option_group
def mount_target_group():
    pass


@click.command(cli_util.override('export_group.command_name', 'export'), cls=CommandGroupWithAlias, help="""A file system and the path that you can use to mount it. Each export resource belongs to exactly one export set.

The export's path attribute is not a path in the referenced file system, but the value used by clients for the path component of the remotetarget argument when mounting the file system.

The path must start with a slash (/) followed by a sequence of zero or more slash-separated path elements. For any two export resources associated with the same export set, except those in a 'DELETED' state, the path element sequence for the first export resource can't contain the complete path element sequence of the second export resource.

For example, the following are acceptable:

  * /foo and /bar   * /foo1 and /foo2   * /foo and /foo1

The following examples are not acceptable:   * /foo and /foo/bar   * / and /foo

Paths may not end in a slash (/). No path element can be a period (.) or two periods in sequence (..). All path elements must be 255 bytes or less.

No two non-'DELETED' export resources in the same export set can reference the same file system.""")
@cli_util.help_option_group
def export_group():
    pass


@click.command(cli_util.override('snapshot_group.command_name', 'snapshot'), cls=CommandGroupWithAlias, help="""A point-in-time snapshot of a specified file system.""")
@cli_util.help_option_group
def snapshot_group():
    pass


@export_group.command(name=cli_util.override('create_export.command_name', 'create'), help="""Creates a new export in the specified export set, path, and file system.""")
@click.option('--export-set-id', callback=cli_util.handle_required_param, help="""The OCID of this export's export set. [required]""")
@click.option('--file-system-id', callback=cli_util.handle_required_param, help="""The OCID of this export's file system. [required]""")
@click.option('--path', callback=cli_util.handle_required_param, help="""Path used to access the associated file system.

Avoid entering confidential information.

Example: `/mediafiles` [required]""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'Export'})
@cli_util.wrap_exceptions
def create_export(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, export_set_id, file_system_id, path):
    kwargs = {}

    details = {}
    details['exportSetId'] = export_set_id
    details['fileSystemId'] = file_system_id
    details['path'] = path

    client = cli_util.build_client('file_storage', ctx)
    result = client.create_export(
        create_export_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_export') and callable(getattr(client, 'get_export')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_export, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('create_file_system.command_name', 'create'), help="""Creates a new file system in the specified compartment and availability domain. Instances can mount file systems in another availability domain, but doing so might increase latency when compared to mounting instances in the same availability domain.

After you create a file system, you can associate it with a mount target. Instances can then mount the file system by connecting to the mount target's IP address. You can associate a file system with more than one mount target at a time.

For information about access control and compartments, see [Overview of the IAM Service].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure resources, including file systems, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID).  When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type or by viewing the resource in the Console.""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The availability domain to create the file system in.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment to create the file system in. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My file system`""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'FileSystem'})
@cli_util.wrap_exceptions
def create_file_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, display_name):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('file_storage', ctx)
    result = client.create_file_system(
        create_file_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_file_system') and callable(getattr(client, 'get_file_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_file_system, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('create_mount_target.command_name', 'create'), help="""Creates a new mount target in the specified compartment and subnet. You can associate a file system with a mount target only when they exist in the same availability domain. Instances can connect to mount targets in another availablity domain, but you might see higher latency than with instances in the same availability domain as the mount target.

Mount targets have one or more private IP addresses that you can provide as the host portion of remote target parameters in client mount commands. These private IP addresses are listed in the privateIpIds property of the mount target and are highly available. Mount targets also consume additional IP addresses in their subnet.

For information about access control and compartments, see [Overview of the IAM Service].

For information about availability domains, see [Regions and Availability Domains]. To get a list of availability domains, use the `ListAvailabilityDomains` operation in the Identity and Access Management Service API.

All Oracle Cloud Infrastructure Services resources, including mount targets, get an Oracle-assigned, unique ID called an Oracle Cloud Identifier (OCID).  When you create a resource, you can find its OCID in the response. You can also retrieve a resource's OCID by using a List API operation on that resource type, or by viewing the resource in the Console.""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The availability domain in which to create the mount target.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment in which to create the mount target. [required]""")
@click.option('--subnet-id', callback=cli_util.handle_required_param, help="""The OCID of the subnet in which to create the mount target. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My mount target`""")
@click.option('--hostname-label', callback=cli_util.handle_optional_param, help="""The hostname for the mount target's IP address, used for DNS resolution. The value is the hostname portion of the private IP address's fully qualified domain name (FQDN). For example, `files-1` in the FQDN `files-1.subnet123.vcn1.oraclevcn.com`. Must be unique across all VNICs in the subnet and comply with [RFC 952] and [RFC 1123].

For more information, see [DNS in Your Virtual Cloud Network].

Example: `files-1`""")
@click.option('--ip-address', callback=cli_util.handle_optional_param, help="""A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.

Example: `10.0.3.3`""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'MountTarget'})
@cli_util.wrap_exceptions
def create_mount_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, availability_domain, compartment_id, subnet_id, display_name, hostname_label, ip_address):
    kwargs = {}

    details = {}
    details['availabilityDomain'] = availability_domain
    details['compartmentId'] = compartment_id
    details['subnetId'] = subnet_id

    if display_name is not None:
        details['displayName'] = display_name

    if hostname_label is not None:
        details['hostnameLabel'] = hostname_label

    if ip_address is not None:
        details['ipAddress'] = ip_address

    client = cli_util.build_client('file_storage', ctx)
    result = client.create_mount_target(
        create_mount_target_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_mount_target') and callable(getattr(client, 'get_mount_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_mount_target, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@snapshot_group.command(name=cli_util.override('create_snapshot.command_name', 'create'), help="""Creates a new snapshot of the specified file system. You can access the snapshot at `.snapshot/<name>`.""")
@click.option('--file-system-id', callback=cli_util.handle_required_param, help="""The OCID of this export's file system. [required]""")
@click.option('--name', callback=cli_util.handle_required_param, help="""Name of the snapshot. This value is immutable. It must also be unique with respect to all other non-DELETED snapshots on the associated file system.

Avoid entering confidential information.

Example: `Sunday` [required]""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'Snapshot'})
@cli_util.wrap_exceptions
def create_snapshot(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, file_system_id, name):
    kwargs = {}

    details = {}
    details['fileSystemId'] = file_system_id
    details['name'] = name

    client = cli_util.build_client('file_storage', ctx)
    result = client.create_snapshot(
        create_snapshot_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_snapshot') and callable(getattr(client, 'get_snapshot')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_snapshot, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@export_group.command(name=cli_util.override('delete_export.command_name', 'delete'), help="""Deletes the specified export.""")
@click.option('--export-id', callback=cli_util.handle_required_param, help="""The OCID of the export. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_export(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, export_id, if_match):

    if isinstance(export_id, six.string_types) and len(export_id.strip()) == 0:
        raise click.UsageError('Parameter --export-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('file_storage', ctx)
    result = client.delete_export(
        export_id=export_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_export') and callable(getattr(client, 'get_export')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_export, export_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('delete_file_system.command_name', 'delete'), help="""Deletes the specified file system. Before you delete the file system, verify that no remaining export resources still reference it. Deleting a file system also deletes all of its snapshots.""")
@click.option('--file-system-id', callback=cli_util.handle_required_param, help="""The OCID of the file system. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_file_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, file_system_id, if_match):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('file_storage', ctx)
    result = client.delete_file_system(
        file_system_id=file_system_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_file_system') and callable(getattr(client, 'get_file_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_file_system, file_system_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('delete_mount_target.command_name', 'delete'), help="""Deletes the specified mount target. This operation also deletes the mount target's VNICs.""")
@click.option('--mount-target-id', callback=cli_util.handle_required_param, help="""The OCID of the mount target. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_mount_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, mount_target_id, if_match):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('file_storage', ctx)
    result = client.delete_mount_target(
        mount_target_id=mount_target_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_mount_target') and callable(getattr(client, 'get_mount_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_mount_target, mount_target_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@snapshot_group.command(name=cli_util.override('delete_snapshot.command_name', 'delete'), help="""Deletes the specified snapshot.""")
@click.option('--snapshot-id', callback=cli_util.handle_required_param, help="""The OCID of the snapshot. [required]""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_snapshot(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, snapshot_id, if_match):

    if isinstance(snapshot_id, six.string_types) and len(snapshot_id.strip()) == 0:
        raise click.UsageError('Parameter --snapshot-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    client = cli_util.build_client('file_storage', ctx)
    result = client.delete_snapshot(
        snapshot_id=snapshot_id,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_snapshot') and callable(getattr(client, 'get_snapshot')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_snapshot, snapshot_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@export_group.command(name=cli_util.override('get_export.command_name', 'get'), help="""Gets the specified export's information.""")
@click.option('--export-id', callback=cli_util.handle_required_param, help="""The OCID of the export. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'Export'})
@cli_util.wrap_exceptions
def get_export(ctx, from_json, export_id):

    if isinstance(export_id, six.string_types) and len(export_id.strip()) == 0:
        raise click.UsageError('Parameter --export-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('file_storage', ctx)
    result = client.get_export(
        export_id=export_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@export_set_group.command(name=cli_util.override('get_export_set.command_name', 'get'), help="""Gets the specified export set's information.""")
@click.option('--export-set-id', callback=cli_util.handle_required_param, help="""The OCID of the export set. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'ExportSet'})
@cli_util.wrap_exceptions
def get_export_set(ctx, from_json, export_set_id):

    if isinstance(export_set_id, six.string_types) and len(export_set_id.strip()) == 0:
        raise click.UsageError('Parameter --export-set-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('file_storage', ctx)
    result = client.get_export_set(
        export_set_id=export_set_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('get_file_system.command_name', 'get'), help="""Gets the specified file system's information.""")
@click.option('--file-system-id', callback=cli_util.handle_required_param, help="""The OCID of the file system. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'FileSystem'})
@cli_util.wrap_exceptions
def get_file_system(ctx, from_json, file_system_id):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('file_storage', ctx)
    result = client.get_file_system(
        file_system_id=file_system_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('get_mount_target.command_name', 'get'), help="""Gets the specified mount target's information.""")
@click.option('--mount-target-id', callback=cli_util.handle_required_param, help="""The OCID of the mount target. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'MountTarget'})
@cli_util.wrap_exceptions
def get_mount_target(ctx, from_json, mount_target_id):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('file_storage', ctx)
    result = client.get_mount_target(
        mount_target_id=mount_target_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@snapshot_group.command(name=cli_util.override('get_snapshot.command_name', 'get'), help="""Gets the specified snapshot's information.""")
@click.option('--snapshot-id', callback=cli_util.handle_required_param, help="""The OCID of the snapshot. [required]""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'Snapshot'})
@cli_util.wrap_exceptions
def get_snapshot(ctx, from_json, snapshot_id):

    if isinstance(snapshot_id, six.string_types) and len(snapshot_id.strip()) == 0:
        raise click.UsageError('Parameter --snapshot-id cannot be whitespace or empty string')
    kwargs = {}
    client = cli_util.build_client('file_storage', ctx)
    result = client.get_snapshot(
        snapshot_id=snapshot_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@export_set_group.command(name=cli_util.override('list_export_sets.command_name', 'list'), help="""Lists the export set resources in the specified compartment.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable.

Example: `My resource`""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@click.option('--id', callback=cli_util.handle_optional_param, help="""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[ExportSetSummary]'})
@cli_util.wrap_exceptions
def list_export_sets(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_export_sets,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_export_sets,
            limit,
            page_size,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    else:
        result = client.list_export_sets(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@export_group.command(name=cli_util.override('list_exports.command_name', 'list'), help="""Lists the export resources in the specified compartment. You must also specify an export set, a file system, or both.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--export-set-id', callback=cli_util.handle_optional_param, help="""The OCID of the export set.""")
@click.option('--file-system-id', callback=cli_util.handle_optional_param, help="""The OCID of the file system.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@click.option('--id', callback=cli_util.handle_optional_param, help="""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "PATH"]), help="""The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by path, results are shown in ascending alphanumeric order.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[ExportSummary]'})
@cli_util.wrap_exceptions
def list_exports(ctx, from_json, all_pages, page_size, compartment_id, limit, page, export_set_id, file_system_id, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if export_set_id is not None:
        kwargs['export_set_id'] = export_set_id
    if file_system_id is not None:
        kwargs['file_system_id'] = file_system_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_exports,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_exports,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_exports(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('list_file_systems.command_name', 'list'), help="""Lists the file system resources in the specified compartment.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable.

Example: `My resource`""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@click.option('--id', callback=cli_util.handle_optional_param, help="""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can provide either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[FileSystemSummary]'})
@cli_util.wrap_exceptions
def list_file_systems(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_file_systems,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_file_systems,
            limit,
            page_size,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    else:
        result = client.list_file_systems(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('list_mount_targets.command_name', 'list'), help="""Lists the mount target resources in the specified compartment.""")
@click.option('--compartment-id', callback=cli_util.handle_required_param, help="""The OCID of the compartment. [required]""")
@click.option('--availability-domain', callback=cli_util.handle_required_param, help="""The name of the availability domain.

Example: `Uocm:PHX-AD-1` [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable.

Example: `My resource`""")
@click.option('--export-set-id', callback=cli_util.handle_optional_param, help="""The OCID of the export set.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@click.option('--id', callback=cli_util.handle_optional_param, help="""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@click.option('--sort-by', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help="""The field to sort by. You can choose either value, but not both. By default, when you sort by time created, results are shown in descending order. When you sort by display name, results are shown in ascending order.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[MountTargetSummary]'})
@cli_util.wrap_exceptions
def list_mount_targets(ctx, from_json, all_pages, page_size, compartment_id, availability_domain, limit, page, display_name, export_set_id, lifecycle_state, id, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    if sort_by and not availability_domain and not all_pages:
        raise click.UsageError('You must provide an --availability-domain when doing a --sort-by, unless you specify the --all parameter')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if display_name is not None:
        kwargs['display_name'] = display_name
    if export_set_id is not None:
        kwargs['export_set_id'] = export_set_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_mount_targets,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_mount_targets,
            limit,
            page_size,
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    else:
        result = client.list_mount_targets(
            compartment_id=compartment_id,
            availability_domain=availability_domain,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@snapshot_group.command(name=cli_util.override('list_snapshots.command_name', 'list'), help="""Lists snapshots of the specified file system.""")
@click.option('--file-system-id', callback=cli_util.handle_required_param, help="""The OCID of the file system. [required]""")
@click.option('--limit', callback=cli_util.handle_optional_param, type=click.INT, help="""The maximum number of items to return in a paginated \"List\" call.

Example: `500`""")
@click.option('--page', callback=cli_util.handle_optional_param, help="""The value of the `opc-next-page` response header from the previous \"List\" call.""")
@click.option('--lifecycle-state', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help="""Filter results by the specified lifecycle state. Must be a valid state for the resource type.""")
@click.option('--id', callback=cli_util.handle_optional_param, help="""Filter results by OCID. Must be an OCID of the correct type for the resouce type.""")
@click.option('--sort-order', callback=cli_util.handle_optional_param, type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help="""The sort order to use, either 'asc' or 'desc', where 'asc' is ascending and 'desc' is descending.""")
@click.option('--all', 'all_pages', is_flag=True, callback=cli_util.handle_optional_param, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@click.option('--page-size', type=click.INT, callback=cli_util.handle_optional_param, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'list[SnapshotSummary]'})
@cli_util.wrap_exceptions
def list_snapshots(ctx, from_json, all_pages, page_size, file_system_id, limit, page, lifecycle_state, id, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')
    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if id is not None:
        kwargs['id'] = id
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    client = cli_util.build_client('file_storage', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = retry_utils.list_call_get_all_results_with_default_retries(
            client.list_snapshots,
            file_system_id=file_system_id,
            **kwargs
        )
    elif limit is not None:
        result = retry_utils.list_call_get_up_to_limit_with_default_retries(
            client.list_snapshots,
            limit,
            page_size,
            file_system_id=file_system_id,
            **kwargs
        )
    else:
        result = client.list_snapshots(
            file_system_id=file_system_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@export_set_group.command(name=cli_util.override('update_export_set.command_name', 'update'), help="""Updates the specified export set's information.""")
@click.option('--export-set-id', callback=cli_util.handle_required_param, help="""The OCID of the export set. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My export set`""")
@click.option('--max-fs-stat-bytes', callback=cli_util.handle_optional_param, type=click.INT, help="""Controls the maximum `tbytes`, `fbytes`, and `abytes` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tbytes` value reported by `FSSTAT` will be `maxFsStatBytes`. The value of `fbytes` and `abytes` will be `maxFsStatBytes` minus the metered size of the file system. If the metered size is larger than `maxFsStatBytes`, then `fbytes` and `abytes` will both be '0'.""")
@click.option('--max-fs-stat-files', callback=cli_util.handle_optional_param, type=click.INT, help="""Controls the maximum `ffiles`, `ffiles`, and `afiles` values reported by `NFS FSSTAT` calls through any associated mount targets. This is an advanced feature. For most applications, use the default value. The `tfiles` value reported by `FSSTAT` will be `maxFsStatFiles`. The value of `ffiles` and `afiles` will be `maxFsStatFiles` minus the metered size of the file system. If the metered size is larger than `maxFsStatFiles`, then `ffiles` and `afiles` will both be '0'.""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'ExportSet'})
@cli_util.wrap_exceptions
def update_export_set(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, export_set_id, display_name, max_fs_stat_bytes, max_fs_stat_files, if_match):

    if isinstance(export_set_id, six.string_types) and len(export_set_id.strip()) == 0:
        raise click.UsageError('Parameter --export-set-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    if max_fs_stat_bytes is not None:
        details['maxFsStatBytes'] = max_fs_stat_bytes

    if max_fs_stat_files is not None:
        details['maxFsStatFiles'] = max_fs_stat_files

    client = cli_util.build_client('file_storage', ctx)
    result = client.update_export_set(
        export_set_id=export_set_id,
        update_export_set_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_export_set') and callable(getattr(client, 'get_export_set')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_export_set, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@file_system_group.command(name=cli_util.override('update_file_system.command_name', 'update'), help="""Updates the specified file system's information. You can use this operation to rename a file system.""")
@click.option('--file-system-id', callback=cli_util.handle_required_param, help="""The OCID of the file system. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. It does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My file system`""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'FileSystem'})
@cli_util.wrap_exceptions
def update_file_system(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, file_system_id, display_name, if_match):

    if isinstance(file_system_id, six.string_types) and len(file_system_id.strip()) == 0:
        raise click.UsageError('Parameter --file-system-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('file_storage', ctx)
    result = client.update_file_system(
        file_system_id=file_system_id,
        update_file_system_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_file_system') and callable(getattr(client, 'get_file_system')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_file_system, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@mount_target_group.command(name=cli_util.override('update_mount_target.command_name', 'update'), help="""Updates the specified mount target's information.""")
@click.option('--mount-target-id', callback=cli_util.handle_required_param, help="""The OCID of the mount target. [required]""")
@click.option('--display-name', callback=cli_util.handle_optional_param, help="""A user-friendly name. Does not have to be unique, and it is changeable. Avoid entering confidential information.

Example: `My mount target`""")
@click.option('--if-match', callback=cli_util.handle_optional_param, help="""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@click.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), callback=cli_util.handle_optional_param, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state.""")
@click.option('--max-wait-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@click.option('--wait-interval-seconds', type=click.INT, callback=cli_util.handle_optional_param, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'file_storage', 'class': 'MountTarget'})
@cli_util.wrap_exceptions
def update_mount_target(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, mount_target_id, display_name, if_match):

    if isinstance(mount_target_id, six.string_types) and len(mount_target_id.strip()) == 0:
        raise click.UsageError('Parameter --mount-target-id cannot be whitespace or empty string')
    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match

    details = {}

    if display_name is not None:
        details['displayName'] = display_name

    client = cli_util.build_client('file_storage', ctx)
    result = client.update_mount_target(
        mount_target_id=mount_target_id,
        update_mount_target_details=details,
        **kwargs
    )
    if wait_for_state:
        if hasattr(client, 'get_mount_target') and callable(getattr(client, 'get_mount_target')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, retry_utils.call_funtion_with_default_retries(client.get_mount_target, result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except Exception as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)

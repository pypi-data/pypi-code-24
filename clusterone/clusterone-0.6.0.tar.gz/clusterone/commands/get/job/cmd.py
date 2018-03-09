import click

from clusterone import authenticate
from clusterone.utilities import path_to_job_id, make_table, serialize_job


HEADER = ['Property', 'Value']

HEADER_BASE = [
    'Name',
    'Status',
    'Project',
    'Module',
    'Package-path',
    'Datasets',
    'Python version',
    'Package manager',
    'Requirements',
    'Framework',
    'Framework version',
    'Mode',
    'Instance type',
    'Worker type',
    'Worker replicas',
    'Ps type',
    'Ps replicas',
    'Time limit',
    ]

#TODO: Test this thoughrilly in the future -> [], [dataset], [dataset] * 3
def displayable_data(datasets_list):
    return "".join(["{}:{}\n".format(dataset['mount_point'], dataset['hash']) for dataset in datasets_list])

def extract_data_from_job(job):

    mode = job['parameters']['mode']

    extracted_data = [
        job['display_name'],
        job['status'],
        job['repository_name'],
        job['parameters']['module'],
        job['parameters']['package_path'],
        displayable_data(job['parameters']['data_repos']),
        job['parameters']['python_version'],
        job['parameters']['package_manager'],
        job['parameters']['requirements'],
        job['parameters']['framework'],
        job['parameters']['tf_version'],
        mode,
        job['parameters']['instance_type'],
        job['parameters']['worker_type'],
        job['parameters']['worker_replicas'],
        job['parameters']['ps_type'],
        job['parameters']['ps_replicas'],
        "{} minutes".format(job['parameters']['time_limit']),
    ]

    key_value_pairs = zip(HEADER_BASE, extracted_data)

    return list(filter(lambda pair: not pair[0] in
                       (["Worker type", "Ps type", "Worker replicas", "Ps replicas"]
                        if mode in ["single", "single-node-tf"]
                        else ["Instance type"]),
                       key_value_pairs))

@click.command()
@click.pass_obj
@authenticate()
@click.argument(
    'job-path-or-id',
    )
def command(context, job_path_or_id):
    """
    Get information about a job
    """

    job = serialize_job(job_path_or_id, context=context)

    click.echo(make_table(extract_data_from_job(job), header=HEADER))

    return job

import json
import logging
import os
import socket
import sys
from pathlib import Path

import aiodns

from .utils import curl

__all__ = (
    'detect_cloud',
    'current_provider',
    'get_instance_id',
    'get_instance_ip',
    'get_instance_type',
    'get_instance_region',
)

log = logging.getLogger(__name__)


def is_containerized() -> bool:
    '''
    Check if I am running inside a Linux container.
    '''
    try:
        cginfo = Path('/proc/self/cgroup').read_text()
        if '/docker/' in cginfo or '/lxc/' in cginfo:
            return True
    except IOError:
        return False


def detect_cloud() -> str:
    '''
    Detect the cloud provider where I am running on.
    '''
    if sys.platform.startswith('linux'):
        # Google Cloud Platform or Amazon AWS (hvm)
        try:
            bios = Path('/sys/devices/virtual/dmi/id/bios_version').read_text().lower()
            if 'google' in bios:
                return 'google'
            if 'amazon' in bios:
                return 'amazon'
        except IOError:
            pass
        # Microsoft Azure
        # https://gallery.technet.microsoft.com/scriptcenter/Detect-Windows-Azure-aed06d51
        # TODO: this only works with Debian/Ubuntu instances.
        # TODO: this does not work inside containers.
        try:
            dhcp = Path('/var/lib/dhcp/dhclient.eth0.leases').read_text()
            if 'unknown-245' in dhcp:
                return 'azure'
            # alternative method is to read /var/lib/waagent/GoalState.1.xml
            # but it requires sudo privilege.
        except IOError:
            pass
    else:
        log.warning('Cloud detection is implemented for Linux only yet.')
    return 'unknown'


# Detect upon module load.
current_provider = detect_cloud()
log.info(f'cloud provider detected: {current_provider}')

_defined = False
get_instance_id = None
get_instance_ip = None
get_instance_type = None
get_instance_region = None


def _define_functions():
    global _defined
    global get_instance_id
    global get_instance_ip
    global get_instance_type
    global get_instance_region
    if _defined:
        return

    if current_provider == 'amazon':
        # ref: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
        _metadata_prefix = 'http://169.254.169.254/latest/meta-data/'
        _dynamic_prefix = 'http://169.254.169.254/latest/dynamic/'

        async def _get_instance_id():
            return await curl(_metadata_prefix + 'instance-id',
                              lambda: f'i-{socket.gethostname()}')

        async def _get_instance_ip():
            return await curl(_metadata_prefix + 'local-ipv4',
                              '127.0.0.1')

        async def _get_instance_type():
            return await curl(_metadata_prefix + 'instance-type',
                              'unknown')

        async def _get_instance_region():
            doc = await curl(_dynamic_prefix + 'instance-identity/document')
            if doc is None:
                return 'amazon/unknown'
            region = json.loads(doc)['region']
            return f'amazon/{region}'

    elif current_provider == 'azure':
        # ref: https://docs.microsoft.com/azure/virtual-machines/virtual-machines-instancemetadataservice-overview
        _metadata_prefix = 'http://169.254.169.254/metadata/instance'

        async def _get_instance_id():
            data = await curl(_metadata_prefix, None,
                              params={'version': '2017-03-01'},
                              headers={'Metadata': 'true'})
            if data is None:
                return f'i-{socket.gethostname()}'
            o = json.loads(data)
            return o['compute']['vmId']

        async def _get_instance_ip():
            data = await curl(_metadata_prefix, None,
                              params={'version': '2017-03-01'},
                              headers={'Metadata': 'true'})
            if data is None:
                return '127.0.0.1'
            o = json.loads(data)
            return o['network']['interface'][0]['ipv4']['ipaddress'][0]['ipaddress']

        async def _get_instance_type():
            data = await curl(_metadata_prefix, None,
                              params={'version': '2017-03-01'},
                              headers={'Metadata': 'true'})
            if data is None:
                return 'unknown'
            o = json.loads(data)
            return o['compute']['vmSize']

        async def _get_instance_region():
            data = await curl(_metadata_prefix, None,
                              params={'version': '2017-03-01'},
                              headers={'Metadata': 'true'})
            if data is None:
                return 'azure/unknown'
            o = json.loads(data)
            region = o['compute']['location']
            return f'azure/{region}'

    elif current_provider == 'google':
        # ref: https://cloud.google.com/compute/docs/storing-retrieving-metadata
        _metadata_prefix = 'http://metadata.google.internal/computeMetadata/v1/'

        async def _get_instance_id():
            return await curl(_metadata_prefix + 'instance/id',
                              lambda: f'i-{socket.gethostname()}',
                              headers={'Metadata-Flavor': 'Google'})

        async def _get_instance_ip():
            return await curl(_metadata_prefix + 'instance/network-interfaces/0/ip',
                              '127.0.0.1',
                              headers={'Metadata-Flavor': 'Google'})

        async def _get_instance_type():
            return await curl(_metadata_prefix + 'instance/machine-type',
                              'unknown',
                              headers={'Metadata-Flavor': 'Google'})

        async def _get_instance_region():
            zone = await curl(_metadata_prefix + 'instance/zone',
                              'unknown',
                              headers={'Metadata-Flavor': 'Google'})
            region = zone.rsplit('-', 1)[0]
            return f'google/{region}'

    else:
        _metadata_prefix = None

        async def _get_instance_id():
            return f'i-{socket.gethostname()}'

        async def _get_instance_ip():
            try:
                myself = socket.gethostname()
                resolver = aiodns.DNSResolver()
                result = await resolver.gethostbyname(myself, socket.AF_INET)
                return result.addresses[0]
            except aiodns.error.DNSError:
                return '127.0.0.1'

        async def _get_instance_type():
            return 'unknown'

        async def _get_instance_region():
            return os.environ.get('BACKEND_REGION', 'local/unknown')

    get_instance_id = _get_instance_id
    get_instance_ip = _get_instance_ip
    get_instance_type = _get_instance_type
    get_instance_region = _get_instance_region
    _defined = True


_define_functions()

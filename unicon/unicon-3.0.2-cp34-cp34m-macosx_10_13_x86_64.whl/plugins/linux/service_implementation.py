import re
import ipaddress

from unicon.bases.linux.services import BaseService
from unicon.core.errors import SubCommandFailure
from unicon.eal.dialogs import Dialog, Statement
from unicon.plugins.linux.patterns import LinuxPatterns
from unicon.plugins.linux.utils import LinuxUtils
from unicon.utils import AttributeDict
from unicon import log

utils = LinuxUtils()


class Execute(BaseService):
    def __init__(self, connection, context, **kwargs):
        self.connection = connection
        self.context = context
        self.timeout_pattern = ['Timeout occurred', ]
        self.error_pattern = []
        self.start_state = 'None'
        self.end_state = 'None'
        self.result = None
        # add the keyword arguments to the object
        self.__dict__.update(kwargs)

    def call_service(self, command,
                     reply=Dialog([]),
                     timeout=None,
                     *args, **kwargs):

        con = self.connection
        con.log.debug("+++ execute %s +++" % command)
        timeout = timeout or con.settings.EXEC_TIMEOUT
        if not isinstance(reply, Dialog):
            raise SubCommandFailure(
                "dialog passed via 'reply' must be an instance of Dialog")
        p = LinuxPatterns()
        dialog = Dialog()
        if reply:
            dialog += reply
        dialog.append(Statement(pattern=con.state_machine.get_state(con.state_machine.current_state).pattern))
        con.sendline(command)
        try:
            self.result = dialog.process(con.spawn, timeout=timeout,
                prompt_recovery=self.prompt_recovery)
        except Exception as err:
            raise SubCommandFailure("Command execution failed", err)
        # Remove command and hostname from output.
        if self.result:
            output = utils.truncate_trailing_prompt(
                        con.state_machine.get_state(con.state_machine.current_state).pattern,
                        self.result.match_output,
                        self.connection.hostname)
            output = re.sub(re.escape(command), "", output, 1)
            self.result = output.strip()


class Ping(BaseService):
    """ Service to issue ping response request to another network from device.

    Returns:
        ping command response, raises SubCommandFailure if 0% packet loss is not seen

    Example:
        .. code-block:: python

            ping("10.1.1.1")
            ping("10.2.1.1", count=10)

    Syntax:
        .. code-block:: python

            ping(destination, options="LRUbfnqrvA", arg=value)

    """

    _ping_option_long_to_short = {
        'count': 'c',
        'interval': 'i',
        'deadline': 'w',
        'timeout': 'w',
        'pattern': 'p',
        'size': 's',
        'ttl': 't',
        'interface': 'I',
        'sndbuf': 'S',
        'timestamp': 'T',
        'tos': 'Q'
    }

    # Ping Options
    ping_boolean_options = {
                    # 'a': 'Audible ping'
                    'A': 'Adaptive ping. Interpacket interval adapts to round-trip time',
                    'b': 'Allow pinging a broadcast address.',
                    # 'd': 'Set the SO_DEBUG option on the socket being used.'
                    #      ' Essentially, this socket option is not used by Linux kernel.',
                    'f': 'Flood ping.',
                    'L': 'Suppress loopback of multicast packets.'
                         ' This flag only applies if the ping destination is a multicast address.',
                    'n': 'Numeric output only. No attempt will be made to lookup'
                         ' symbolic names for host addresses.',
                    'q': 'Quiet output. Nothing is displayed except the summary lines at startup time and when finished.',
                    'r': 'Bypass the normal routing tables and send directly to a host on an attached interface.',
                    'R': 'Record route.',
                    'S': 'Set socket sndbuf. If not specified, it is selected to buffer not more than one packet.',
                    'U': 'Print full user-to-user latency',
                    'v': 'Verbose output.',
                    # 'V': 'show version',
                    }

    ping_arg_options = {
                    'c': 'Number of packets to send',
                    'i': 'Wait interval seconds between sending each packet.',
                    'I': 'Set source address to specified interface address. '
                         'Argument may be numeric IP address or name of device.',
                    'p': 'You may specify up to 16 ''pad'' bytes to '
                         'fill out the packet you send.',
                    's': 'Specifies the number of data bytes to be sent.',
                    'Q': 'Set Quality of Service -related bits in ICMP datagrams. '
                         'tos can be either decimal or hex number. ',
                    't': 'Set the IP Time to Live.',
                    'T': 'Set special IP timestamp options. timestamp option may be either\n'
                    '            tsonly (only timestamps), tsandaddr (timestamps and addresses) or\n'
                    '            tsprespec host1 [host2 [host3 [host4]]] (timestamp prespecified hops).',
                    'w': 'Specify a timeout, in seconds',
                    }

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.start_state = 'shell'
        self.end_state = 'shell'
        self.service_name = 'ping'
        self.timeout = 60
        # Ping error Patterns
        self.default_error_pattern = ['[123456789]+0*% packet loss']

        self.__dict__.update(kwargs)

        ping_option_short_to_long = {v:k for (k,v) in self._ping_option_long_to_short.items()}

        self.__doc__ = self.__doc__ + "Boolean options\n{}\n\n    Argument options\n{}".format(
            "\n".join(["{:>10}: {}".format(k,self.ping_boolean_options[k]) \
                 for k in sorted(self.ping_boolean_options.keys(), key=lambda k: k.lower())]),
            "\n".join(["{:>10}: {}".format(ping_option_short_to_long[k],self.ping_arg_options[k]) \
                 for k in sorted(self.ping_arg_options.keys(), key=lambda k: k.lower())]),
            )

    def call_service(self, addr, command="ping", **kwargs):
        if not addr:
            raise SubCommandFailure("Address is not specified")

        if 'error_pattern' in kwargs:
            self.error_pattern = kwargs['error_pattern']
            if self.error_pattern is None:
                self.error_pattern=[]
            if not isinstance(self.error_pattern, list):
                raise ValueError('error pattern must be a list')
            kwargs.pop('error_pattern')
        else:
            self.error_pattern = self.default_error_pattern

        con = self.connection
        # Default value setting
        timeout = self.timeout

        ping_options = AttributeDict({})
        ping_options['c'] = '5' # default to 5 packets

        # Read input values passed
        # Convert to string in case users passes non-string types
        for key in kwargs:
            if key in self._ping_option_long_to_short:
                new_key = self._ping_option_long_to_short[key]
                kwargs[new_key] = kwargs[key]
                kwargs.pop(key)
                key = new_key
            if key == 'options':
                for o in str(kwargs['options']):
                    if o in self.ping_boolean_options:
                        ping_options[o] = "" # Boolean options
                    else:
                        log.warning('Uknown ping option - %s, ignoring' % o)
            elif key in self.ping_arg_options:
                ping_options[key] = str(kwargs[key])
            else:
                log.warning('Uknown ping option - %s, ignoring' % key)

        if not 'options' in kwargs:
            ping_options['A'] = "" # Default to adaptive ping

        ipaddr = ipaddress.ip_address(addr)
        if isinstance(ipaddr, ipaddress.IPv6Address):
            ping_str = 'ping6'
        elif isinstance(ipaddr, ipaddress.IPv4Address):
            ping_str = 'ping'
        else:
            # Stringify the command in case it is an object.
            ping_str = str(command)

        for ping_option in sorted(ping_options):
            ping_str += ' -%s%s' % (ping_option, ping_options[ping_option])

        ping_str += ' %s' % addr

        p = LinuxPatterns()
        dialog = Dialog()
        dialog.append(Statement(pattern=p.prompt))

        spawn = con.spawn
        spawn.sendline(ping_str)
        try:
            self.result = dialog.process(spawn, timeout=timeout)
        except Exception as err:
            raise SubCommandFailure("Ping failed", err)

        # Remove command and hostname from output.
        if self.result:
            output = utils.truncate_trailing_prompt(
                        con.state_machine.get_state(con.state_machine.current_state).pattern,
                        self.result.match_output,
                        self.connection.hostname)
            output = re.sub(re.escape(ping_str), "", output, 1)
            self.result = output.strip()

        # Error checking is not part of the linux base infra, adding it here for now
        # TODO: update linux infra
        self.match_flag = False
        self.match_list = []
        for pat in self.error_pattern:
            m = re.search(pat, self.result)
            if m:
                self.match_list.append(m.group())
                self.match_flag = True

        if self.match_flag:
            raise SubCommandFailure(self.result, self.match_list)

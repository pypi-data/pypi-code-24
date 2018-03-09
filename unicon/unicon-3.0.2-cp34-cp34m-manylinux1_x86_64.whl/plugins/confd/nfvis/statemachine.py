__copyright__ = "# Copyright (c) 2017 by cisco Systems, Inc. All rights reserved."
__author__ = "Dave Wapstra <dwapstra@cisco.com>"

from unicon.statemachine import State, Path, StateMachine
from unicon.eal.dialogs import Dialog, Statement

from ..statemachine import ConfdStateMachine

from .patterns import NfvisPatterns

patterns = NfvisPatterns()


class NfvisStateMachine(ConfdStateMachine):
    def __init__(self, hostname=None):
        super().__init__(hostname)

    def create(self):
        cisco_exec = State('cisco_exec', patterns.cisco_prompt)
        cisco_config = State('cisco_config', patterns.cisco_config_prompt)

        self.add_state(cisco_exec)
        self.add_state(cisco_config)

        cisco_exec_to_config = Path(cisco_exec, cisco_config, 'config term', None)

        # Ignore config changes on state change
        # config commits are done as part of the configure method
        cisco_config_dialog = Dialog([
            # Uncommitted changes found, commit them? [yes/no/CANCEL] no
            [patterns.cisco_commit_changes_prompt, 'sendline(no)', None, True, False],
            ])

        cisco_config_to_exec = Path(cisco_config, cisco_exec, 'end', cisco_config_dialog)

        self.add_path(cisco_exec_to_config)
        self.add_path(cisco_config_to_exec)

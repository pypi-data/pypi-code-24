__copyright__ = "# Copyright (c) 2017 by cisco Systems, Inc. All rights reserved."
__author__ = "Dave Wapstra <dwapstra@cisco.com>"

from unicon.plugins.generic.patterns import GenericPatterns

class VosPatterns(GenericPatterns):
    def __init__(self):
        super().__init__()
        self.prompt = r'^(.*?)([\r\n]|\x1b\[K)admin:\s*'
        self.press_enter_space_q = r".*\x1b\[1mPress <enter> for 1 line, <space> for one page, or <q> to quit\x1b\[0m"
        self.paging_options = r".*\x1b\[1m\r\noptions: q=quit, n=next, p=prev, b=begin, e=end \(lines (\d+) - (\d+) of (\d+)\) : \x1b\[0m"

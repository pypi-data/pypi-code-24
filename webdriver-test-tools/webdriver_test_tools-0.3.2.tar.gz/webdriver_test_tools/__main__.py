#!/usr/bin/env python3
import argparse

from webdriver_test_tools.version import __version__
from webdriver_test_tools.project import initialize


def get_parser():
    """Returns ArgumentParser object for use with main()"""
    parser = argparse.ArgumentParser()
    # Argument for initializing
    parser.add_argument('-i', '--init', action='store_true', help='Initialize a new test project in the current directory')
    # Print version number
    parser.add_argument('-V', '--version', action='store_true', help='Print version number and exit')
    return parser


def main():
    """Parse command line arguments and handle appropriately"""
    parser = get_parser()
    args = parser.parse_args()
    if args.version is not None and args.version:
        print('webdriver_test_tools ' + __version__)
        return
    if args.init:
        initialize.main()
    # If no arguments were specified, print help
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

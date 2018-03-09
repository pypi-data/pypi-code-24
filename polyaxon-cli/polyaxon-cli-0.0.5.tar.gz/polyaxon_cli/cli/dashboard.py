# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import click
import sys

from polyaxon_cli.utils.clients import PolyaxonClients


@click.command()
@click.option('--yes', '-y', is_flag=True, default=False,
              help='Automatic yes to prompts. '
                   'Assume "yes" as answer to all prompts and run non-interactively.')
@click.option('--url', is_flag=True, default=False,
              help='Print the url of the dashboard.')
def dashboard(yes, url):
    """Open dashboard in browser."""
    dashboard_url = "{}".format(PolyaxonClients().auth.http_host)
    if url:
        click.echo(dashboard_url)
        sys.exit(0)
    if not yes:
        click.confirm('Dashboard page will now open in your browser. Continue?',
                      abort=True, default=True)

    click.launch(dashboard_url)

# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2017-2018 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Load, parse and make available Greasemonkey scripts."""

import re
import os
import json
import fnmatch
import functools
import glob
import textwrap

import attr
from PyQt5.QtCore import pyqtSignal, QObject, QUrl

from qutebrowser.utils import log, standarddir, jinja, objreg, utils
from qutebrowser.commands import cmdutils
from qutebrowser.browser import downloads


def _scripts_dir():
    """Get the directory of the scripts."""
    return os.path.join(standarddir.data(), 'greasemonkey')


class GreasemonkeyScript:

    """Container class for userscripts, parses metadata blocks."""

    def __init__(self, properties, code):
        self._code = code
        self.includes = []
        self.excludes = []
        self.requires = []
        self.description = None
        self.name = None
        self.namespace = None
        self.run_at = None
        self.script_meta = None
        self.runs_on_sub_frames = True
        for name, value in properties:
            if name == 'name':
                self.name = value
            elif name == 'namespace':
                self.namespace = value
            elif name == 'description':
                self.description = value
            elif name in ['include', 'match']:
                self.includes.append(value)
            elif name in ['exclude', 'exclude_match']:
                self.excludes.append(value)
            elif name == 'run-at':
                self.run_at = value
            elif name == 'noframes':
                self.runs_on_sub_frames = False
            elif name == 'require':
                self.requires.append(value)

    HEADER_REGEX = r'// ==UserScript==|\n+// ==/UserScript==\n'
    PROPS_REGEX = r'// @(?P<prop>[^\s]+)\s*(?P<val>.*)'

    @classmethod
    def parse(cls, source):
        """GreasemonkeyScript factory.

        Takes a userscript source and returns a GreasemonkeyScript.
        Parses the Greasemonkey metadata block, if present, to fill out
        attributes.
        """
        matches = re.split(cls.HEADER_REGEX, source, maxsplit=2)
        try:
            _head, props, _code = matches
        except ValueError:
            props = ""
        script = cls(re.findall(cls.PROPS_REGEX, props), source)
        script.script_meta = props
        if not props:
            script.includes = ['*']
        return script

    def code(self):
        """Return the processed JavaScript code of this script.

        Adorns the source code with GM_* methods for Greasemonkey
        compatibility and wraps it in an IIFE to hide it within a
        lexical scope. Note that this means line numbers in your
        browser's debugger/inspector will not match up to the line
        numbers in the source script directly.
        """
        return jinja.js_environment.get_template(
            'greasemonkey_wrapper.js').render(
                scriptName="/".join([self.namespace or '', self.name]),
                scriptInfo=self._meta_json(),
                scriptMeta=self.script_meta,
                scriptSource=self._code)

    def _meta_json(self):
        return json.dumps({
            'name': self.name,
            'description': self.description,
            'matches': self.includes,
            'includes': self.includes,
            'excludes': self.excludes,
            'run-at': self.run_at,
        })

    def add_required_script(self, source):
        """Add the source of a required script to this script."""
        # The additional source is indented in case it also contains a
        # metadata block. Because we pass everything at once to
        # QWebEngineScript and that would parse the first metadata block
        # found as the valid one.
        self._code = "\n".join([textwrap.indent(source, "    "), self._code])


@attr.s
class MatchingScripts(object):

    """All userscripts registered to run on a particular url."""

    url = attr.ib()
    start = attr.ib(default=attr.Factory(list))
    end = attr.ib(default=attr.Factory(list))
    idle = attr.ib(default=attr.Factory(list))


class GreasemonkeyManager(QObject):

    """Manager of userscripts and a Greasemonkey compatible environment.

    Signals:
        scripts_reloaded: Emitted when scripts are reloaded from disk.
            Any cached or already-injected scripts should be
            considered obsolete.
    """

    scripts_reloaded = pyqtSignal()
    # https://wiki.greasespot.net/Include_and_exclude_rules#Greaseable_schemes
    # Limit the schemes scripts can run on due to unreasonable levels of
    # exploitability
    greaseable_schemes = ['http', 'https', 'ftp', 'file']

    def __init__(self, parent=None):
        super().__init__(parent)
        self._run_start = []
        self._run_end = []
        self._run_idle = []
        self._in_progress_dls = []

        self.load_scripts()

    @cmdutils.register(name='greasemonkey-reload',
                       instance='greasemonkey')
    def load_scripts(self, force=False):
        """Re-read Greasemonkey scripts from disk.

        The scripts are read from a 'greasemonkey' subdirectory in
        qutebrowser's data directory (see `:version`).

        Args:
            force: For any scripts that have required dependencies,
                   re-download them.
        """
        self._run_start = []
        self._run_end = []
        self._run_idle = []

        scripts_dir = os.path.abspath(_scripts_dir())
        log.greasemonkey.debug("Reading scripts from: {}".format(scripts_dir))
        for script_filename in glob.glob(os.path.join(scripts_dir, '*.js')):
            if not os.path.isfile(script_filename):
                continue
            script_path = os.path.join(scripts_dir, script_filename)
            with open(script_path, encoding='utf-8') as script_file:
                script = GreasemonkeyScript.parse(script_file.read())
                if not script.name:
                    script.name = script_filename
                self.add_script(script, force)
        self.scripts_reloaded.emit()

    def add_script(self, script, force=False):
        """Add a GreasemonkeyScript to this manager.

        Args:
            force: Fetch and overwrite any dependancies which are
                   already locally cached.
        """
        if script.requires:
            log.greasemonkey.debug(
                "Deferring script until requirements are "
                "fulfilled: {}".format(script.name))
            self._get_required_scripts(script, force)
        else:
            self._add_script(script)

    def _add_script(self, script):
        if script.run_at == 'document-start':
            self._run_start.append(script)
        elif script.run_at == 'document-end':
            self._run_end.append(script)
        elif script.run_at == 'document-idle':
            self._run_idle.append(script)
        else:
            if script.run_at:
                log.greasemonkey.warning("Script {} has invalid run-at "
                                         "defined, defaulting to "
                                         "document-end"
                                         .format(script.name))
                # Default as per
                # https://wiki.greasespot.net/Metadata_Block#.40run-at
            self._run_end.append(script)
        log.greasemonkey.debug("Loaded script: {}".format(script.name))

    def _required_url_to_file_path(self, url):
        requires_dir = os.path.join(_scripts_dir(), 'requires')
        if not os.path.exists(requires_dir):
            os.mkdir(requires_dir)
        return os.path.join(requires_dir, utils.sanitize_filename(url))

    def _on_required_download_finished(self, script, download):
        self._in_progress_dls.remove(download)
        if not self._add_script_with_requires(script):
            log.greasemonkey.debug(
                "Finished download {} for script {} "
                "but some requirements are still pending"
                .format(download.basename, script.name))

    def _add_script_with_requires(self, script, quiet=False):
        """Add a script with pending downloads to this GreasemonkeyManager.

        Specifically a script that has dependancies specified via an
        `@require` rule.

        Args:
            script: The GreasemonkeyScript to add.
            quiet: True to suppress the scripts_reloaded signal after
                   adding `script`.
        Returns: True if the script was added, False if there are still
                 dependancies being downloaded.
        """
        # See if we are still waiting on any required scripts for this one
        for dl in self._in_progress_dls:
            if dl.requested_url in script.requires:
                return False

        # Need to add the required scripts to the IIFE now
        for url in reversed(script.requires):
            target_path = self._required_url_to_file_path(url)
            log.greasemonkey.debug(
                "Adding required script for {} to IIFE: {}"
                .format(script.name, url))
            with open(target_path, encoding='utf8') as f:
                script.add_required_script(f.read())

        self._add_script(script)
        if not quiet:
            self.scripts_reloaded.emit()
        return True

    def _get_required_scripts(self, script, force=False):
        required_dls = [(url, self._required_url_to_file_path(url))
                        for url in script.requires]
        if not force:
            required_dls = [(url, path) for (url, path) in required_dls
                            if not os.path.exists(path)]
        if not required_dls:
            # All the required files exist already
            self._add_script_with_requires(script, quiet=True)
            return

        download_manager = objreg.get('qtnetwork-download-manager')

        for url, target_path in required_dls:
            target = downloads.FileDownloadTarget(target_path,
                                                  force_overwrite=True)
            download = download_manager.get(QUrl(url), target=target,
                                            auto_remove=True)
            download.requested_url = url
            self._in_progress_dls.append(download)
            if download.successful:
                self._on_required_download_finished(script, download)
            else:
                download.finished.connect(
                    functools.partial(self._on_required_download_finished,
                                      script, download))

    def scripts_for(self, url):
        """Fetch scripts that are registered to run for url.

        returns a tuple of lists of scripts meant to run at (document-start,
        document-end, document-idle)
        """
        if url.scheme() not in self.greaseable_schemes:
            return MatchingScripts(url, [], [], [])

        string_url = url.toString(QUrl.FullyEncoded)

        def _match(pattern):
            # For include and exclude rules if they start and end with '/' they
            # should be treated as a (ecma syntax) regular expression.
            if pattern.startswith('/') and pattern.endswith('/'):
                matches = re.search(pattern[1:-1], string_url, flags=re.I)
                return matches is not None

            # Otherwise they are glob expressions.
            return fnmatch.fnmatch(string_url, pattern)

        tester = (lambda script:
                  any(_match(pat) for pat in script.includes) and
                  not any(_match(pat) for pat in script.excludes))

        return MatchingScripts(
            url,
            [script for script in self._run_start if tester(script)],
            [script for script in self._run_end if tester(script)],
            [script for script in self._run_idle if tester(script)]
        )

    def all_scripts(self):
        """Return all scripts found in the configured script directory."""
        return self._run_start + self._run_end + self._run_idle


def init():
    """Initialize Greasemonkey support."""
    gm_manager = GreasemonkeyManager()
    objreg.register('greasemonkey', gm_manager)

    try:
        os.mkdir(_scripts_dir())
    except FileExistsError:
        pass

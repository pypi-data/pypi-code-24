#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# When building with readthedocs, install the requirements too
if "READTHEDOCS" in os.environ:
    reqs = "requirements.txt"
    if os.path.isfile(reqs):
        from subprocess import check_call
        check_call([sys.executable, "-m", "pip", "install", "-r", reqs])

from setuptools import setup
from distutils.command.build import build as _build
from distutils.command.build_py import build_py as _build_py
from setuptools.command.install import install as _install
from setuptools.command.bdist_egg import bdist_egg as _bdist_egg
from setuptools.extension import Extension

import warnings
warnings.simplefilter("always")

from glob import glob

opj = os.path.join


cythonize_dir = "build"

macros = [
    # Disable .c line numbers in exception tracebacks
    ("CYTHON_CLINE_IN_TRACEBACK", 0),

    # Disable sanity checking in GNU libc. This is required because of
    # false positives in the longjmp() check.
    ("_FORTIFY_SOURCE", 0),
]

if sys.platform == 'cygwin':
    # On Cygwin FD_SETSIZE defaults to a rather low 64; we set it higher
    # for use with PSelecter
    # See https://github.com/sagemath/cysignals/pull/57
    macros.append(('FD_SETSIZE', 512))

kwds = dict(include_dirs=[opj("src", "cysignals"),
                          opj(cythonize_dir, "src"),
                          opj(cythonize_dir, "src", "cysignals")],
            depends=glob(opj("src", "cysignals", "*.h")),
            define_macros=macros)

extensions = [
    Extension("cysignals.signals", ["src/cysignals/signals.pyx"], **kwds),
    Extension("cysignals.pysignals", ["src/cysignals/pysignals.pyx"], **kwds),
    Extension("cysignals.alarm", ["src/cysignals/alarm.pyx"], **kwds),
    Extension("cysignals.pselect", ["src/cysignals/pselect.pyx"], **kwds),
    Extension("cysignals.tests", ["src/cysignals/tests.pyx"], **kwds),
]


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    ('License :: OSI Approved :: '
     'GNU Lesser General Public License v3 or later (LGPLv3+)'),
    'Operating System :: POSIX',
    'Programming Language :: C',
    'Programming Language :: Cython',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: System',
    'Topic :: Software Development :: Debuggers',
]


def write_if_changed(filename, text):
    """
    Write ``text`` to ``filename`` but only if it differs from the
    current content of ``filename``. If needed, the file and the
    containing directory are created.
    """
    try:
        f = open(filename, "r+")
    except IOError:
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError:
            pass
        f = open(filename, "w")
    else:
        if f.read() == text:
            # File is up-to-date
            f.close()
            return
        f.seek(0)
        f.truncate()

    print("generating {0}".format(filename))
    f.write(text)
    f.close()


# Run Distutils
class build(_build):
    def run(self):
        """
        Run ``./configure`` and Cython first.
        """
        config_h = opj(cythonize_dir, "src", "config.h")
        if not os.path.isfile(config_h):
            import subprocess
            subprocess.check_call(["make", "configure"])
            subprocess.check_call(["sh", "configure"])

        self.create_init_pxd()

        dist = self.distribution
        ext_modules = dist.ext_modules
        if ext_modules:
            dist.ext_modules[:] = self.cythonize(ext_modules)

        _build.run(self)

    def cythonize(self, extensions):
        from Cython.Build.Dependencies import cythonize
        return cythonize(extensions,
                build_dir=cythonize_dir,
                include_path=["src", os.path.join(cythonize_dir, "src")],
                compiler_directives=dict(binding=True))

    def create_init_pxd(self):
        """
        Create an ``__init__.pxd`` file in the build directory. This
        file will then be installed.

        The ``__init__.pxd`` file sets the correct compiler options for
        packages using cysignals.
        """
        # Determine installation directory
        inst = self.get_finalized_command("install")
        try:
            platlib = inst.noroot_platlib
        except AttributeError:
            platlib = inst.install_platlib
        install_dir = opj(platlib, "cysignals")

        # The variable "init_pxd" is the string which should be written to
        # __init__.pxd
        init_pxd = "# distutils: include_dirs = {0}\n".format(install_dir)
        # Append __init__.pxd from configure
        init_pxd += self.get_init_pxd()

        init_pxd_file = opj(self.build_lib, "cysignals", "__init__.pxd")
        write_if_changed(init_pxd_file, init_pxd)

    def get_init_pxd(self):
        """
        Get the contents of ``__init__.pxd`` as generated by configure.
        """
        configure_init_pxd_file = opj(cythonize_dir, "src", "cysignals", "__init__.pxd")
        with open(configure_init_pxd_file, "r") as f:
            return f.read()


class build_py(_build_py):
    """
    Custom distutils build_py class. For every package FOO, we also
    check package data for a "fake" FOO-cython package.
    """
    def get_data_files(self):
        """Generate list of '(package,src_dir,build_dir,filenames)' tuples"""
        data = []
        if not self.packages:
            return data
        for package in self.packages:
            for src_package in [package, package + "-cython"]:
                # Locate package source directory
                src_dir = self.get_package_dir(src_package)

                # Compute package build directory
                build_dir = os.path.join(*([self.build_lib] + package.split('.')))

                # Length of path to strip from found files
                plen = 0
                if src_dir:
                    plen = len(src_dir)+1

                # Strip directory from globbed filenames
                filenames = [
                    file[plen:] for file in self.find_data_files(src_package, src_dir)
                    ]
                data.append((package, src_dir, build_dir, filenames))
        return data


class install(_install):
    # When handling the --root option, keep the original paths prefixed
    # with "noroot" instead of "install"
    def change_roots(self, *names):
        for name in names:
            path = getattr(self, "install_" + name)
            setattr(self, "noroot_" + name, path)
        _install.change_roots(self, *names)


class no_egg(_bdist_egg):
    def run(self):
        from distutils.errors import DistutilsOptionError
        raise DistutilsOptionError("The package cysignals will not function correctly when built as egg. Therefore, it cannot be installed using 'python setup.py install' or 'easy_install'. Instead, use 'pip install' to install cysignals.")


with open("VERSION") as f:
    VERSION = f.read().strip()

with open('README.rst') as f:
    README = f.read()


setup(
    name="cysignals",
    author=u"Martin R. Albrecht, François Bissey, Volker Braun, Jeroen Demeyer",
    author_email="sage-devel@googlegroups.com",
    version=VERSION,
    url="https://github.com/sagemath/cysignals",
    license="GNU Lesser General Public License, version 3 or later",
    description="Interrupt and signal handling for Cython",
    long_description=README,
    classifiers=classifiers,
    setup_requires=["Cython"],

    ext_modules=extensions,
    packages=["cysignals"],
    package_dir={"cysignals": opj("src", "cysignals"),
                 "cysignals-cython": opj(cythonize_dir, "src", "cysignals")},
    package_data={"cysignals": ["*.pxi", "*.pxd", "*.h"],
                  "cysignals-cython": ["*.h"]},
    scripts=glob(opj("src", "scripts", "*")),
    cmdclass=dict(build=build, build_py=build_py, install=install, bdist_egg=no_egg),
)

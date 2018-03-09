# -*- coding: utf-8 -*-
"""
New static version of dynamic_make_init.py
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import textwrap
from os.path import join, exists
from six.moves import builtins


def autogen_init(modpath_or_name, imports=None, attrs=True, use_all=True,
                 dry=False):
    """
    Autogenerates imports for a package __init__.py file.

    Args:
        modpath_or_name (str): path to or name of a package module.
            The path should reference the dirname not the __init__.py file.
            If specified by name, must be findable from the PYTHONPATH.
        imports (list): if specified, then only these specific submodules are
            used in package generation. Otherwise, all non underscore prefixed
            modules are used.
        attrs (bool): if False, then module attributes will not be
            imported.
        use_all (bool): if False the `__all__` attribute is ignored.
        dry (bool): if True, the autogenerated string is not written

    Notes:
        This will partially override the __init__ file. By default everything
        up to the last comment / __future__ import is preserved, and everything
        after is overriden.  For more fine grained control, you can specify
        XML-like `# <AUTOGEN_INIT>` and `# </AUTOGEN_INIT>` comments around the
        volitle area. If specified only the area between these tags will be
        overwritten.

        To autogenerate a module on demand, its useful to keep a doctr comment
        in the __init__ file like this:
            python -c "import ubelt._internal as a; a.autogen_init('<your_module_path_or_name>')"
    """
    # from ubelt import util_import
    from xdoctest import static_analysis as static
    if exists(modpath_or_name):
        modpath = modpath_or_name
    else:
        modpath = static.modname_to_modpath(modpath_or_name)
        if modpath is None:
            raise ValueError('Invalid module {}'.format(modpath_or_name))

    if imports is None:
        # the __init__ file may have a variable describing the correct imports
        # should imports specify the name of this variable or should it always
        # be GLOBAL_MODULES?
        with open(join(modpath, '__init__.py'), 'r') as file:
            source = file.read()
        varname = 'GLOBAL_MODULES'
        try:
            imports = static.parse_static_value(varname, source)
        except NameError:
            pass

    modname, imports, from_imports = _static_parse_imports(modpath,
                                                           imports=imports,
                                                           use_all=use_all)
    if not attrs:
        from_imports = []
    initstr = _initstr(modname, imports, from_imports, withheader=False)
    if dry:
        print(initstr)
    else:
        _autogen_init_write(modpath, initstr)


def _static_parse_imports(modpath, imports=None, use_all=True):
    # from ubelt.meta import static_analysis as static
    # TODO: port some of this functionality over
    from xdoctest import static_analysis as static
    modname = static.modpath_to_modname(modpath)
    if imports is not None:
        import_paths = {
            m: static.modname_to_modpath(modname + '.' + m, hide_init=False)
            for m in imports
        }
    else:
        imports = []
        import_paths = {}
        for sub_modpath in static.package_modpaths(modpath, with_pkg=True,
                                                   recursive=False):
            # print('sub_modpath = {!r}'.format(sub_modpath))
            sub_modname = static.modpath_to_modname(sub_modpath)
            rel_modname = sub_modname[len(modname) + 1:]
            if rel_modname.startswith('_'):
                continue
            if not rel_modname:
                continue
            import_paths[rel_modname] = sub_modpath
            imports.append(rel_modname)
        imports = sorted(imports)

    from_imports = []
    for rel_modname in imports:
        sub_modpath = import_paths[rel_modname]
        with open(sub_modpath, 'r') as file:
            source = file.read()
        valid_callnames = None
        if use_all:
            try:
                valid_callnames = static.parse_static_value('__all__', source)
            except NameError:
                pass
        if valid_callnames is None:
            # The __all__ variable is not specified or we dont care
            top_level = static.TopLevelVisitor.parse(source)
            attrnames = list(top_level.assignments) + list(top_level.calldefs.keys())
            # list of names we wont export by default
            invalid_callnames = dir(builtins)
            valid_callnames = []
            for attr in attrnames:
                if '.' in attr or attr.startswith('_'):
                    continue
                if attr in invalid_callnames:
                    continue
                valid_callnames.append(attr)
        from_imports.append((rel_modname, sorted(valid_callnames)))
    return modname, imports, from_imports


def _autogen_init_write(modpath, initstr):
    from os.path import join, exists
    #print(new_else)
    # Get path to init file so we can overwrite it
    init_fpath = join(modpath, '__init__.py')
    print('attempting to update: %r' % init_fpath)
    assert exists(init_fpath)
    with open(init_fpath, 'r') as file_:
        lines = file_.readlines()

    # write after the last multiline comment, unless explicit tags are defined
    startline = 0
    endline = len(lines)
    explicit = False
    init_indent = ''
    for lineno, line in enumerate(lines):
        if not explicit and line.strip() in ['"""', "'''"]:
            startline = lineno + 1
        if not explicit and line.strip().startswith('from __future__'):
            startline = lineno + 1
        if not explicit and line.strip().startswith('#'):
            startline = lineno + 1
        if line.strip().startswith('# <AUTOGEN_INIT>'):  # allow tags too
            init_indent = line[:line.find('#')]
            explicit = True
            startline = lineno + 1
        if explicit and line.strip().startswith('# </AUTOGEN_INIT>'):
            endline = lineno

    initstr_ = _indent(initstr, init_indent) + '\n'

    assert startline <= endline
    new_lines = lines[:startline] + [initstr_] + lines[endline:]
    print('startline = {!r}'.format(startline))
    print('endline = {!r}'.format(endline))

    print('writing updated file: %r' % init_fpath)
    new_text = ''.join(new_lines).rstrip() + '\n'
    print(new_text)
    with open(init_fpath, 'w') as file_:
        file_.write(new_text)


def _indent(str_, indent='    '):
    return indent + str_.replace('\n', '\n' + indent)


def _initstr(modname, imports, from_imports, withheader=True):
    """ Calls the other string makers """
    header         = _make_module_header() if withheader else ''
    import_str     = _make_imports_str(imports, modname)
    fromimport_str = _make_fromimport_str(from_imports, modname)
    initstr = '\n'.join([str_ for str_ in [
        header,
        import_str,
        fromimport_str,
    ] if len(str_) > 0])
    return initstr


def _make_module_header():
    return '\n'.join([
        '# flake8:' + ' noqa',  # the plus prevents it from triggering on this file
        'from __future__ import absolute_import, division, print_function, unicode_literals'])


def _make_imports_str(imports, rootmodname='.'):
    imports_fmtstr = 'from {rootmodname} import %s'.format(
        rootmodname=rootmodname)
    return '\n'.join([imports_fmtstr % (name,) for name in imports])


def _make_fromimport_str(from_imports, rootmodname='.'):
    if rootmodname == '.':
        # dot is already taken care of in fmtstr
        rootmodname = ''
    def _pack_fromimport(tup):
        name, fromlist = tup[0], tup[1]
        from_module_str = 'from {rootmodname}.{name} import ('.format(
            rootmodname=rootmodname, name=name)
        newline_prefix = (' ' * len(from_module_str))
        if len(fromlist) > 0:
            rawstr = from_module_str + ', '.join(fromlist) + ',)'
        else:
            rawstr = ''

        # not sure why this isn't 76? >= maybe?
        packstr = '\n'.join(textwrap.wrap(rawstr, break_long_words=False,
                                          width=79, initial_indent='',
                                          subsequent_indent=newline_prefix))
        return packstr
    from_str = '\n'.join(map(_pack_fromimport, from_imports))
    return from_str

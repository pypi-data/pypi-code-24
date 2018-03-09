# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pywrapsat')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pywrapsat')
    _pywrapsat = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pywrapsat', [dirname(__file__)])
        except ImportError:
            import _pywrapsat
            return _pywrapsat
        try:
            _mod = imp.load_module('_pywrapsat', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pywrapsat = swig_import_helper()
    del swig_import_helper
else:
    import _pywrapsat
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pywrapsat.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pywrapsat.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pywrapsat.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pywrapsat.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pywrapsat.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pywrapsat.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pywrapsat.SwigPyIterator_copy(self)

    def next(self):
        return _pywrapsat.SwigPyIterator_next(self)

    def __next__(self):
        return _pywrapsat.SwigPyIterator___next__(self)

    def previous(self):
        return _pywrapsat.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pywrapsat.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pywrapsat.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pywrapsat.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pywrapsat.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pywrapsat.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pywrapsat.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pywrapsat.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pywrapsat.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


import sys
from ortools.sat import cp_model_pb2

class PySolutionCallback(object):

  def WrapAux(self, proto_str):
    try:
      response = cp_model_pb2.CpSolverResponse()
      if sys.version_info[0] < 3:
        status = response.MergeFromString(proto_str)
      else:
        status = response.MergeFromString(bytes(proto_str))
      self.Wrap(response)
    except:
      print("Unexpected error: %s" % sys.exc_info()[0])

  def Wrap(self, proto):
    pass

class SatHelper(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SatHelper, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SatHelper, name)
    __repr__ = _swig_repr
    if _newclass:
        Solve = staticmethod(_pywrapsat.SatHelper_Solve)
    else:
        Solve = _pywrapsat.SatHelper_Solve
    if _newclass:
        SolveWithParameters = staticmethod(_pywrapsat.SatHelper_SolveWithParameters)
    else:
        SolveWithParameters = _pywrapsat.SatHelper_SolveWithParameters
    if _newclass:
        SolveWithParametersAndSolutionObserver = staticmethod(_pywrapsat.SatHelper_SolveWithParametersAndSolutionObserver)
    else:
        SolveWithParametersAndSolutionObserver = _pywrapsat.SatHelper_SolveWithParametersAndSolutionObserver

    def __init__(self):
        this = _pywrapsat.new_SatHelper()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pywrapsat.delete_SatHelper
    __del__ = lambda self: None
SatHelper_swigregister = _pywrapsat.SatHelper_swigregister
SatHelper_swigregister(SatHelper)

def SatHelper_Solve(model_proto):
    return _pywrapsat.SatHelper_Solve(model_proto)
SatHelper_Solve = _pywrapsat.SatHelper_Solve

def SatHelper_SolveWithParameters(model_proto, parameters):
    return _pywrapsat.SatHelper_SolveWithParameters(model_proto, parameters)
SatHelper_SolveWithParameters = _pywrapsat.SatHelper_SolveWithParameters

def SatHelper_SolveWithParametersAndSolutionObserver(model_proto, parameters, observer):
    return _pywrapsat.SatHelper_SolveWithParametersAndSolutionObserver(model_proto, parameters, observer)
SatHelper_SolveWithParametersAndSolutionObserver = _pywrapsat.SatHelper_SolveWithParametersAndSolutionObserver

# This file is compatible with both classic and new-style classes.



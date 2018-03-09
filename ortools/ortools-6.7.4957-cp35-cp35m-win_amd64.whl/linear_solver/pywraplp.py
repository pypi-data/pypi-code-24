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
        mname = '.'.join((pkg, '_pywraplp')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pywraplp')
    _pywraplp = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pywraplp', [dirname(__file__)])
        except ImportError:
            import _pywraplp
            return _pywraplp
        try:
            _mod = imp.load_module('_pywraplp', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pywraplp = swig_import_helper()
    del swig_import_helper
else:
    import _pywraplp
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
    __swig_destroy__ = _pywraplp.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self) -> "PyObject *":
        return _pywraplp.SwigPyIterator_value(self)

    def incr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _pywraplp.SwigPyIterator_incr(self, n)

    def decr(self, n: 'size_t'=1) -> "swig::SwigPyIterator *":
        return _pywraplp.SwigPyIterator_decr(self, n)

    def distance(self, x: 'SwigPyIterator') -> "ptrdiff_t":
        return _pywraplp.SwigPyIterator_distance(self, x)

    def equal(self, x: 'SwigPyIterator') -> "bool":
        return _pywraplp.SwigPyIterator_equal(self, x)

    def copy(self) -> "swig::SwigPyIterator *":
        return _pywraplp.SwigPyIterator_copy(self)

    def next(self) -> "PyObject *":
        return _pywraplp.SwigPyIterator_next(self)

    def __next__(self) -> "PyObject *":
        return _pywraplp.SwigPyIterator___next__(self)

    def previous(self) -> "PyObject *":
        return _pywraplp.SwigPyIterator_previous(self)

    def advance(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _pywraplp.SwigPyIterator_advance(self, n)

    def __eq__(self, x: 'SwigPyIterator') -> "bool":
        return _pywraplp.SwigPyIterator___eq__(self, x)

    def __ne__(self, x: 'SwigPyIterator') -> "bool":
        return _pywraplp.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _pywraplp.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator &":
        return _pywraplp.SwigPyIterator___isub__(self, n)

    def __add__(self, n: 'ptrdiff_t') -> "swig::SwigPyIterator *":
        return _pywraplp.SwigPyIterator___add__(self, n)

    def __sub__(self, *args) -> "ptrdiff_t":
        return _pywraplp.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pywraplp.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


import numbers
from ortools.linear_solver.linear_solver_natural_api import OFFSET_KEY
from ortools.linear_solver.linear_solver_natural_api import inf
from ortools.linear_solver.linear_solver_natural_api import LinearExpr
from ortools.linear_solver.linear_solver_natural_api import ProductCst
from ortools.linear_solver.linear_solver_natural_api import Sum
from ortools.linear_solver.linear_solver_natural_api import SumArray
from ortools.linear_solver.linear_solver_natural_api import SumCst
from ortools.linear_solver.linear_solver_natural_api import LinearConstraint
from ortools.linear_solver.linear_solver_natural_api import VariableExpr

class Solver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solver, name)
    __repr__ = _swig_repr
    CLP_LINEAR_PROGRAMMING = _pywraplp.Solver_CLP_LINEAR_PROGRAMMING
    GLOP_LINEAR_PROGRAMMING = _pywraplp.Solver_GLOP_LINEAR_PROGRAMMING
    CBC_MIXED_INTEGER_PROGRAMMING = _pywraplp.Solver_CBC_MIXED_INTEGER_PROGRAMMING
    BOP_INTEGER_PROGRAMMING = _pywraplp.Solver_BOP_INTEGER_PROGRAMMING

    def __init__(self, name: 'std::string const &', problem_type: 'operations_research::MPSolver::OptimizationProblemType'):
        this = _pywraplp.new_Solver(name, problem_type)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pywraplp.delete_Solver
    __del__ = lambda self: None
    if _newclass:
        SupportsProblemType = staticmethod(_pywraplp.Solver_SupportsProblemType)
    else:
        SupportsProblemType = _pywraplp.Solver_SupportsProblemType

    def Clear(self) -> "void":
        return _pywraplp.Solver_Clear(self)

    def NumVariables(self) -> "int":
        return _pywraplp.Solver_NumVariables(self)

    def LookupVariable(self, var_name: 'std::string const &') -> "operations_research::MPVariable *":
        return _pywraplp.Solver_LookupVariable(self, var_name)

    def NumVar(self, lb: 'double', ub: 'double', name: 'std::string const &') -> "operations_research::MPVariable *":
        return _pywraplp.Solver_NumVar(self, lb, ub, name)

    def IntVar(self, lb: 'double', ub: 'double', name: 'std::string const &') -> "operations_research::MPVariable *":
        return _pywraplp.Solver_IntVar(self, lb, ub, name)

    def BoolVar(self, name: 'std::string const &') -> "operations_research::MPVariable *":
        return _pywraplp.Solver_BoolVar(self, name)

    def NumConstraints(self) -> "int":
        return _pywraplp.Solver_NumConstraints(self)

    def LookupConstraint(self, constraint_name: 'std::string const &') -> "operations_research::MPConstraint *":
        return _pywraplp.Solver_LookupConstraint(self, constraint_name)

    def Constraint(self, *args) -> "operations_research::MPConstraint *":
        return _pywraplp.Solver_Constraint(self, *args)

    def Objective(self) -> "operations_research::MPObjective *":
        return _pywraplp.Solver_Objective(self)
    OPTIMAL = _pywraplp.Solver_OPTIMAL
    FEASIBLE = _pywraplp.Solver_FEASIBLE
    INFEASIBLE = _pywraplp.Solver_INFEASIBLE
    UNBOUNDED = _pywraplp.Solver_UNBOUNDED
    ABNORMAL = _pywraplp.Solver_ABNORMAL
    NOT_SOLVED = _pywraplp.Solver_NOT_SOLVED

    def Solve(self, *args) -> "operations_research::MPSolver::ResultStatus":
        return _pywraplp.Solver_Solve(self, *args)

    def ComputeConstraintActivities(self) -> "std::vector< double,std::allocator< double > >":
        return _pywraplp.Solver_ComputeConstraintActivities(self)

    def VerifySolution(self, tolerance: 'double', log_errors: 'bool') -> "bool":
        return _pywraplp.Solver_VerifySolution(self, tolerance, log_errors)

    def InterruptSolve(self) -> "bool":
        return _pywraplp.Solver_InterruptSolve(self)

    def SetSolverSpecificParametersAsString(self, parameters: 'std::string const &') -> "bool":
        return _pywraplp.Solver_SetSolverSpecificParametersAsString(self, parameters)
    FREE = _pywraplp.Solver_FREE
    AT_LOWER_BOUND = _pywraplp.Solver_AT_LOWER_BOUND
    AT_UPPER_BOUND = _pywraplp.Solver_AT_UPPER_BOUND
    FIXED_VALUE = _pywraplp.Solver_FIXED_VALUE
    BASIC = _pywraplp.Solver_BASIC
    if _newclass:
        infinity = staticmethod(_pywraplp.Solver_infinity)
    else:
        infinity = _pywraplp.Solver_infinity

    def EnableOutput(self) -> "void":
        return _pywraplp.Solver_EnableOutput(self)

    def SuppressOutput(self) -> "void":
        return _pywraplp.Solver_SuppressOutput(self)

    def set_time_limit(self, time_limit_milliseconds: 'int64') -> "void":
        return _pywraplp.Solver_set_time_limit(self, time_limit_milliseconds)

    def wall_time(self) -> "int64":
        return _pywraplp.Solver_wall_time(self)

    def iterations(self) -> "int64":
        return _pywraplp.Solver_iterations(self)

    def nodes(self) -> "int64":
        return _pywraplp.Solver_nodes(self)

    def ComputeExactConditionNumber(self) -> "double":
        return _pywraplp.Solver_ComputeExactConditionNumber(self)

    def ExportModelAsLpFormat(self, obfuscated: 'bool') -> "std::string":
        return _pywraplp.Solver_ExportModelAsLpFormat(self, obfuscated)

    def ExportModelAsMpsFormat(self, fixed_format: 'bool', obfuscated: 'bool') -> "std::string":
        return _pywraplp.Solver_ExportModelAsMpsFormat(self, fixed_format, obfuscated)

    def LoadModelFromProto(self, input_model: 'operations_research::MPModelProto const &') -> "std::string":
        return _pywraplp.Solver_LoadModelFromProto(self, input_model)

    def Add(self, constraint, name=''):
      if isinstance(constraint, bool):
        if constraint:
          return self.RowConstraint(0, 0, name)
        else:
          return self.RowConstraint(1, 1, name)
      else:
        return constraint.Extract(self, name)

    def Sum(self, expr_array):
      result = SumArray(expr_array)
      return result

    def RowConstraint(self, *args):
      return self.Constraint(*args)

    def Minimize(self, expr):
      objective = self.Objective()
      objective.Clear()
      objective.SetMinimization()
      if isinstance(expr, numbers.Number):
          objective.AddOffset(expr)
      else:
          coeffs = expr.GetCoeffs()
          objective.AddOffset(coeffs.pop(OFFSET_KEY, 0.0))
          for v, c, in list(coeffs.items()):
            objective.SetCoefficient(v, float(c))

    def Maximize(self, expr):
      objective = self.Objective()
      objective.Clear()
      objective.SetMaximization()
      if isinstance(expr, numbers.Number):
          objective.AddOffset(expr)
      else:
          coeffs = expr.GetCoeffs()
          objective.AddOffset(coeffs.pop(OFFSET_KEY, 0.0))
          for v, c, in list(coeffs.items()):
            objective.SetCoefficient(v, float(c))

    if _newclass:
        Infinity = staticmethod(_pywraplp.Solver_Infinity)
    else:
        Infinity = _pywraplp.Solver_Infinity

    def SetTimeLimit(self, x: 'int64') -> "void":
        return _pywraplp.Solver_SetTimeLimit(self, x)

    def WallTime(self) -> "int64":
        return _pywraplp.Solver_WallTime(self)

    def Iterations(self) -> "int64":
        return _pywraplp.Solver_Iterations(self)
Solver_swigregister = _pywraplp.Solver_swigregister
Solver_swigregister(Solver)

def Solver_SupportsProblemType(problem_type: 'operations_research::MPSolver::OptimizationProblemType') -> "bool":
    return _pywraplp.Solver_SupportsProblemType(problem_type)
Solver_SupportsProblemType = _pywraplp.Solver_SupportsProblemType

def Solver_infinity() -> "double":
    return _pywraplp.Solver_infinity()
Solver_infinity = _pywraplp.Solver_infinity

def Solver_Infinity() -> "double":
    return _pywraplp.Solver_Infinity()
Solver_Infinity = _pywraplp.Solver_Infinity


def __lshift__(os: 'std::ostream &', status: 'operations_research::MPSolver::ResultStatus') -> "std::ostream &":
    return _pywraplp.__lshift__(os, status)
__lshift__ = _pywraplp.__lshift__
class Objective(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Objective, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Objective, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def Clear(self) -> "void":
        return _pywraplp.Objective_Clear(self)

    def SetCoefficient(self, var: 'Variable', coeff: 'double') -> "void":
        return _pywraplp.Objective_SetCoefficient(self, var, coeff)

    def GetCoefficient(self, var: 'Variable') -> "double":
        return _pywraplp.Objective_GetCoefficient(self, var)

    def SetOffset(self, value: 'double') -> "void":
        return _pywraplp.Objective_SetOffset(self, value)

    def offset(self) -> "double":
        return _pywraplp.Objective_offset(self)

    def AddOffset(self, value: 'double') -> "void":
        return _pywraplp.Objective_AddOffset(self, value)

    def SetOptimizationDirection(self, maximize: 'bool') -> "void":
        return _pywraplp.Objective_SetOptimizationDirection(self, maximize)

    def SetMinimization(self) -> "void":
        return _pywraplp.Objective_SetMinimization(self)

    def SetMaximization(self) -> "void":
        return _pywraplp.Objective_SetMaximization(self)

    def maximization(self) -> "bool":
        return _pywraplp.Objective_maximization(self)

    def minimization(self) -> "bool":
        return _pywraplp.Objective_minimization(self)

    def Value(self) -> "double":
        return _pywraplp.Objective_Value(self)

    def BestBound(self) -> "double":
        return _pywraplp.Objective_BestBound(self)

    def Offset(self) -> "double":
        return _pywraplp.Objective_Offset(self)
    __swig_destroy__ = _pywraplp.delete_Objective
    __del__ = lambda self: None
Objective_swigregister = _pywraplp.Objective_swigregister
Objective_swigregister(Objective)

class Variable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Variable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Variable, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")

    def name(self) -> "std::string const &":
        return _pywraplp.Variable_name(self)

    def integer(self) -> "bool":
        return _pywraplp.Variable_integer(self)

    def solution_value(self) -> "double":
        return _pywraplp.Variable_solution_value(self)

    def index(self) -> "int":
        return _pywraplp.Variable_index(self)

    def lb(self) -> "double":
        return _pywraplp.Variable_lb(self)

    def ub(self) -> "double":
        return _pywraplp.Variable_ub(self)

    def reduced_cost(self) -> "double":
        return _pywraplp.Variable_reduced_cost(self)

    def basis_status(self) -> "operations_research::MPSolver::BasisStatus":
        return _pywraplp.Variable_basis_status(self)

    def __str__(self) -> "std::string":
        return _pywraplp.Variable___str__(self)

    def __repr__(self) -> "std::string":
        return _pywraplp.Variable___repr__(self)

    def __getattr__(self, name):
      return getattr(VariableExpr(self), name)


    def SolutionValue(self) -> "double":
        return _pywraplp.Variable_SolutionValue(self)

    def Integer(self) -> "bool":
        return _pywraplp.Variable_Integer(self)

    def Lb(self) -> "double":
        return _pywraplp.Variable_Lb(self)

    def Ub(self) -> "double":
        return _pywraplp.Variable_Ub(self)

    def SetLb(self, x: 'double') -> "void":
        return _pywraplp.Variable_SetLb(self, x)

    def SetUb(self, x: 'double') -> "void":
        return _pywraplp.Variable_SetUb(self, x)

    def ReducedCost(self) -> "double":
        return _pywraplp.Variable_ReducedCost(self)
    __swig_destroy__ = _pywraplp.delete_Variable
    __del__ = lambda self: None
Variable_swigregister = _pywraplp.Variable_swigregister
Variable_swigregister(Variable)

class Constraint(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Constraint, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Constraint, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def name(self) -> "std::string const &":
        return _pywraplp.Constraint_name(self)

    def SetCoefficient(self, var: 'Variable', coeff: 'double') -> "void":
        return _pywraplp.Constraint_SetCoefficient(self, var, coeff)

    def GetCoefficient(self, var: 'Variable') -> "double":
        return _pywraplp.Constraint_GetCoefficient(self, var)

    def lb(self) -> "double":
        return _pywraplp.Constraint_lb(self)

    def ub(self) -> "double":
        return _pywraplp.Constraint_ub(self)

    def SetLB(self, lb: 'double') -> "void":
        return _pywraplp.Constraint_SetLB(self, lb)

    def SetUB(self, ub: 'double') -> "void":
        return _pywraplp.Constraint_SetUB(self, ub)

    def SetBounds(self, lb: 'double', ub: 'double') -> "void":
        return _pywraplp.Constraint_SetBounds(self, lb, ub)

    def set_is_lazy(self, laziness: 'bool') -> "void":
        return _pywraplp.Constraint_set_is_lazy(self, laziness)

    def index(self) -> "int":
        return _pywraplp.Constraint_index(self)

    def dual_value(self) -> "double":
        return _pywraplp.Constraint_dual_value(self)

    def basis_status(self) -> "operations_research::MPSolver::BasisStatus":
        return _pywraplp.Constraint_basis_status(self)

    def Lb(self) -> "double":
        return _pywraplp.Constraint_Lb(self)

    def Ub(self) -> "double":
        return _pywraplp.Constraint_Ub(self)

    def SetLb(self, x: 'double') -> "void":
        return _pywraplp.Constraint_SetLb(self, x)

    def SetUb(self, x: 'double') -> "void":
        return _pywraplp.Constraint_SetUb(self, x)

    def DualValue(self) -> "double":
        return _pywraplp.Constraint_DualValue(self)
    __swig_destroy__ = _pywraplp.delete_Constraint
    __del__ = lambda self: None
Constraint_swigregister = _pywraplp.Constraint_swigregister
Constraint_swigregister(Constraint)

class MPSolverParameters(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MPSolverParameters, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MPSolverParameters, name)
    __repr__ = _swig_repr
    RELATIVE_MIP_GAP = _pywraplp.MPSolverParameters_RELATIVE_MIP_GAP
    PRESOLVE = _pywraplp.MPSolverParameters_PRESOLVE

    def __init__(self):
        this = _pywraplp.new_MPSolverParameters()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def SetDoubleParam(self, param: 'operations_research::MPSolverParameters::DoubleParam', value: 'double') -> "void":
        return _pywraplp.MPSolverParameters_SetDoubleParam(self, param, value)

    def SetIntegerParam(self, param: 'operations_research::MPSolverParameters::IntegerParam', value: 'int') -> "void":
        return _pywraplp.MPSolverParameters_SetIntegerParam(self, param, value)

    def GetDoubleParam(self, param: 'operations_research::MPSolverParameters::DoubleParam') -> "double":
        return _pywraplp.MPSolverParameters_GetDoubleParam(self, param)

    def GetIntegerParam(self, param: 'operations_research::MPSolverParameters::IntegerParam') -> "int":
        return _pywraplp.MPSolverParameters_GetIntegerParam(self, param)
    __swig_destroy__ = _pywraplp.delete_MPSolverParameters
    __del__ = lambda self: None
MPSolverParameters_swigregister = _pywraplp.MPSolverParameters_swigregister
MPSolverParameters_swigregister(MPSolverParameters)
cvar = _pywraplp.cvar
MPSolverParameters.kDefaultPrimalTolerance = _pywraplp.cvar.MPSolverParameters_kDefaultPrimalTolerance


def setup_variable_operator(opname):
  setattr(Variable, opname,
          lambda self, *args: getattr(VariableExpr(self), opname)(*args))
for opname in LinearExpr.OVERRIDDEN_OPERATOR_METHODS:
  setup_variable_operator(opname)

# This file is compatible with both classic and new-style classes.



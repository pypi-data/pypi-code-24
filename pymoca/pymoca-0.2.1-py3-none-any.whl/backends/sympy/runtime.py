# do not edit, generated by pymoca

from __future__ import print_function, division

from typing import List

import numpy as np
import scipy.integrate
import sympy


# noinspection PyPep8Naming
class OdeModel:
    def __init__(self):
        self.t = sympy.symbols('t')
        self.x = sympy.Matrix([])
        self.u = sympy.Matrix([])
        self.y = sympy.Matrix([])
        self.p = sympy.Matrix([])
        self.c = sympy.Matrix([])
        self.v = sympy.Matrix([])
        self.x0 = {}
        self.u0 = {}
        self.p0 = {}
        self.c0 = {}
        self.eqs = []
        self.f = None
        self.g = None

    def compute_fg(self):
        n_states = len(self.x)
        n_vars = len(self.v)
        n_eqs = len(self.eqs)
        if n_states + n_vars != n_eqs:
            raise RuntimeError('# states: {:d} + # variables: {:d} != # equations {:d}'.format(
                n_states, n_vars, n_eqs))
        fg_sol = sympy.solve(self.eqs, list(self.x.diff(self.t)) + list(self.v) + list(self.y))
        self.f = self.x.diff(self.t).subs(fg_sol)
        assert len(self.x) == len(self.f)
        self.g = self.y.subs(fg_sol)
        assert len(self.y) == len(self.g)

    def linearize_symbolic(self) -> List[sympy.MutableDenseMatrix]:
        A = sympy.Matrix([])
        B = sympy.Matrix([])
        C = sympy.Matrix([])
        D = sympy.Matrix([])
        if len(self.x) > 0:
            if len(self.f) > 0:
                A = self.f.jacobian(self.x)
            if len(self.g) > 0:
                C = self.g.jacobian(self.x)
        if len(self.u) > 0:
            if len(self.f) > 0:
                B = self.f.jacobian(self.u)
            if len(self.g) > 0:
                D = self.g.jacobian(self.u)
        return [A, B, C, D]

    def linearize(self, x0: np.array=None, u0: np.array=None) -> List[np.array]:
        """
        Numerical linearization
        :param x0: initial state
        :param u0: initial input
        :return: list of Jacobians
        """
        ss = self.linearize_symbolic()
        ss_eval = []
        ss_subs = {}
        if x0 is None:
            # noinspection PyUnusedLocal
            x0 = self.x.subs(self.x0)[:]
        if u0 is None:
            # noinspection PyUnusedLocal
            u0 = self.u.subs(self.u0)[:]
        # note, we don't substitute y here since
        # all equations should be in terms of x, u
        # if you substitute y, it will resubstitute
        # over x and cause issues
        ss_subs.update({self.x[i]: x0[i] for i in range(len(self.x))})
        ss_subs.update({self.u[i]: u0[i] for i in range(len(self.u))})
        ss_subs.update(self.p0)
        ss_subs.update(self.c0)
        for i in range(len(ss)):
            ss_eval += [np.matrix(ss[i].subs(ss_subs)).astype(float)]
        return ss_eval

    def simulate(self, x0: List[float] = None, u0: float = None, t0: float = 0, tf: float = 10,
                 dt: float = 0.01) -> dict:
        x_sym = sympy.DeferredVector('x')
        # noinspection PyUnusedLocal
        y_sym = sympy.DeferredVector('y')
        u_sym = sympy.DeferredVector('u')
        ss_subs = {self.x[i]: x_sym[i] for i in range(len(self.x))}
        ss_subs.update({self.u[i]: u_sym[i] for i in range(len(self.u))})
        ss_subs.update(self.p0)
        ss_subs.update(self.c0)

        # create f (dynamics) lambda function
        f_lam = sympy.lambdify((self.t, x_sym, u_sym), self.f.subs(ss_subs))
        res = np.array(f_lam(0, np.zeros(len(self.x)), np.zeros(len(self.u))), dtype=float)
        if len(res) != len(self.x):
            raise IOError("f doesn't return correct size", res, self.x)

        # create jacobian lambda function
        if len(self.x) > 0 and len(self.f) > 0:
            jac_lam = sympy.lambdify((self.t, x_sym, u_sym), self.f.jacobian(self.x).subs(ss_subs))
            res = np.array(jac_lam(0, np.zeros(len(self.x)), np.zeros(len(self.u))), dtype=float)
            if len(res.shape) == 2 and res.shape[0] != len(self.x):
                raise IOError("jacobian doesn't return correct size", res['f'])
        else:
            jac_lam = None

        # create g (measurement) lambda function
        g_lam = sympy.lambdify((self.t, x_sym, u_sym), self.g.subs(ss_subs))
        res = np.array(g_lam(0, np.zeros(len(self.x)), np.zeros(len(self.u))), dtype=float)
        if len(res.shape) == 2 and res.shape[0] != len(self.y):
            raise IOError("g doesn't return correct size", res, self.y)

        ode = scipy.integrate.ode(f_lam, jac_lam)
        ss_subs.update(self.x0)
        ss_subs.update(self.u0)
        if x0 is None:
            x0 = self.x.subs(self.x0)[:]
        if u0 is None:
            u0 = self.u.subs(self.u0)[:]
        ode.set_initial_value(x0, t0)
        y0 = g_lam(0, x0, u0)
        data = {
            't': [t0],
            'x': [x0],
            'y': [y0],
            'u': [u0],
        }
        while ode.t + dt <= tf:
            ode.set_f_params(u0)
            ode.set_jac_params(u0)
            if len(self.x) > 0:
                ode.integrate(ode.t + dt)
            else:
                ode.t += dt
            x = ode.y
            y = g_lam(ode.t, x, u0)
            data['t'] += [ode.t]
            data['x'] += [x]
            data['y'] += [y]
            data['u'] += [u0]
        data = {key: np.array(data[key]) for key in data.keys()}
        return data

    def __repr__(self):
        return repr(self.__dict__)

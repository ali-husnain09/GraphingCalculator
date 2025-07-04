import sympy as sp

x = sp.symbols('x')

def get_derivative(expr):
    return sp.diff(expr, x)

def latexify(expr):
    return sp.latex(expr)

def lambdify_expr(expr):
    return sp.lambdify(x, expr, modules=["numpy"])

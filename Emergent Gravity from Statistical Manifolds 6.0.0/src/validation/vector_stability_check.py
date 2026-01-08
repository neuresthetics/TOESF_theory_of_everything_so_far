import sympy as sp

A, m = sp.symbols('A m', real=True)
E = sp.symbols('E', positive=True)
B = sp.symbols('B', positive=True)
divA = sp.symbols('divA', real=True)

H = (1/2) * sp.integrate(E**2 + B**2 + m**2 * A**2 + (divA)**2, (sp.symbols('x y z')))
print(sp.simplify(H))  # Bounded positive for real fields
# Expected: Positive definite expression
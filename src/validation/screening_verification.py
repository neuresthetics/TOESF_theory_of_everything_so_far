import sympy as sp

# Chameleon screening
phi, rho, M, beta0, n = sp.symbols('phi rho M beta0 n', positive=True)
V = M**(4 + n) * phi**(-n)
L = -sp.diff(phi, sp.symbols('x'))**2 / 2 - V - beta0 / (1 + rho / 1e-24) * phi
eom = sp.diff(L, phi) - sp.diff(sp.diff(L, sp.diff(phi, sp.symbols('x'))), sp.symbols('x'))
# Solve for phi_min (approx for high rho)
phi_min = sp.solve(eom, phi)[0].approx()  # Symbolic solve
# Force
F = -sp.diff(beta0 / (1 + rho / 1e-24) * phi_min, sp.symbols('x'))
# Check continuity at rho transition
rho_trans = 1e-24
F_plus = F.subs(rho, rho_trans + 1e-30)
F_minus = F.subs(rho, rho_trans - 1e-30)
print(f"Discontinuity: {sp.simplify(F_plus - F_minus):.2e}")  # Expected ~0
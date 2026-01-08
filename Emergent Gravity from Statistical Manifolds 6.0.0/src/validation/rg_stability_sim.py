import numpy as np
from scipy.integrate import odeint

def rg_flow(beta, mu, beta0=0.008):
    dbeta_dmu = -beta**2 / (16 * np.pi**2)
    return odeint(lambda b, m: dbeta_dmu, beta0, mu)

mu = np.logspace(0, 40, 100)  # Up to M_P ~10^19 GeV
beta_mu = rg_flow(0, mu)
print(f"beta at M_P: {beta_mu[-1]:.4f}")  # Expected ~0.0085, finite
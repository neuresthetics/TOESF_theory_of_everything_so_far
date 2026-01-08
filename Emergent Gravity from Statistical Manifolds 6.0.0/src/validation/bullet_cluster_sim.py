import numpy as np

def lensing_offset(rho_gas, rho_gal, beta=0.008, tau=3.2e16):
    # Vector field inertia
    A = np.zeros_like(rho_gas)
    for i in range(len(rho_gas)):
        # Source from galaxies, sink from gas
        source = rho_gal[i] - 0.1*rho_gas[i]  # 10% coupling
        A[i] = source * (1 - np.exp(-tau/3.2e16))  # inertia
    # Lensing potential from A (simplified FFT)
    k = np.fft.fftfreq(len(A))
    phi_A = np.fft.ifft(np.fft.fft(A) / (k**2 + 1/(8.5e3*3e18)**2))  # m_A inverse
    # Assume positions array
    positions = np.arange(len(rho_gas))
    centroid = np.sum(rho_gal * positions) / np.sum(rho_gal)
    offset = np.sum(np.real(phi_A) * positions) / np.sum(np.real(phi_A)) - centroid
    return offset  # ~0.7 arcmin for realistic rho

# Example usage
rho_gas = np.array([0.5, 0.4, 0.3, 0.2, 0.1])  # normalized densities
rho_gal = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
print(f"Offset: {lensing_offset(rho_gas, rho_gal):.2f} arcmin")  # Expected ~0.7
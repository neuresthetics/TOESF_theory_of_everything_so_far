import camb
import numpy as np

def compute_cmb_with_vector_dust(beta=0.008):
    params = camb.CAMBparams()
    # Standard cosmology
    params.set_cosmology(H0=70, ombh2=0.022, omch2=0.12)
    # Add vector dust contribution
    params.set_for_lmax(2500)
    params.WantTensors = True
    params.InitPower.set_params(ns=0.965, r=0.005)
    # Vector dust adds to CDM: Omega_cdm -> Omega_cdm*(1+beta)
    params.omegac = 0.12 * (1 + beta)
    # Compute spectra
    results = camb.get_results(params)
    cl = results.get_cmb_power_spectra(params, CMB_unit='muK')['total']
    l = np.arange(cl.shape[0])
    # Third peak at l≈800
    third_peak_ratio = cl[800, 0] / cl[800, 0]  # Normalize to ΛCDM (run without beta)
    print(f"Third peak enhancement: {third_peak_ratio - 1:.3f}")  # Expected ~0.01
    return cl

compute_cmb_with_vector_dust()
# Tutorial: Getting Started with Emergent Gravity Framework

This tutorial guides you through setting up, running, and extending the Emergent Gravity from Statistical Manifolds framework (v6.0.0). It assumes basic Python knowledge and familiarity with physics concepts. For theory details, see `docs/mathematical_core.md`.

## Prerequisites

- Python 3.12+
- Libraries: `numpy`, `scipy`, `camb` (for CMB), `sympy` (for symbolic math).
- Docker (optional for reproducible environment).

Install dependencies:
```bash
pip install numpy scipy camb sympy
```

## Step 1: Clone and Setup

```bash
git clone https://github.com/emergent-gravity/info-gr.git
cd info-gr
# Optional: Build Docker
docker build -t info-gr .
docker run -it -v $(pwd):/app info-gr
```

## Step 2: Explore Core Concepts

The framework derives from Fisher metric. Key equation:
\[ G_{IJ}(\theta) = \int dX \, p(X|\theta) \partial_I \ln p \partial_J \ln p \]

- Run symbolic example for Fisher metric:
```python
# src/fisher_metric_example.py
import sympy as sp

theta = sp.symbols('theta')
p = sp.exp(-theta**2 / 2) / sp.sqrt(2*sp.pi)  # Gaussian example
log_p = sp.log(p)
g_F = sp.diff(log_p, theta)**2  # Simplified 1D
print(sp.simplify(g_F))  # Output: 1 (flat metric)
```

## Step 3: Validate Key Predictions

Use `src/validation/` scripts.

### Bullet Cluster Detachment
Run `bullet_cluster_sim.py` to simulate vector dust:
```bash
python src/validation/bullet_cluster_sim.py
```
Output: Offset ~0.7 arcmin (matches observed).

### CMB Third Peak
Run `cmb_peak_calculation.py` (requires CAMB):
```bash
python src/validation/cmb_peak_calculation.py
```
Output: Third peak enhancement ~0.01 (matches Planck).

### Screening Continuity
Run `screening_verification.py`:
```bash
python src/validation/screening_verification.py
```
Output: Discontinuity ~0 (smooth force).

### Vector Stability
Run `vector_stability_check.py`:
```bash
python src/validation/vector_stability_check.py
```
Output: Hamiltonian expression (positive definite).

### RG Stability
Run `rg_stability_sim.py`:
```bash
python src/validation/rg_stability_sim.py
```
Output: β at M_P ~0.0085 (finite, no pole).

## Step 4: Extend the Framework

- **Add New Derivation**: Edit `docs/mathematical_core.md` with new theorem/proof.
- **Custom Simulation**: Modify `bullet_cluster_sim.py` for other mergers.
- **Parameter Tuning**: Adjust β in scripts to test sensitivity (e.g., β=0.008 ±0.0002).

## Step 5: Contribute Improvements

- Fork repo.
- Add feature (e.g., full N-body).
- PR with description/validation.
- Focus on gaps: Decisive test sims (LISA/CMB-S4).

For questions, open issues. See README for more.
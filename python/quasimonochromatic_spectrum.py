from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

_output_dir = Path('figures/python')

_E0 = 4.5
_DE0 = 0.15/2.4

_n_energies = 500
_energies = np.linspace(0.1, 5., _n_energies)
spectrum = norm.pdf(_energies, _E0, _DE0)
spectrum = spectrum/np.max(spectrum)

_figsize=(3.5, 3.2)

fig, ax = plt.subplots(1,1, figsize=_figsize)
ax.set_xlabel('Photon energy (MeV)')
ax.set_ylabel('Intensity')
ax.plot(_energies, spectrum, color='black')
plt.tight_layout()
plt.savefig(_output_dir / 'quasimonochromatic.pdf')
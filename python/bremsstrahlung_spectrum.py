    # This file is part of nrf_seminar.

    # nrf_seminar is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # nrf_seminar is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with nrf_seminar.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from schiff import schiff

_output_dir = Path('figures/python')

_E0 = 5.
_Z = 29

_n_energies = 500
_energies = np.linspace(0.1, 0.9*_E0, _n_energies)
spectrum = schiff(_energies, _E0, _Z, e2=1.)
spectrum = spectrum/np.max(spectrum)

_figsize=(3.5, 3.2)
_ylim=[1e-3, 1.]

fig, ax = plt.subplots(1,1, figsize=_figsize)
ax.set_xlabel('Photon energy (MeV)')
ax.set_ylabel('Intensity')
ax.set_ylim(_ylim)
ax.plot(_energies, spectrum, color='black')
plt.tight_layout()
plt.savefig(_output_dir / 'bremsstrahlung_linear.pdf')

fig, ax = plt.subplots(1,1, figsize=_figsize)
ax.set_xlabel('Photon energy (MeV)')
ax.set_ylabel('Intensity')
ax.set_ylim(_ylim)
ax.semilogy(_energies, spectrum, color='black')
plt.tight_layout()
plt.savefig(_output_dir / 'bremsstrahlung_logarithmic.pdf')
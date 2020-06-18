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

from nrf_cross_section import cross_section_breit_wigner

_output_dir = Path('figures/python')

_resonance_energy = 1. # MeV
_photon_energy = 1. # MeV
_Ji = 0 
_Jf = 1
_Gamma_f = _Gamma_if = _Gamma_kf = 1e-7 # MeV
_mass = 20.

_energy_range = 20. # in units of Gamma_f
_n_energies = 501
energies = np.linspace(_resonance_energy-_energy_range*_Gamma_f, _resonance_energy+_energy_range*_Gamma_f, _n_energies)
relative_energies = (energies - _resonance_energy)*1e6 # eV

cross_section = cross_section_breit_wigner(energies, _resonance_energy, _photon_energy, _Ji, _Jf, _Gamma_f, _Gamma_if, _Gamma_kf)
cross_section = cross_section/np.max(cross_section)

photon_energies = [-0.5*_energy_range*_Gamma_f*1e6, 0., 0.5*_energy_range*_Gamma_f*1e6]
colors = ['lime', 'orange', 'red']

fig, ax = plt.subplots(1,1, figsize=(4.2,3))
ax.set_xlabel('Difference to Resonance Wave Length')
ax.set_ylabel('Probability for Absorption')
ax.plot(relative_energies, cross_section, '-', color='black')
for i, ene in enumerate(photon_energies):
    ax.plot([ene]*2, [0., 1.], '-', lw=6, color=colors[i], alpha=0.5)
output_file_name = 'resonance_shape.pdf'
plt.tight_layout()
plt.savefig(_output_dir / output_file_name)
print('Created file \'{}\'.'.format(output_file_name))
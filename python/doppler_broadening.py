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

from nrf_cross_section import cross_section_doppler_broadened_approx

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

temperatures = [0., 77., 293.]
line_styles = [':', '--', '-']
colors = ['black', 'blue', 'red']
labels = ['0 K (abs. zero)', '77 K (liquid $N_2$)', '293 K (room)']
filename = ['cross_section_absolute_zero', 'cross_section_ln2', 'cross_section_room_temperature']

cross_sections = np.zeros((len(temperatures), _n_energies))
for i, t in enumerate(temperatures):
    cross_sections[i] = cross_section_doppler_broadened_approx(energies, _resonance_energy, _photon_energy, _Ji, _Jf, _Gamma_f, _Gamma_if, _Gamma_kf, temperature=t, mass=_mass)

for i in range(len(cross_sections)):
    fig, ax = plt.subplots(1,1, figsize=(5,4))
    ax.set_xlabel('Distance to Resonance Energy (eV)')
    ax.set_ylabel('Absorption cross section (fm$^2$)')
    for j in range(i+1):
        ax.plot(relative_energies, cross_sections[j], line_styles[j], color=colors[j], label=labels[j])
    ax.legend()
    output_file_name = filename[i] + '.pdf'
    plt.savefig(_output_dir / output_file_name)
    print('Created file \'{}\'.'.format(output_file_name))
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
from scipy.stats import norm

_output_dir = Path('figures/python')

_n_points = 2000
_wave_lengths = np.linspace(0., 1., _n_points)

_resonance_wave_lengths = [0.3, 0.5, 0.8]
_absorbed_wave_lengths = [0.8]
_absorbed_wave_lengths_alternative = [0.3, 0.5, 0.8]

_resolutions = [0.001, 0.005, 0.01, 0.03]
_labels = [r'$\sigma = 0$', r'$\sigma = 5 \Gamma$', r'$\sigma = 10 \Gamma$', r'$\sigma = 30 \Gamma$']
_file_name_suffixes = ['001', '005', '01', '03']

spectrum = np.zeros(_n_points)

for wl in _resonance_wave_lengths:
    spectrum = spectrum + norm.pdf(_wave_lengths, wl, _resolutions[0])
_transmission_max = np.max(spectrum)

_figsize = (4., 3.2)
_xlabel = 'Wave length'

for i in range(len(_resolutions)):

    spectrum = np.zeros(_n_points)
    for wl in _resonance_wave_lengths:
        spectrum = spectrum + norm.pdf(_wave_lengths, wl, _resolutions[i])
    spectrum = np.random.poisson(spectrum)

    absorption_spectrum = np.zeros(_n_points)
    for wl in _absorbed_wave_lengths:
        absorption_spectrum = absorption_spectrum + norm.pdf(_wave_lengths, wl, _resolutions[i])
    transmission_spectrum = np.random.poisson(_transmission_max-absorption_spectrum)

    absorption_spectrum_alternative = np.zeros(_n_points)
    for wl in _absorbed_wave_lengths_alternative:
        absorption_spectrum_alternative = absorption_spectrum_alternative + norm.pdf(_wave_lengths, wl, _resolutions[i])
    transmission_spectrum_alternative = np.random.poisson(_transmission_max-absorption_spectrum_alternative)

    for j, wl in enumerate(_resonance_wave_lengths):
        spectrum_single = np.random.poisson(norm.pdf(_wave_lengths, wl, _resolutions[i]))

        fig, ax = plt.subplots(1,1, figsize=_figsize)
        ax.set_xlabel(_xlabel)
        ax.set_ylabel('Scattering intensity')
        ax.plot(_wave_lengths, spectrum_single, color='black', label=_labels[i])
        ax.legend()
        output_file_name = 'scattering_single_' + str(j) + '_' + _file_name_suffixes[i] + '.pdf'
        plt.tight_layout()
        plt.savefig(_output_dir / output_file_name)
        print('Created file \'{}\'.'.format(output_file_name))

    fig, ax = plt.subplots(1,1, figsize=_figsize)
    ax.set_xlabel(_xlabel)
    ax.set_ylabel('Scattering intensity')
    ax.plot(_wave_lengths, spectrum, color='black', label=_labels[i])
    ax.legend()
    output_file_name = 'scattering_' + _file_name_suffixes[i] + '.pdf'
    plt.tight_layout()
    plt.savefig(_output_dir / output_file_name)
    print('Created file \'{}\'.'.format(output_file_name))

    fig, ax = plt.subplots(1,1, figsize=_figsize)
    ax.set_xlabel(_xlabel)
    ax.set_ylabel('Transmission intensity')
    ax.plot(_wave_lengths, transmission_spectrum, color='black', label=_labels[i])
    ax.legend()
    output_file_name = 'transmission_' + _file_name_suffixes[i] + '.pdf'
    plt.tight_layout()
    plt.savefig(_output_dir / output_file_name)
    print('Created file \'{}\'.'.format(output_file_name))

    fig, ax = plt.subplots(1,1, figsize=_figsize)
    ax.set_xlabel(_xlabel)
    ax.set_ylabel('Transmission intensity')
    ax.plot(_wave_lengths, transmission_spectrum_alternative, color='black', label=_labels[i])
    ax.legend()
    output_file_name = 'transmission_alternative_' + _file_name_suffixes[i] + '.pdf'
    plt.tight_layout()
    plt.savefig(_output_dir / output_file_name)
    print('Created file \'{}\'.'.format(output_file_name))
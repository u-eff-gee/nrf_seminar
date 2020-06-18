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

import warnings

import numpy as np
import scipy.constants as constants

_sqrt_pi = np.sqrt(np.pi)

def cross_section_breit_wigner(energy, resonance_energy, photon_energy, Ji, Jf, Gamma_f, Gamma_if, Gamma_kf):
    """Cross section for the nuclear resonance fluorescence process

    See, e.g. Eq. (3) in F. R. Metzger, Prog. Nucl. Phys. 7 (1959) 53-88.

    Parameters
    ----------
    energy: float
        Energy in MeV.
    resonance_energy: float
        Resonance energy in MeV.
    photon_energy: float
        Energy of the absorbed photon in MeV which corresponds to the resonance transition.
    Ji, Jf: float
        Angular momentum quantum numbers of the initial and final state in units of the \
reduced Planck constant.
    Gamma_f: float
        Total width of the final state in MeV.
    Gamma_if, Gamma_kf: float
        Partial widths for the excitation transition i->f and another decay branch i->k. \
For an 'elastic' NRF process, set Gamma_if = Gamma_kf. \
For a photoabsorption process, set Gamma_kf = Gamma_f. This corresponds to summing over all \
possible decay branches.

    Returns
    -------
    float
        Cross section in fm**2.
    """
    return np.pi*(constants.physical_constants['reduced Planck constant times c in MeV fm'][0]/photon_energy)**2*(2.*Jf+1.)/(2.*Ji+1.)*Gamma_if*Gamma_kf/((energy - resonance_energy)*(energy - resonance_energy) + 0.25*Gamma_f*Gamma_f)

def cross_section_doppler_broadened_approx(energy, resonance_energy, photon_energy, Ji, Jf, Gamma_f, Gamma_if, Gamma_kf, temperature=0., mass=1.):
    """Cross section for the nuclear resonance fluorescence process at finite temperatures

    This implementation uses an approximation which is valid if the total width of the excited \
state is much smaller than the Doppler width.
    See, e.g. Eq. (11) in F. R. Metzger, Prog. Nucl. Phys. 7 (1959) 53-88.

    Parameters
    ----------
    energy: float
        Energy in MeV.
    resonance_energy: float
        Resonance energy in MeV.
    photon_energy: float
        Energy of the absorbed photon in MeV which corresponds to the resonance transition.
    Ji, Jf: float
        Angular momentum quantum numbers of the initial and final state in units of the \
reduced Planck constant.
    Gamma_f: float
        Total width of the final state in MeV.
    Gamma_if, Gamma_kf: float
        Partial widths for the excitation transition i->f and another decay branch i->k. \
For an 'elastic' NRF process, set Gamma_if = Gamma_kf. \
For a photoabsorption process, set Gamma_kf = Gamma_f. This corresponds to summing over all \
possible decay branches.
    temperature: float
        Temperature in Kelvin (default: 0 K). If the temperature is 0 K, the function \
cross_section_breit_wigner will be called
    mass: float
        Nuclear mass in atomic mass units (u, AMU) (default: 1 u).

    Returns
    -------
    float
        Cross section in fm**2.
    """

    if temperature == 0.:
        return cross_section_breit_wigner(energy, resonance_energy, photon_energy, Ji, Jf, Gamma_f, Gamma_if, Gamma_kf)

    sigma_0 = 4.*np.pi*(constants.physical_constants['reduced Planck constant times c in MeV fm'][0]/photon_energy)**2*(2.*Jf+1.)/(2.*Ji+1.)*Gamma_if*Gamma_kf/(Gamma_f*Gamma_f)

    Delta = resonance_energy*np.sqrt(2.*constants.physical_constants['Boltzmann constant in eV/K'][0]*1e-6*temperature/(mass*constants.physical_constants['atomic mass constant energy equivalent in MeV'][0]))

    Delta_Gamma_ratio = Delta / Gamma_f
    if Delta_Gamma_ratio < 10.:
        warnings.warn('The ratio Delta/Gamma = {:f} is smaller than ten. The chosen approximation may not be valid.'.format(Delta_Gamma_ratio))

    return sigma_0*Gamma_f*_sqrt_pi/(2.*Delta)*np.exp(-((energy-resonance_energy)/Delta)**2)
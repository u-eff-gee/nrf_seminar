from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import jv

_output_dir = Path('figures/python')

def circ_aper_diff(theta, radius):
    """Fraunhofer diffraction pattern of a circular aperture

    Equation (10.47) in W. Demtröder, Experimentalphysik, Band 2, Elektrizität und Optik, 3. Auflage, \
    Springer-Verlag Berlin Heidelberg (2004).

    The diffraction pattern depends only on the ratio of the aperture radius and the wave length, \
    therefore they have been merged into a single parameter.

    Parameters
    ----------
    theta: float
        Polar angle in radians with respect to the optical axis of the incoming planar wave. at which the \
    diffraction is observed.
    radius: float
        Radius of the circular aperture in units of the wave length.

    Returns
    -------
    float
        Intensity of the scattered light after going through a circular aperture, observed at an \
    angle theta.
    """

    x = 2.*np.pi*radius*np.sin(theta)

    return (2.*jv(1, x)/x)**2

radius = [0.1, 1., 10.]
filename = ['circular_aperture_one_tenth', 'circular_aperture_one', 'circular_aperture_ten']
theta = np.linspace(-0.5*np.pi, 0.5*np.pi, 1000)

diff_patt = np.zeros((len(radius), len(theta)))

for i, r in enumerate(radius):
    diff_patt[i] = circ_aper_diff(theta, r)

for i, r in enumerate(radius):
    fig, ax = plt.subplots(1,1, figsize=(4.2,4))
    ax.set_xlabel('Scattering angle')
    ax.set_xlim(-0.5*np.pi, 0.5*np.pi)
    ax.set_xticks([-0.5*np.pi, -0.25*np.pi, 0., 0.25*np.pi, 0.5*np.pi])
    ax.set_xticklabels([r'-90$^\circ$', r'-45$^\circ$', r'0$^\circ$', r'45$^\circ$', r'90$^\circ$'])
    ax.set_ylabel('Relative Intensity')
    ax.set_ylim(0., 1.1)
    for j in range(0,i):
        ax.plot(theta, diff_patt[j], '--', color='grey')
    ax.plot(theta, diff_patt[i], color='darkorange')
    output_file_name = filename[i] + '.pdf'
    plt.savefig(_output_dir / output_file_name)
    print('Created file \'{}\'.'.format(output_file_name))
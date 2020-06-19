# Nuclear Resonance Fluorescence
## Renaissance of a 70-year-old Technique

This talk was prepared for the 'Advances in Physics' seminar at [TUNL](https://tunl.duke.edu/).
The abstract can be found in the `abstract.txt` file.
It was intended to be an introduction to the nuclear resonance fluorescence (NRF) method for undergraduate (physics) students with a basic knowledge of (relativistic) mechanics (conservation of momentum) wave optics (diffraction, Doppler effect) and atomic physics (Bohr model of the atom, electromagnetic transitions, spectroscopy).
Two previous talks in the same series by Prof. M. Ahmed ('Exploring Neutron Stars on Earth') and Prof. R. V. F. Janssens (' It’s Nuclear: The Hulk, Gamma rays, the Atomic Nucleus, and Shining Stars') had already introduced basic concepts of nuclear physics (common units, the nuclear chart, transitions, decays, nuclear astrophysics) and gamma-ray spectroscopy.

The repository provides the slides in a PDF file, but it also contains the LaTeX and python code to generate all slides.
Instructions for the compilation of the code are given below.
Some copyrighted figures have been removed from the PDF and the `figure` directory.
In the code, the respective `includegraphics` commands have been commented, and a descriptive text is displayed instead.
Please refer to the reference section for information on the sources of these figures.

The 70 years mentioned in the subtitle refer to the first experimental demonstration of NRF by Moon in 1951, and the recent developments, after the first use of quasi-monochromatic, polarized photon beams for NRF experiments, are interpreted as a 'renaissance'.

## Prerequisites

 * **LaTeX** and all packages used in `nrf_seminar.tex`, in particular `beamer` and `PGF`/`TikZ`.
 * **python3**, with the libraries `matplotlib`, `numpy`, and `scipy`.

## Build

To build, type 

```
make
```

in the directory where `README.md` is located.
This will create a file `nrf_seminar.pdf`.

The `Makefile` also provides a command to clean up all generated files:

```
make clean
```

Depending on the system, it may be necessary to rename the `LATEX` and `PYTHON` executables in the `Makefile`.

To speed up the build process, the number of samples (`NWAVEFORMSAMPLES`) for plotting sine curves ('photons') can be set to a lower value.
In that case, some wave trains will not look smooth.

## License

Copyright (C) 2020

U. Friman-Gayer (ufg@email.unc.edu)

This code is distributed under the terms of the GNU General Public License. See the COPYING file for more information.

## Acknowledgements

The author would like to thank Dr. A. Crowell for organizing the seminar and Prof. R. V. F. Janssens for helpful discussions.
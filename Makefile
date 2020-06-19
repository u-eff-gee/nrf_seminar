LATEX=pdflatex

PROJECT=nrf_seminar
LATEX_SOURCE_DIR=source/
LATEX_SOURCE=$(addprefix ${LATEX_SOURCE_DIR}, $(addsuffix .tex, absorption_spectroscopy bremsstrahlung doppler_broadening figures_1 figures_2 figures_3 footer literature quasimonochromatic resonance_fluorescence resonance_fluorescence_atom resonance_fluorescence_nucleus r_process scattering scanning spectrum_summary title))
LATEX_OUTPUT=$(addprefix ${PROJECT}, .aux .log .nav .out .pdf .snm .toc)

PYTHON=python
PYTHON_SOURCE_DIR=python/
PYTHON_SOURCE=$(addprefix ${PYTHON_SOURCE_DIR}, $(addsuffix .py, bremsstrahlung_spectrum circular_aperture_diffraction doppler_broadening nrf_cross_section resolution quasimonochromatic_spectrum resonance_shape schiff))
PYTHON_FIGURES_DIR=figures/python/
PYTHON_FIGURES=$(addprefix ${PYTHON_FIGURES_DIR}, $(addsuffix .pdf, bremsstrahlung_linear bremsstrahlung_logarithmic circular_aperture_one_tenth circular_aperture_one circular_aperture_ten cross_section_absolute_zero cross_section_ln2 cross_section_room_temperature quasimonochromatic resonance_shape scattering_01 scattering_001 scattering_03 scattering_005 scattering_single_0_001 scattering_single_1_001 scattering_single_2_001 transmission_01 transmission_001 transmission_03 transmission_005 transmission_alternative_001))

FIGURES_DIR=figures/
FIGURES=$(addprefix ${FIGURES_DIR}, dhips.pdf neutron_star_merger.jpg prism.jpg se82_spectrum_branchings.pdf)

${PROJECT}.pdf: ${PROJECT}.tex ${LATEX_SOURCE} ${PYTHON_FIGURES} ${FIGURES}
	${LATEX} ${PROJECT}
	${LATEX} ${PROJECT}

${PYTHON_FIGURES}: ${PYTHON_SOURCE}
	${PYTHON} ${PYTHON_SOURCE_DIR}bremsstrahlung_spectrum.py
	${PYTHON} ${PYTHON_SOURCE_DIR}circular_aperture_diffraction.py
	${PYTHON} ${PYTHON_SOURCE_DIR}doppler_broadening.py
	${PYTHON} ${PYTHON_SOURCE_DIR}quasimonochromatic_spectrum.py
	${PYTHON} ${PYTHON_SOURCE_DIR}resolution.py
	${PYTHON} ${PYTHON_SOURCE_DIR}resonance_shape.py

clean:
	rm -f ${LATEX_OUTPUT}
	rm -f ${PYTHON_FIGURES_DIR}*
	rm -rf ${PYTHON_SOURCE_DIR}__pycache__
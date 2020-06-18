LATEX=pdflatex

PROJECT=nrf_seminar
LATEX_SOURCE_DIR=source/
LATEX_SOURCE=$(addprefix ${LATEX_SOURCE_DIR}, $(addsuffix .tex, doppler_broadening footer resonance_fluorescence resonance_fluorescence_atom resonance_fluorescence_nucleus scattering title))
LATEX_OUTPUT=$(addprefix ${PROJECT}, .aux .log .nav .out .pdf .snm .toc)

PYTHON=python
PYTHON_SOURCE_DIR=python/
PYTHON_SOURCE=$(addprefix ${PYTHON_SOURCE_DIR}, $(addsuffix .py, circular_aperture_diffraction doppler_broadening nrf_cross_section resonance_shape))
PYTHON_FIGURES_DIR=figures/python/
PYTHON_FIGURES=$(addprefix ${PYTHON_FIGURES_DIR}, $(addsuffix .pdf, circular_aperture_one_tenth circular_aperture_one circular_aperture_ten cross_section_absolute_zero cross_section_ln2 cross_section_room_temperature resonance_shape))

FIGURES_DIR=figures/
FIGURES=$(addprefix ${FIGURES_DIR}, crystal_resonance.pdf gammasphere.jpg prism.jpg th229m.pdf)

${PROJECT}.pdf: ${PROJECT}.tex ${LATEX_SOURCE} ${PYTHON_FIGURES} ${FIGURES}
	${LATEX} ${PROJECT}
	${LATEX} ${PROJECT}

${PYTHON_FIGURES}: ${PYTHON_SOURCE}
	${PYTHON} ${PYTHON_SOURCE_DIR}circular_aperture_diffraction.py
	${PYTHON} ${PYTHON_SOURCE_DIR}doppler_broadening.py
	${PYTHON} ${PYTHON_SOURCE_DIR}resonance_shape.py

clean:
	rm -f ${LATEX_OUTPUT}
	rm -f ${PYTHON_FIGURES}
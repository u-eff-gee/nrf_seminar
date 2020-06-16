LATEX=pdflatex

PROJECT=nrf_seminar
LATEX_SOURCE_DIR=source/
LATEX_SOURCE=$(addprefix ${LATEX_SOURCE_DIR}, $(addsuffix .tex, footer scattering title))
LATEX_OUTPUT=$(addprefix ${PROJECT}, .aux .log .nav .out .pdf .snm .toc)

PYTHON=python
PYTHON_SOURCE_DIR=python/
PYTHON_SOURCE=$(addprefix ${PYTHON_SOURCE_DIR}, $(addsuffix .py, circular_aperture_diffraction))
PYTHON_FIGURES_DIR=figures/python/
PYTHON_FIGURES=$(addprefix ${PYTHON_FIGURES_DIR}, $(addsuffix .pdf, circular_aperture_one_tenth circular_aperture_one circular_aperture_ten))

${PROJECT}.pdf: ${PROJECT}.tex ${LATEX_SOURCE} ${PYTHON_FIGURES}
	${LATEX} ${PROJECT}
	${LATEX} ${PROJECT}

${PYTHON_FIGURES}: ${PYTHON_SOURCE}
	${PYTHON} ${PYTHON_SOURCE_DIR}circular_aperture_diffraction.py

clean:
	rm -f ${LATEX_OUTPUT}
	rm -f ${PYTHON_FIGURES}
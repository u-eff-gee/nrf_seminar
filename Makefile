LATEX=pdflatex

PROJECT=nrf_seminar
LATEX_SOURCE_DIR=source/
LATEX_SOURCE=$(addprefix ${LATEX_SOURCE_DIR}, $(addsuffix .tex, footer scattering title))
LATEX_OUTPUT=$(addprefix ${PROJECT}, .aux .log .nav .out .pdf .snm .toc)

${PROJECT}.pdf: ${PROJECT}.tex ${LATEX_SOURCE}
	${LATEX} ${PROJECT}
	${LATEX} ${PROJECT}

clean:
	rm -f ${LATEX_OUTPUT}
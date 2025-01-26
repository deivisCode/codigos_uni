.DEFAULT_GOAL := rula

rula: documento.tex
	latexmk documento.tex

limpa:
	latexmk -C
	latexmk -norc -C
	rm -rf .out .aux

.PHONY: rula limpa

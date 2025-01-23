.DEFAULT_GOAL := rula

rula: documento.tex
	latexmk documento.tex

limpa:
	latexmk -C
	rm -rf .out .aux

.PHONY: rula limpa

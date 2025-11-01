SHELL := bash
.DEFAULT_GOAL := memoria.pdf
.PHONY: limpa

# Opcions para compilar
OPCIONS := \
	--format pdf              \
	--root .                  \
	--pdf-standard 2.0,a-4f   \
	--diagnostic-format short \

datos.csv: analise.jl
	julia analise.jl

memoria.pdf: datos.csv memoria.typ funcions.typ estilo.typ
	typst compile $(OPCIONS) memoria.typ

limpa:
	rm -rf datos.csv memoria.pdf

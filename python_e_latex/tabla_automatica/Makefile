
.DEFAULT_GOAL := rula

PYTHON = .\venv\Scripts\python

venv: requirements.txt
	python -m venv venv
	.\venv\Scripts\activate
	$(PYTHON) -m pip install -r requirements.txt

rula: venv
	$(PYTHON) test.py
	latexmk -synctex=0 -file-line-error -shell-escape -pdf test.tex
	latexmk -c

limpar:
	pwsh -Command Remove-Item -Recurse -Force -Path "./venv"
	latexmk -C

.PHONY: venv rula limpar

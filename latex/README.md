Estas son algunhas cousas que uso habitualmente con LaTeX

## apuntes.sty

Un arquivo de estilo para latex que se pode cargar con \usepackage{apuntes}.
Debería funcionar correctamente para as clases de 'book' e 'article', con
pequenas diferencias nos formatos (concretamente nos encabezados). É un estilo
que estou usando eu cos meus propios apuntes. Inclúe: soporte para galego
(babel, csquotes), bibliografía (biblatex), matemáticas (mathtools, amssymb,
amsthm, esint, diffcoeff, etc.), estilos para definicións e teoremas con cores
(tcolorbox), unidades (siunitx), encabezados chulos (fancyhdr), indice
(makeidx), e outras cousas varias.

## memoria.cls

Unha clase completa para memoria. Cárgase con \documentclass{memoria}. Está
bastante completa igual que o arquivo 'apuntes.sty' pero está centrado a unhas
memorias básicas. Inclúe soporte para cargar datos con datatool, pero non
inclúe cousas como teoremas, definicións, etc.

## config.rsc

Configuración para usar bibtool. Esta é unha ferramenta que permite formatear
os arquivos *.bib. Véxase https://www.ctan.org/pkg/bibtool

## latexmkrc

Configuración para latemk. Porque non me apetece escribir un comando larguísimo
na terminal cada vez

## Makefile

Porque incluso escribir 'latexmk documento.tex' me é cansino. Así pódese
facer 'make' e pista. Tamén 'make limpa' para borrar todos os arquivos xerados.

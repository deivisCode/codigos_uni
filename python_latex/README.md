## Datos directamente a LaTeX

De vez en cando ao facer memorias de laboratorio en LaTeX atopámonos
reescribindo os mesmos datos unha e outra vez a medida que imos cambiando a
análise de datos en paralelo. Por exemplo, supoñamos a práctica da balanza de
torsión do laboratorio de mecánica de segundo. Un dato que debemos obter é a
constante G. Na nosa memoria podemos escribir directamente

```latex
\documentclass{article}

\begin{document}

A constante da gravitación univeral vale 59 

\end{document}
```

Tal vez, ao refacer o análise vos decatades de que non usastes as incertezas
correctas (as incertezas soen dar polo cu), polo que tendes que volver ao
arquivo de latex, buscar o numeriño e cambialo. Logo vedes que o análise estaba
mal e estábades usando `absolute_error=False` con `scipy.optimize`. Toca volver
cambialas no documento. Logo resulta que volvedes cambiar de idea cas
incertezas. Logo que non vos da ben asique preferides manipular un par de datos
(dios me libre) e repetilo. Etcétera. É máis sinxelo que o numeriño se
actualice automáticamente.

A idea é esa, 'cargar' directamente datos a latex para non ter que facelo a
man. Podemos facer eso gardando automáticamente os datos que nos interesan nun
arquivo e formato específicos, e logo lendo dito arquivo dende latex para chamar
o dato concreto.

O arquivo test.py so ten a definicion dunha funcion que garda un dato no formato
requerido, pero non é un arquivo necesario, o importante é ter os datos 
nun formato tipo

```
constante_G,59
```
Se temos o mesmo preámbulo que no arquivo `test.tex` podemos facer simplemente
```latex
\begin{document}

A constante da gravitación universal vale \var{constante_G}

\end{document}
```
E o valor actualizarase automáticamente.

## LIMITACIONS

Non sei como facer que esto furrule con unidades, so sei que funciona con
numeros a pelo tipo 230 ou 0.000000000000000000000000021. Se alguén ten idea,
sobre todo se se pode compaxinar con `siuntix`, que mo diga

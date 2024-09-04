## Datos directamente a LaTeX


A idea desto é poder gardar diversos datos da nosa análise a un arquivo de
'resultados', e leelos directamente desde LaTeX
```
┌──────────┐       ┌──────────────┐      ┌─────────────┐
│analise.py├──────►│resultados.csv├─────►│documento.tex│
└──────────┘       └──────────────┘      └─────────────┘
```
A motivación é que desta forma aforrámonos ter que re-escribir a man
constantemente os datos (cas correspontentes e engorrosas unidades) cada vez
que re-executamos a análise e obtemos resultados novos (por exemplo, se
cambiamos de idea nas incertezas que usamos). É mellor que os datos se cambien
soliños. 

No documento de LaTeX, en vez de escribir

```latex
\begin{document}

A constante da gravitación univeral vale $(59 \pm 0.2) m / s$

\end{document}
```
Podemos facer simplemente
```latex
\begin{document}

A constante da gravitación universal vale \cantidade{variable_G}

\end{document}
```
E o valor actualizarase automáticamente.

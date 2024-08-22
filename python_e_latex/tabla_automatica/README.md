# CSV -> Pandas dataframe -> tabla de LaTeX

Convirte datos tipo CSV a unha tabla bonita de LaTeX usando
[pandas](https://pandas.pydata.org/docs/reference/index.html#api)

Tendo estos datos:
```csv
voltaxe,intensidade
1,6
1,2
2,3
2,4
```
xeramos esta tabla automáticamente:
```latex
\begin{table}[H]
\centering
\caption{Tabla feita con Python e Pandas}
\label{tab:Tabla bonita}
\begin{tabular}{rr}
\toprule
voltaxe & intensidade \\
\midrule
1 & 6 \\
1 & 2 \\
2 & 3 \\
2 & 4 \\
\bottomrule
\end{tabular}
\end{table}
```
## Instalación das dependencias

### Método Recomendado
no directorio onde están os arquivos:
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### Coa Makefile (só windows, e non prometo que funcione)
```
make # para rulalo todo
make limpar # para eliminar os arquivos xerados
```
### Miña setup
- Microsoft Windows NT 10.0.19045.0
- Powershell 7.4.3
- Python 3.11.3
- [Make](https://www.gnu.org/software/make/manual/make.html) 4.4.1, instalado con [scoop](https://scoop.sh/)
- Latexmk 4.85, instalado con MikTex


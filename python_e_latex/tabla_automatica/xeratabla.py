import pandas as pd

# Esto son uns datos de proba. Neste caso colloos dun arquivo *.csv, pero poden
# vir doutro sitio, como dunha matriz rectangular de numpy
datos = pd.read_csv(
    "datos.csv",
    header = 0 # qué fila usar pos nomes das columnas
)

# Os nomes das columnas serán os do arquivo .csv Podemos melloralos un pouco
# facendo o seguinte para engadirlle as unidades correctas, nun formato que o
# paquete de LaTeX siunitx poderá 'parsear' para deixalas deliciosas. Esto
# facémolo usando o paquete 'siunitx' en latex
datos.columns = [
    datos.columns[0] + " [\\unit{\\volt}]",
    datos.columns[1] + " [\\unit{\\ampere}]",
] # OLLO: esta parte non era necesaria, pero queda ben bonita

# esto e un cristo e a documentacion oficial tamén
with open(r"tabla.tex",'w') as ficheiro:
    # escribir, facilillo
    ficheiro.write(
        # usar o método 'style'. Os desarrolladores din que usar directamente
        # 'datos.to_latex()' vai a quedar obsoleto, e que se debe usar
        # 'datos.style.to_latex()'. A cousa e que os parámetros que aceptan
        # eses dous 'to_latex' non son iguales. No primeiro caso, podíase
        # incluir 'no_index' pa que non se mostrase a columna de índices da
        # tabla, pero usando 'style.to_latex()' non se pode. Entonces, pa que
        # non se mostre a columna cos índices, hai que concatenar 'hide()'
        # antes, é dicir: datos.style.hide(*args).to_latex(*args)
        datos.style.hide(axis="index").to_latex(
            position_float = "centering", # pa que meta un \centering por ahí
            position = "H", # pa que quede no sitio (necesita paquete 'float')
            label = "tab:Tabla bonita", # label e caption largo e corto
            # ollo, tildes e esas cousas téñense que escapar con \
            caption = (r"Esta tabla foi xerada automaticamente con python",r"Tabla feita con python" ),
            hrules = True, # liñas horizontais bonicas (necesita paquete 'booktabs')
            siunitx = True # Usar tabla estilo siunitx (necesita paquete 'siunitx')
        )
    )

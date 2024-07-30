import pandas as pd

datos = pd.read_csv(
    "datos.csv",
    header = 0 # qué fila usar pos nomes das columnas
)

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
            caption = (r"Esta tabla foi feita nin mais nin menos que co noso querid\'isimo leitek",r"Tabla feita con latex" ),
            hrules = True, # liñas horizontais bonicas (necesita paquete 'booktabs')
        )
    )

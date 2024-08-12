
import numpy as np
import matplotlib.pyplot as plt
from analise import xerador_van_der_waals



datos = [
    np.loadtxt(r"resultados\serie_1_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_2_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_3_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_4_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_5_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_6_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_7_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_8_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_9_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_10_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_11_presion_volumen.txt"),
    np.loadtxt(r"resultados\serie_12_presion_volumen.txt"),
]

# columna 0: a
# columna 1: b
# columna 2: s(a)
# columna 3: s(b)
parametros = np.loadtxt(r"resultados\axuste_vdw.txt")
temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")
moles = np.loadtxt(r"resultados\moles.txt")

ventana = plt.figure(
    num     = "Axustes de Van der Waals",
    figsize = (8,9),
)

# hai que meter 12 axustes.
lenzos = ventana.subplots(
    nrows = 4,
    ncols = 3,
    sharex = True,
    sharey = True
)

for i in range(len(datos)):

    # i//3 = 0 0 0 1 1 1 2 2 2 3 3 3
    # i%3  = 0 1 2 0 1 2 0 1 2 0 1 2
    lenzo = lenzos[i // 3, i % 3]

    lenzo.plot(
        datos[i][0]/moles[0],
        datos[i][1],
        color = "red",
        marker = '.'
    )

    # para as rectas, necesitamos valores x
    coord_x_curvas = np.linspace(
        min(datos[i][0] / moles[0]),
        max(datos[i][0] / moles[0])
    )
    coord_y_curvas = xerador_van_der_waals(temperaturas[i])(
        coord_x_curvas, 
        parametros[i][0],
        parametros[i][1]
    )

    lenzo.plot(
        coord_x_curvas,
        coord_y_curvas,
        color = "gray",
        marker = '',
        linestyle = '-'
    )

    lenzo.set(title=f"{temperaturas[i]} K")
    if i%3 == 0:
        lenzo.set(ylabel = r"Presión, Pa")
    if i//3 == 3:
        lenzo.set(xlabel = "Volume m$^3$/mol")

plt.show()

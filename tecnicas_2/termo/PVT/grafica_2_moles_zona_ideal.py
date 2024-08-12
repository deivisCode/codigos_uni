import numpy as np
import matplotlib.pyplot as plt

datos = [
    np.loadtxt(r"resultados\serie_1_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_2_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_3_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_4_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_5_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_6_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_7_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_8_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_9_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_10_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_11_presion_volumen_ideal.txt"),
    np.loadtxt(r"resultados\serie_12_presion_volumen_ideal.txt"),
]

temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")
R = 8.31446261815324  # J / mol K

regresions_moles = np.loadtxt(r"resultados\regresions_moles.txt")

# primeiro creo unha ventana normal
ventana = plt.figure(
    num     = "Figura comportamento ideal",
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

    coord_x = (1 / datos[i][0]) * R * temperaturas[i] # RT/V
    coord_y = datos[i][1]

    # para as rectas, necesitamos valores x
    coord_x_rectas = np.array([min(coord_x),max(coord_x)])

    lenzo.plot(
        coord_x_rectas,
        coord_x_rectas * regresions_moles[i][2] + regresions_moles[i][0],
        #    X         *   pendente (moles)    +  ordenada 
        linestyle = '-',
        marker = '',
        color = 'black'
    ) 

    # E os puntos
    lenzo.plot(
        coord_x,  
        coord_y,
    )
    lenzo.set(title=f"{temperaturas[i]} K")

plt.show()

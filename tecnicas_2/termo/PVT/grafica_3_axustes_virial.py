
import numpy as np
import matplotlib.pyplot as plt

datos_x = np.loadtxt(r"resultados\virial_x.txt")
datos_y = np.loadtxt(r"resultados\virial_y.txt")
incertezas_y = np.loadtxt(r"resultados\incertezas_virial_y.txt")
regresions = np.loadtxt(r"resultados\regresions_virial.txt")

ventana = plt.figure(
    num     = "Figura axustes virial",
    figsize = (8,9),
)


temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")
R = 8.31446261815324  # J / mol K

# hai que meter 12 axustes.
lenzos = ventana.subplots(
    nrows = 4,
    ncols = 3,
    sharex = True,
    sharey = True
)

for i in range(len(datos_x)):
    # i//3 = 0 0 0 1 1 1 2 2 2 3 3 3
    # i%3  = 0 1 2 0 1 2 0 1 2 0 1 2
    lenzo = lenzos[i // 3, i % 3]
    lenzo.errorbar(
        datos_x[i],
        datos_y[i],
        incertezas_y[i],
        marker = '.',
        color = 'red',
        ecolor = 'black'
    )
    coord_x_rectas = np.array([min(datos_x[i]),max(datos_x[i])])
    lenzo.plot(
        coord_x_rectas,
        coord_x_rectas * regresions[i][2] + regresions[i][0],
        #    X         *   pendente     +  ordenada 
        linestyle = '-',
        marker = '',
        color = 'grey'
    )
    lenzo.set(
        title = f"{temperaturas[i]} K",
    )
    if i%3 == 0:
        lenzo.set(ylabel = r"$\frac{PV}{RT}-1$")
    if i//3 == 3:
        lenzo.set(xlabel = r"$\frac{1}{v}$")

plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Como sempre, empezamos cargando os datos. Neste caso temos directamente
# valores x e y pa graficar. 'datos_x/y' son 12 arrays (series) de 16 datos
# cada un, correspondentes aos 16 valores que había na zona ideal. Véxase o
# arquivo principal 'analise.py' para máis detalles
datos_x = np.loadtxt(r"resultados\virial_x.txt") # 1/v
datos_y = np.loadtxt(r"resultados\virial_y.txt") # P * v / R * T - 1
incertezas_y = np.loadtxt(r"resultados\incertezas_virial_y.txt")
regresions = np.loadtxt(r"resultados\regresions_virial.txt")

temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")
R = 8.31446261815324  # J / mol K


# Toca graficar
ventana = plt.figure(
    num     = "Figura axustes virial",
    figsize = (8,9),
)


# hai que meter 12 axustes como na grafica anterior
lenzos = ventana.subplots(
    nrows = 4,
    ncols = 3,
    sharex = True,
    sharey = True
)

# Esto usa o truco dos restos da gráfica 2, aló está explicado. A única
# diferencia é que aquí uso tamén 'errorbar'
for i in range(len(datos_x)):
    # i//3 = 0 0 0 1 1 1 2 2 2 3 3 3
    # i%3  = 0 1 2 0 1 2 0 1 2 0 1 2
    lenzo = lenzos[i // 3, i % 3]

    # primeiro graficamos os 16 datos da serie, cas incertezas correspondentes
    lenzo.errorbar(
        datos_x[i], # 1/v               
        datos_y[i], # P * v / R * T - 1 
        incertezas_y[i], # incerteza en y
        marker = '.',
        color = 'red',
        ecolor = 'black'
    )

    # agora as rectas de regresión. Fan falta 2 puntos (minimo). Collo o máximo
    # e o minimo dos datos x experimentales (podense coller outros) e
    # multiplícoos pola pendente e súmolles a ordenada
    coord_x_rectas = np.array([min(datos_x[i]),max(datos_x[i])])
    lenzo.plot(
        coord_x_rectas,
        coord_x_rectas * regresions[i][2] + regresions[i][0],
        #    X         *   pendente     +  ordenada
        linestyle = '-',
        marker = '',
        color = 'grey'
    )

    lenzo.set( title = f"{temperaturas[i]} K" )
    if i%3 == 0:
        lenzo.set(ylabel = r"$\frac{PV}{RT}-1$")
    if i//3 == 3:
        lenzo.set(xlabel = r"$\frac{1}{v}$")

plt.show()

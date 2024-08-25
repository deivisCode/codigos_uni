import pathlib

import numpy as np
import matplotlib.pyplot as plt

# Como sempre, empezamos cargando os datos. Neste caso temos directamente
# valores x e y pa graficar. 'datos_x/y' son 12 arrays (series) cos puntos que
# usamos pa calcular as regresions. Véxase o arquivo 'principal.py' para máis
# detalles
DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

datos_x = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_puntos_x.txt")  # 1/v
datos_y = np.loadtxt( DIRETORIO_PRINCIPAL + "\\resultados\\virial_puntos_y.txt")  # P * v / R * T - 1
incertezas_y = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_incertezas_y.txt")
regresions = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_regresions.txt")

cantas_series = len(datos_x)

temperaturas = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperaturas.txt")
R = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\R.txt")  # J / mol K


# Toca graficar
ventana = plt.figure(
    num     = "Figura axustes virial",
    # figsize = (8,9),
)

# Agora fago o truco da grafica anterior. Non o volvo explicar :)
raiz  = np.sqrt(cantas_series)
techo = np.ceil(raiz)
chan  = np.floor(raiz)

if chan * chan == cantas_series:
    filas = int(chan)
    columnas = int(chan)

elif techo * chan >= cantas_series:
    filas = int(chan)
    columnas = int(techo)

else:
    filas = int(techo)
    columnas = int(techo)

lenzos = ventana.subplots(
    nrows = filas,
    ncols = columnas,
    sharex = True,
    sharey = True
)

for i in range(filas * columnas):

    if i+1 <= cantas_series:

        lenzo = lenzos[i // columnas, i % columnas]

        # primeiro graficamos os datos da serie, cas incertezas correspondentes
        lenzo.errorbar(
            datos_x[i], # 1/v
            datos_y[i], # P * v / R * T - 1
            incertezas_y[i], # incerteza en y
            marker = '.',
            color = 'red',
            ecolor = 'black'
        )

        # agora as rectas de regresión. Fan falta 2 puntos (minimo). Collo o
        # máximo e o minimo dos datos x experimentales (podense coller outros)
        # e multiplícoos pola pendente e súmolles a ordenada
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

        if i % columnas == 0: # Columna 0
            lenzo.set(ylabel = r"PV/RT-1")

        if i // columnas == filas - 1: # ultima fila
            lenzo.set(xlabel = r"1/V")

    elif i+1 > cantas_series:
        lenzos[i // columnas, i % columnas].remove()

plt.show()

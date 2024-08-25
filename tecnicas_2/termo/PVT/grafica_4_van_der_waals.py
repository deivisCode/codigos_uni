import os
import pathlib

import numpy as np
import matplotlib.pyplot as plt
from funcions import xerador_van_der_waals

# Esto é identico á grafica 1
DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

nomes_ficheiros = os.listdir(
    DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI\\"
)
datos = []
for nome in nomes_ficheiros:
    datos.append(
        np.loadtxt(
            DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI\\" + nome,
            unpack=True,  # os datos están por filas
            dtype=np.float64,
        )
    )
cantas_series = len(datos)

# tamén fan falta temperatura e moles
temperaturas = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperaturas.txt")
moles = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\moles_numero.txt") # n, s(n)

# agora os datos dos parámetros. Como recordatorio, teñen esta forma. 12 series
# en total
#
#       a                 b               s(a)           s(b)
# [[ 5.72684379e-01  6.50212212e-05  2.50379583e-04  2.44405568e-08]
#  [ 5.63826019e-01  6.41740311e-05  2.55750623e-04  2.55524003e-08]
#  [ 5.57555888e-01  6.35848329e-05  2.59141022e-04  2.62788015e-08]
#  [ 5.49536432e-01  6.25344818e-05  2.65352592e-04  2.75862606e-08]
#  [ 5.44824850e-01  6.40407648e-05  4.45057616e-04  6.29842378e-08]
#  [ 5.26045129e-01  6.14219598e-05  4.72857673e-04  7.01970654e-08]
#  [ 5.19751236e-01  5.94882576e-05  4.93381804e-04  7.52982440e-08]
#  [ 5.19499864e-01  5.98157237e-05  4.97111577e-04  7.51449856e-08]
#  [ 5.02135384e-01  5.47210440e-05  8.88360577e-04  1.73395473e-07]
#  [ 3.14474474e-01 -2.93604925e-08  2.11296134e+00  8.29918624e-04]
#  [ 3.03528812e-01  8.31609329e-09  1.32958716e+00  5.31555711e-04]
#  [ 2.64412643e-01 -3.19707305e-09  5.05079647e-01  2.01928174e-04]]
parametros = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\vdw_axustes.txt")

ventana = plt.figure(
    num     = "Axustes de Van der Waals",
    figsize = (8,9),
)

# De aquí en adiante é case idéntico ás gráficas anteriores, asique non me
# molesto en explicalo moito
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

        # Ollo, debemos usar volumes molares!! (eu con esto descubrín o que era
        # un 'problema de 3 días' en programación XD) 
        lenzo.plot(
            datos[i][0]/moles[0],
            datos[i][1],
            color = "red",
            marker = '.'
        )

        # para as rectas, necesitamos valores x. Fago o mesmo que nas gráficas
        # anteriores
        coord_x_curvas = np.linspace(
            min(datos[i][0] / moles[0]),
            max(datos[i][0] / moles[0]),
            num = 1000
        )

        # recórdese que nas gráficas anteriores representábamos axustes
        # lineales, collendo os datos x e multiplicándoos pola pendente etc.
        # Neste caso hai que aplicarlle a funcion de Van der Waals. Está
        # documentada no arquivo 'principal.py'
        coord_y_curvas = xerador_van_der_waals(temperaturas[i])(
            coord_x_curvas, 
            parametros[i][0],
            parametros[i][1]
        )

        # e graficamos os puntos x e y da curva
        lenzo.plot(
            coord_x_curvas,
            coord_y_curvas,
            color = "gray",
            marker = '',
            linestyle = '-'
        )

        lenzo.set(title=f"{temperaturas[i]} K")
        if i % columnas == 0: # Columna 0
            lenzo.set(ylabel = r"Presión, Pa")

        if i // columnas == filas - 1: # ultima fila
            lenzo.set(xlabel = "Volume m$^3$/mol")

    elif i+1 > cantas_series:
        lenzos[i // columnas, i % columnas].remove()

plt.show()

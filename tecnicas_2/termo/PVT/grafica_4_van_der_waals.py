
import numpy as np
import matplotlib.pyplot as plt
from analise import xerador_van_der_waals

# estos son  os datos orixinais, nada novo por aquí
datos = [
    np.loadtxt(r"resultados\serie_1_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_2_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_3_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_4_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_5_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_6_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_7_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_8_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_9_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_10_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_11_volumen_presion.txt"),
    np.loadtxt(r"resultados\serie_12_volumen_presion.txt"),
]

# tamén fan falta temperatura e moles
temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")
moles = np.loadtxt(r"resultados\moles.txt") # n, s(n)

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
parametros = np.loadtxt(r"resultados\axuste_vdw.txt")

ventana = plt.figure(
    num     = "Axustes de Van der Waals",
    figsize = (8,9),
)

# De aquí en adiante é case idéntico ás gráficas anteriores, asique non me
# molesto en explicalo moito
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

    # Ollo, debemos usar volumes molares!! (eu con esto descubrín o que era un
    # 'problema de 3 días' en programación XD) 
    lenzo.plot(
        datos[i][0]/moles[0],
        datos[i][1],
        color = "red",
        marker = '.'
    )

    # para as rectas, necesitamos valores x. Fago o mesmo que nas gráficas anteriores
    coord_x_curvas = np.linspace(
        min(datos[i][0] / moles[0]),
        max(datos[i][0] / moles[0]),
        num = 1000
    )

    # recórdese que nas gráficas anteriores representábamos axustes lineales,
    # collendo os datos x e multiplicándoos pola pendente etc. Neste caso hai
    # que aplicarlle a funcion de Van der Waals. Está documentada no arquivo
    # 'analise.py'
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
    if i%3 == 0:
        lenzo.set(ylabel = r"Presión, Pa")
    if i//3 == 3:
        lenzo.set(xlabel = "Volume m$^3$/mol")

plt.show()

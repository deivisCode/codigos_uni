
import numpy as np
import matplotlib.pyplot as plt


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

temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")

campana_entrada = np.loadtxt(           # Estos son os datos na zona limítrofe da
    r"datos\campana_entrada.numpydata", # campana, saqueinos a ollo dos datos e
    unpack = True,                      # das gráficas
    delimiter = ','                     #
)                                       #
v_campana_entrada = campana_entrada[0] / (10 ** 6)
p_campana_entrada = campana_entrada[1] * (10 ** 5)

campana_salida = np.loadtxt(
    r"datos\campana_salida.numpydata",
    unpack = True,
    delimiter = ','
)
v_campana_salida = campana_salida[0] / (10 ** 6)
p_campana_salida = campana_salida[1] * (10 ** 5)


ventana = plt.figure( num="Zona de coexistencia")

lenzo = ventana.add_subplot()

for i in range(len(v_campana_entrada)):

    lenzo.plot(
        datos[i][0],
        datos[i][1],
        # color = "gray",
        marker = '.',
        linestyle = '--',
        alpha = 0.3,
        label = f"{temperaturas[i]} K"
    )

for i in range(len(v_campana_entrada)):
    puntos = lenzo.plot(
        [v_campana_entrada[i],v_campana_salida[i]],
        [p_campana_entrada[i],p_campana_salida[i]],
        marker          = 'o',
        markeredgecolor = "black",
        color           = "red",
        linestyle = '-',
    )

lenzo.set_xlabel("Volumes m$^3$", fontsize = 11)
lenzo.set_ylabel("Presións Pa", fontsize = 11)

lenda_secundaria = lenzo.legend(puntos,["Puntos entrada e saida"],loc="lower left")
lenzo.add_artist(lenda_secundaria)
lenzo.legend()

plt.show()



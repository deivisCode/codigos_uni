
import numpy as np
import matplotlib.pyplot as plt


# estos son  os datos orixinais outra vez, nada novo por aquí
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

temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")

# O complicado do asunto son os valores de entrada e de salida. O que se pode
# facer é graficalos todos (programa grafica_1_**.py), e na propia gráfica ir
# vendo por onde tan. Automatizalo paréceme nada fiable. Eu o que fixen foi
# apuntar 2 ficheiros de datos, cada unha con valores de volumen (mL) e presión
# (bar). Un ficheiro son os pares PV do lado de entrada, e o outro os de
# salida. Seguramente se poida facer doutro modo, eu fixeno así porque quería
# ter separados os datos de cada lado, porque para outra parte fan falta os
# puntos medios de ambos
campana_entrada = np.loadtxt(
    r"datos\campana_entrada.numpydata",
    unpack = True, # esto porque os tomei por filas
    delimiter = ','
)
v_campana_entrada = campana_entrada[0] / (10 ** 6) # hai que pasalo ao SI
p_campana_entrada = campana_entrada[1] * (10 ** 5)

campana_salida = np.loadtxt(
    r"datos\campana_salida.numpydata",
    unpack = True,
    delimiter = ','
)
v_campana_salida = campana_salida[0] / (10 ** 6)
p_campana_salida = campana_salida[1] * (10 ** 5)


ventana = plt.figure( num="Zona de coexistencia" )

lenzo = ventana.add_subplot()

for i in range(len(v_campana_entrada)):

    # primeiro os datos experimentales
    lenzo.plot(
        datos[i][0],
        datos[i][1],
        marker = '.',
        linestyle = '--',
        alpha = 0.3,
        label = f"{temperaturas[i]} K"
    )

    # e logo os puntos de entrada e salida. Fixarse como neste caso instancio o
    # obxeto .plot(...). Esto é porque despois vou poñer varias lendas, asique
    # necesitarei referenciar este obxeto
    puntos = lenzo.plot(
        [v_campana_entrada[i],v_campana_salida[i]], # coord x dos dous puntos
        [p_campana_entrada[i],p_campana_salida[i]], # coord y dos dous puntos
        marker          = 'o',
        markeredgecolor = "black",
        color           = "red",
        linestyle = '-',
    )


lenzo.set_xlabel("Volumes m$^3$", fontsize = 11)
lenzo.set_ylabel("Presións Pa", fontsize = 11)

# O de facer varias lendas é un lio pero bueno. Creo outra lenda, asociada aos
# puntos de entrada e salida
lenda_secundaria = lenzo.legend(puntos,["Puntos entrada e saida"],loc="lower left")
# e engádoa ao lenzo
lenzo.add_artist(lenda_secundaria)

# e con esto mostro a principal
lenzo.legend(title="Temperaturas")

plt.show()

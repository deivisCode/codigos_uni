
import numpy as np
import matplotlib.pyplot as plt

# Primeiro cargamos os datos. Son necesarios os valores de presións e volumes
# no sistema internacional. Podería cargar directamente os datos crus, ou usar
# estes que veñen do arquivo 'analise.py'
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

# E tamén cargo as temperaturas
temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")

# A gráfica é sinxela, primeiro creamos unha ventana normalmente
ventana = plt.figure()

# E dous lenzos onde pintar
lenzo_1 = ventana.add_subplot(1,2,1,
    xlabel = "Volumen  m$^3$",
    ylabel = "Presión  Pa",
    title  = "Datos día 1"
)
lenzo_2 = ventana.add_subplot(1,2,2,
    xlabel = "Volumen  m$^3$",
    title  = "Datos día 2"
)

# Os datos PVT obtivémolos en dous días diferentes. Esto afectou ao análise de
# datos e fai que as curvas do segundo día se solapen demasiado cas da
# primeira. A solución (no tema gráfico), é colocar as series de datos
# separadas. É moi sinxelo. Sei que quero poñer 6 series nuha gráfica e o resto
# na outra, asique vou contando cantas van e ao pasar de 6 pasamos a graficar
# nun lenzo diferente. Evidentemente se os datos fosen diferentes habería que
# cambiar o numeriño (tal vez que sexan 8 gráficas nun, e 2 noutro, etc.). O de
# zip(...) usoo porque é extraordinariamente cómodo (de feito, no linguaxe Lua
# é a forma estandar de iterar) cando hai que iterar por duas listas. Outra
# opción seria iterar con índices, é dicir, temperatura[i] e serie[i], pero
# prefiero iterar polos elementos e usar o índice solo para saber en qué lenzo
# hai que pintar
indice = 0
for temperatura, serie in zip(temperaturas,datos):

    if indice < 7: # Aquí imos pintando no primeiro lenzo
        lenzo_1.plot(serie[0],serie[1],label=f"{temperatura} K")

    else: # e aquí no segundo
        lenzo_2.plot(serie[0],serie[1],label=f"{temperatura} K")

    indice = indice + 1

# Nota. Fixarse qué facil é usar f-strings para ir cambiandolle o nome ás lendas!

lenzo_1.legend(title="Temperaturas",fontsize=12)
lenzo_2.legend(title="Temperaturas",fontsize=12)
    
plt.show()

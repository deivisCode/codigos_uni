
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

ventana = plt.figure()

lenzo_1 = ventana.add_subplot(1,2,1,
    xlabel = "Volumen  m$^3$",
    ylabel = "Presión  Pa",
    title  = "Datos día 1"
)
lenzo_2 = ventana.add_subplot(1,2,2,
    xlabel = "Volumen  m$^3$",
    title  = "Datos día 1"
)


indice = 0
for temperatura, serie in zip(temperaturas,datos):

    if indice < 7:
        lenzo_1.plot(serie[0],serie[1],label=f"{temperatura} K")
    else:
        lenzo_2.plot(serie[0],serie[1],label=f"{temperatura} K")
    indice = indice + 1

lenzo_1.legend(title="Temperaturas",fontsize=12)
lenzo_2.legend(title="Temperaturas",fontsize=12)
    
plt.show()

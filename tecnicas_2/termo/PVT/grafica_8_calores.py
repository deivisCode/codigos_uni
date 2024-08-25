import pathlib

import numpy as np
import matplotlib.pyplot as plt

import funcions

DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

temperaturas = np.loadtxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\campana_temperaturas.txt"
)
calores = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\calores.txt")
incerteza_calores = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\calores_incerteza.txt")
axustes = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\calores_regresions.txt")

ventana = plt.figure()
lenzo = ventana.add_subplot(1,1,1)

lenzo.set_xlim(280,315)
lenzo.errorbar(
    temperaturas,
    calores,
    yerr      = incerteza_calores,
    capsize   = 2,
    ecolor    = "gray",
    elinewidth = 1,
    linestyle = '',
    marker    = 'd',
    color     = "#ff9e19",
    label     = "Calores"
)

x = np.linspace(min(temperaturas),max(temperaturas)+5,2)
y = x * axustes[0] + axustes[1] # y = mx + n
lenzo.plot(
    x, y, color="black", marker="", linestyle="-", label="Axuste lineal", alpha=0.8
)

lenzo.set(xlabel="Temperaturas (K)", ylabel="Calores (J/kg)")

plt.legend()
plt.show()

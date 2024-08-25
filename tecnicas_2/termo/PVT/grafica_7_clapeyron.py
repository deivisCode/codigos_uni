import pathlib

import numpy as np
import matplotlib.pyplot as plt

import funcions

DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

axustes = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\clapeyron_regresions.txt")
temperaturas = np.loadtxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\campana_temperaturas.txt"
)
p_campana_entrada = funcions.bar_a_pascal(
    np.loadtxt(
        DIRETORIO_PRINCIPAL + "\\datos\\campana_entrada.txt", unpack=True, delimiter=","
    )[1]
)

ventana = plt.figure()
lenzo = ventana.add_subplot(1,1,1)

x = np.linspace(min(temperaturas),max(temperaturas),2)
y = x * axustes[0] + axustes[1] # y = mx + n

lenzo.plot(x, y, color="gray", label="Axuste lineal", marker="", linestyle="-")
lenzo.plot(
    temperaturas,
    p_campana_entrada,
    marker    = 'd',
    linestyle = '',
    color     = "red",
    label     = "Presións na entrada"
)

lenzo.set(xlabel="Temperaturas (K)", ylabel="Presións (Pa)")

plt.legend()
plt.show()

import pathlib

import numpy as np
import matplotlib.pyplot as plt
from funcions import pol_cuadrado

# o de cargar os datos é o mesmo de sempre
DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

densidades_entrada = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\densidades_entrada.txt")
densidades_salida = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\densidades_salida.txt")
densidades_coeficientes = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\densidades_coeficientes.txt")
densidades_regresion = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\densidades_regresion.txt")
densidades_mitad  = np.loadtxt(DIRETORIO_PRINCIPAL + "\\resultados\\densidades_mitad.txt")

temperaturas  = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperaturas.txt")
temperatura_critica  = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperatura_critica.txt")


ventana_densidades = plt.figure("densidades",figsize=(6,6),dpi=150)
lenzo  = ventana_densidades.add_subplot(1,1,1)

lenzo.set_ylabel("Temperaturas K", fontsize = 11)
lenzo.set_xlabel(r"$\rho\ \frac{kg}{m^3}$", fontsize = 11)

# estos son os os puntos da zona de entrada
lenzo.errorbar(
    densidades_entrada[0],
    temperaturas[temperaturas<=temperatura_critica],
    xerr            = densidades_entrada[1],
    linestyle       = '',
    marker          = 'o',
    markeredgecolor = "black",
    color           = "green",
    ecolor          = "gray",
    capsize         = 2,
    label = "Densidades zona da entrada"
)

# estos son os os puntos da zona de salida
lenzo.errorbar(
    densidades_salida[0],
    temperaturas[temperaturas<=temperatura_critica],
    xerr            = densidades_salida[1],
    linestyle       = '',
    marker          = 'o',
    markeredgecolor = "black",
    color           = "blue",
    ecolor          = "gray",
    capsize         = 2,
    label = "Densidades zona da salida"
)

# os puntos medios
lenzo.errorbar(
    densidades_mitad[0],
    temperaturas[temperaturas<304.55],
    xerr            = densidades_mitad[1],
    linestyle       = '',
    marker          = 'd',
    markeredgecolor = "black",
    color           = "orange",
    ecolor          = "gray",
    capsize         = 2,
    label = "Densidades medias"
)

# puntos x para calcular o noso polinomio
x_densidades_polinomio = np.linspace(
    min(densidades_entrada[0]),
    max(densidades_salida[0]),
    num=100
)

# os puntos y correspondentes
y_densidades_polinomio = pol_cuadrado(
    x_densidades_polinomio,
    densidades_coeficientes[0],
    densidades_coeficientes[1],
    densidades_coeficientes[2]
)

lenzo.plot(
    x_densidades_polinomio,
    y_densidades_polinomio,
    linestyle="-",
    marker="",
    label="Axuste Cuadrático",
)

# puntos x para a regresion lineal dos puntos medios
x_densidades_regresion = np.linspace(
    densidades_mitad[0][0],
    densidades_mitad[0][-1],
    num=100
)[10:-40] # OLLO, ESTO DE AQUí IGUAL HAI QUE AXUSTALO

# puntos y correspondentes
y_densidades_regresion = (
    x_densidades_regresion - densidades_regresion[1]
) / densidades_regresion[0]

lenzo.plot(
    x_densidades_regresion,
    y_densidades_regresion,
    linestyle="-",
    marker="",
    color="red",
    label = "Axuste lineal"
)

lenzo.legend()
plt.show()

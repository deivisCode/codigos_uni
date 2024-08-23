import numpy as np
import matplotlib.pyplot as plt
from analise import pol_cuadrado

densidades_entrada = np.loadtxt(r"resultados\densidades_entrada.txt")
densidades_salida = np.loadtxt(r"resultados\densidades_salida.txt")
densidades_coeficientes = np.loadtxt(r"resultados\densidades_coeficientes.txt")
densidades_regresion = np.loadtxt(r"resultados\densidades_regresion.txt")
suma_densidades = np.loadtxt(r"resultados\densidades_suma.txt")
temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")

ventana_densidades = plt.figure("densidades",figsize=(6,6),dpi=150)

lenzo  = ventana_densidades.add_subplot(1,1,1)

lenzo.set_ylabel("Temperaturas K", fontsize = 11)
lenzo.set_xlabel(r"$\rho\ \frac{kg}{m^3}$", fontsize = 11)

lenzo.errorbar(
    densidades_entrada[0],
    temperaturas[temperaturas<304.55],
    xerr            = densidades_entrada[1],
    linestyle       = '',
    marker          = 'o',
    markeredgecolor = "black",
    color           = "green",
    ecolor          = "gray",
    capsize         = 2,
    label = "Densidades zona da entrada"
)
lenzo.errorbar(
    densidades_salida[0],
    temperaturas[temperaturas<304.55],
    xerr            = densidades_salida[1],
    linestyle       = '',
    marker          = 'o',
    markeredgecolor = "black",
    color           = "blue",
    ecolor          = "gray",
    capsize         = 2,
    label = "Densidades zona da entrada"
)


lenzo.errorbar(
    suma_densidades[0],
    temperaturas[temperaturas<304.55],
    xerr            = suma_densidades[1],
    linestyle       = '',
    marker          = 'd',
    markeredgecolor = "black",
    color           = "orange",
    ecolor          = "gray",
    capsize         = 2,
    label = "Densidades medias"
)

x_densidades_polinomio = np.linspace(
    min(densidades_entrada[0]),
    max(densidades_salida[0]),
    num=100
)

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

x_densidades_regresion = np.linspace(
    suma_densidades[0][0],
    suma_densidades[0][-1],
    num=100
)[10:-40]

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

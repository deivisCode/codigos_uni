import numpy as np
import matplotlib.pyplot as plt

# Os datos necesarios neste caso son os de P V e T na 'zona ideal'. Sería
# totalmente factible cargar aquí os orixinais e logo reducilos á zona de
# interés, pero prefiero usar os que xa 'recortei' no outro programa
# (analise.py)
datos = [
    np.loadtxt(r"resultados\serie_1_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_2_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_3_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_4_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_5_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_6_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_7_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_8_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_9_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_10_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_11_volumen_presion_ideal.txt"),
    np.loadtxt(r"resultados\serie_12_volumen_presion_ideal.txt"),
]

# Tamén necesitamos as temperaturas, e a constante R
temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")
R = 8.31446261815324  # J / mol K

# E evidentemente, os valores das pendentes e ordenadas (vamos, as regresións)
regresions_moles = np.loadtxt(r"resultados\regresions_moles.txt")

# primeiro creo unha ventana normal
ventana = plt.figure(
    num     = "Figura comportamento ideal",
    figsize = (8,9),
)

# hai que meter 12 axustes, asique monto 4 filas e 3 columnas pa que quede
# bonito. Evidentemente esto cambiaría no caso de ter máis ou menos series de
# datos (pensei en facelo máis automático pero por ahora hai que fastidiarse).
# Recomendable ver o exemplo de matplotlib
lenzos = ventana.subplots(
    nrows = 4,
    ncols = 3,
    sharex = True, # pa que teñan as mesmas escalas e eixos
    sharey = True  #
)

# E agora hai que iterar polos 12 lenzos. A cousa e que estos lenzos están
# gardados por filas e columnas, tal e como sería de esperar. Se queremos
# iterar polos 12 en 'orde', é dicir, de esquerda a dereita e arriba abaixo,
# podemos usar o truco do almendruco e usar as operacións // e %
for i in range(len(datos)):

    # Iremos 'seleccionando' os lenzos un a un. Podese escribir nun papel os
    # valores de i//3 e i%3 pa ver o que da. Usaremos estas parexas de numeros
    # como índices
    # i//3 = 0 0 0 1 1 1 2 2 2 3 3 3
    # i%3  = 0 1 2 0 1 2 0 1 2 0 1 2
    lenzo = lenzos[i // 3, i % 3]

    coord_x = (1 / datos[i][0]) * R * temperaturas[i] # RT/V
    coord_y = datos[i][1] # P

    # para as rectas, necesitamos valores x, polo menos 2 puntos
    coord_x_rectas = np.array([min(coord_x),max(coord_x)])

    lenzo.plot(
        coord_x_rectas,
        coord_x_rectas * regresions_moles[i][2] + regresions_moles[i][0],
        #    X         *   pendente (moles)    +  ordenada
        linestyle = '-',
        marker = '',
        color = 'black'
    )

    # E os puntos
    lenzo.plot(
        coord_x,
        coord_y,
    )
    lenzo.set( title=f"{temperaturas[i]} K" )

    # usando o mesmo truco de antes, é posible poñer titulos solo as gráficas
    # que están abaixo e á esquerda
    if i%3 == 0: # Columna 0
        lenzo.set(ylabel = r"$Presión  (Pa)$")
    if i//3 == 3: # Fila 3
        lenzo.set(xlabel = r"$RT/V$")


plt.show()

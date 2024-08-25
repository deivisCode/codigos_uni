import os
import pathlib

import numpy as np
import matplotlib.pyplot as plt


# Os datos necesarios neste caso son os de P V e T na 'zona ideal'. Sería
# totalmente factible cargar aquí os orixinais e logo reducilos á zona de
# interés, pero prefiero usar os que xa 'recortei' no outro programa
# (principal.py). Para cargar os datos, como son varios ficheiros, fago o mesmo
# que na grafica anterior
DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

nomes_ficheiros = os.listdir(
    DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI_ideales\\"
)
datos = []
for nome in nomes_ficheiros:
    datos.append(
        np.loadtxt(
            DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI_ideales\\" + nome,
            unpack=True,  # os datos están por filas
            dtype=np.float64,
        )
    )
cantas_series = len(datos)


# Tamén necesitamos as temperaturas, e a constante R
temperaturas = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperaturas.txt")
R = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\R.txt")  # J / mol K

# E evidentemente, os valores das pendentes e ordenadas (vamos, as regresións)
regresions_moles = np.loadtxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\moles_regresions.txt"
)


# GRAFICAS ============================================

# primeiro creo unha ventana normal
ventana = plt.figure(
    num     = "Figura comportamento ideal",
    figsize = (8,9),
)


# Quero colocar todas as graficas nunha espacie de forma rectangular, pero como
# a priori non sei cantas series de datos habrá o que fixen foi usar meus
# alucinantes (broma) coñecementos de matemáticas para estimar a forma correcta
# da grafica. Supoñamos que temos N series de datos. Poderíamos coller sempre o
# enteiro superior de raiz(N) para as filas e para as columnas. O problema é
# que moitas veces este número é demasiado grande e quedan demasiados ocos
# baleiros. Tamén poderíamos coller o enteiro inferior e o superior,
# respectivamente, pero neste caso non temos asegurado que seu produto sexa tan
# grande como o noso numero N. O que fixen entonces foi considerar os casos, e
# dependendo da situación usarase un ou outro. Comezo calculando a raiz do
# numero de series, o enteiro superior e o inferior
raiz  = np.sqrt(cantas_series)
techo = np.ceil(raiz)
chan  = np.floor(raiz)

# Este é o caso dos cadrados perfectos, teremos unha cuadrícula perfecta
if chan * chan == cantas_series:
    filas = int(chan)
    columnas = int(chan)

# caso intermedio, por exemplo con 11 series teremos raiz(12) = 3.317...  o
# enteiro superior e 4 e o inferior é 3, e ademais 3*4 é 12 > 11, polo que
# collemos este. Non sempre pasa, por eso a veces hai que ir polo exceso (caso
# seguinte)
elif techo * chan >= cantas_series:
    filas = int(chan)
    columnas = int(techo)

# pa numeros puñeteros, como 7. raiz(7) = 2.648... o enteiro inferior e 2, o
# superior é 3, e 2*3 < 7, polo que non nos chegaría o espazo. Pa esos casos
# usamos este
else:
    filas = int(techo)
    columnas = int(techo)

# e usamos este método para crear os nosos lenzos de golpe, moi cómodo
lenzos = ventana.subplots(
    nrows = filas,
    ncols = columnas,
    sharex = True, # pa que teñan as mesmas escalas e eixos
    sharey = True  #
)

# Iteramos por todos os elementos
for i in range(filas * columnas):

    # Tal e como se viu nas explicacions anteriores, pode darse o caso de que
    # teñamos máis ocos que datos. En total temos 'cantas_series' de datos,
    # polo que unha vez pasemos ese número non plotearemos máis cousas
    if i+1 <= cantas_series:

        # Quero ir colocando os elementos de esquerda a dereita e arriba
        # abaixo. Para eso teño que indexalos da seguinte maneira
        #
        # columna_actual = i // columnas
        # fila_actual    = i %  columnas
        #
        # non sei explicar por qué esto funciona, facédeo en papel
        lenzo = lenzos[i // columnas, i % columnas]

        # Os puntos x e y que queremos graficar
        coord_x = (1 / datos[i][0]) * R * temperaturas[i] # RT/V
        coord_y = datos[i][1] # P

        # ploteámolos
        lenzo.plot( coord_x, coord_y,)

        # para as rectas, necesitamos valores x, polo menos 2 puntos. Collo o
        # primeiro e o ultimo dos valores anteriores
        coord_x_rectas = np.array([min(coord_x),max(coord_x)])

        lenzo.plot(
            coord_x_rectas,
            coord_x_rectas * regresions_moles[i][2] + regresions_moles[i][0],
            #    X         *   pendente (moles)    +  ordenada
            linestyle = '-',
            marker = '',
            color = 'black'
        )

        # E poñolle titulo
        lenzo.set( title=f"{temperaturas[i]} K" )

        # usando o mesmo truco de antes, é posible poñer titulos solo as
        # gráficas que están abaixo e á esquerda
        if i % columnas == 0: # Columna 0
            lenzo.set(ylabel = r"Presión  (Pa)")

        if i // columnas == filas - 1: # ultima fila
            lenzo.set(xlabel = r"RT/V  (mol/Pa)")

    # se temos demasiados ocos, os que facemos é vaciar completamente ese lenzo
    elif i+1 > cantas_series:
        lenzos[i // columnas, i % columnas].remove()

plt.show()

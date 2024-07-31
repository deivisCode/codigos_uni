
import numpy as np
import matplotlib.pyplot as plt
from regresion_lineal import regresion

# Primeiro cargo as 4 series de datos correspondentes aos 4 procesos medidos.
# e.g. t_p_etanol_quentamento refírese á serie de datos de (t)emperatura e
# (p)resion do etanol no proceso de quentamento. A extensión 'numpydata' é
# inventada, non son máis que arquivos de texto plano. Ollo, non son arquivos
# CSV propiamente ditos porque conteñen espazos (podedes eliminalos se
# queredes). Por defecto 'loadtxt' carga os datos fila a fila, polo que
# teríamos un array con 70 e pico sub-arrays. O que quero é, para cada serie de
# datos, ter as temperaturas e presións nunha ristra
# de datos en liña. Simplemente hai que especificar 'unpack'= True
t_p_etanol_quentamento = np.loadtxt(
    r"datos\t_p_etanol_quentamento.numpydata",
    dtype=np.float64, # creo que non fai falta pero poñoo por si acaso
    delimiter=",", # caracter que separa os datos en cada fila
    unpack=True, # obter a trasposta
    comments="#", # caracter que especifica un comentario
)
t_p_etanol_enfriamento = np.loadtxt(
    r"datos\t_p_etanol_enfriamento.numpydata",
    dtype=np.float64,
    delimiter=",",
    unpack=True,
    comments="#",
)
t_p_auga_quentamento = np.loadtxt(
    r"datos\t_p_auga_quentamento.numpydata",
    dtype=np.float64,
    delimiter=",",
    unpack=True,
    comments="#",
)
t_p_auga_enfriamento = np.loadtxt(
    r"datos\t_p_auga_enfriamento.numpydata",
    dtype=np.float64,
    delimiter=",",
    unpack=True,
    comments="#",
)

# Agora arrexunto todos os datos nunha lista normal de Python (son dinámicas e
# seus elementos poden ser de calquer tipo/lonxitude, non como nos arrays de
# numpy que deberian ter a mesma lonxitude). Deste xeito poderemos iterar pola
# lista para realizar as regresións en vez de escribilo
# todo 4 veces
datos = [
    t_p_etanol_quentamento,
    t_p_etanol_enfriamento,
    t_p_auga_quentamento,
    t_p_auga_enfriamento,
]

# Por algún motivo os do departamento de termo néganse a usar unidades do SI
# nos aparellos asique a continuación hai que facer esto
for i in range(len(datos)):
    # datos[i] é cada unha das series de datos, que á sua vez contén
    # as temperaturas, datos[i][0] e as presións datos[i][1]
    datos[i][0] = datos[i][0] + 273.15 # pasar de ºC a K
    datos[i][1] = datos[i][1] * (10**5) # pasar de bar a Pa

# Para as incertezas, só consideraremos erro no eixo 'y', que corresponde ao log(p),
# polo que solo necesitamos o erro da presion.
erro_presion = 100  # pascales. Non recordo de onde o saquei, seguramente o inventase

# A continuación hai que realizar as regresións lineales. Neste caso uso un
# programilla que fixen eu tamén, que é a aplicación directa das formulas que
# aparecen no librillo verde aquel de estadística de Faustino. Realmente
# calquera outro paquete vale. A funcion esta devolve unha tupla con
# (ordenada, erro ordenada, pendente, erro pendente). Para cada serie realizo a
# regresión (a cal devolve unha tupla de 4 datos) e logo meto cada unha nunha
# lista
regresions = []
for serie in datos:  # para cada serie de datos
    # calculase a regresion usando a funcion esta
    calculos = regresion(
        np.reciprocal(serie[0]),  # datos 'x', 1/T
        np.log(serie[1]),  # datos 'y', log(P)
        # erro no eixo 'y'. Realmente habería que cambialo porque no eixo y
        # temos o logaritmo da presión e non a presión sola (súdama)
        [erro_presion] * len(serie[0]),
    )
    # finalmente engadimos a regresion á lista
    regresions.append(calculos)

# prefiero pasar a lista a un array, inda que tanto da
regresions = np.array(regresions)

# deberían ser datos tal que así:
# 2.610144042968750000e+01 1.503591918945312500e+02 -5.149218750000000000e+03 5.141592578125000000e+04
# 2.645703125000000000e+01 5.551948852539062500e+02 -5.300250000000000000e+03 2.084273437500000000e+05
# 2.432336425781250000e+01 1.475106506347656250e+02 -4.759500000000000000e+03 5.639607031250000000e+04
# 2.358105468750000000e+01 2.239029998779296875e+02 -4.468375000000000000e+03 8.686179687500000000e+04

# GRAFICAS ===================================================================

# NOTA: moitos estilos e detalles das gráficas están no arquivo 'matplotlibrc'

# Creo unha ventana
ventana = plt.figure("Ventana bonica", dpi=(150),figsize=(10,6))

# Creo un lenzo pa pintar
lenzo = ventana.add_subplot(1,1,1,
    xlabel = r"$\frac{1}{T}$", # usando tipografía de \LaTeX
    ylabel = r"$\log{P}$"      #
)

# Agora hai que graficar moitas cousas: 4 series de datos crudos, os dos
# arquivos; e 4 rectas axustadas. Temos todo en listas ou arrays asique podemos
# iteralas e facelo todo de golpe. Primeiro defino unhas listas cos  estilos
# que quero usar pa cada serie de datos. NOTA: fixarse que o ciclo de cores
# roxo-azul-roxo-azul está no arquivo matplotlibrc
marcas = ['.','.','d','d']
nomes = [
    "Etanol, quentamento",
    "Etanol, enfriamento",
    "Auga, quentamento",
    "Auga, enfriamento",
]

# E toca iterar
for i in range(len(datos)):
    # Comezo ploteando os datos crudos
    lenzo.plot(
        np.reciprocal(datos[i][0]),  # datos 'x', 1/T
        np.log(datos[i][1]),  # datos 'y', log(P)
        linestyle = "",
        marker    = marcas[i],
        label     = nomes[i],
        # 'zorder' é pa que os puntos estos queden por encima das liñas grises que
        # vamos pintar despois
        zorder    = 2.5 
    )
    # Agora os axustes. Os datos que temos son as pendentes, ordenadas e súas
    # incertezas. Para graficar unha recta só necesitamos 2 puntos. Para cada
    # serie, podemos coller 2 valores x, por exemplo, min(serie), max(serie), e
    # logo calcular a 'y' correspondente como y = pendente * x + ordenada.
    # Entonces: primeiro collo dous puntos do eixo x, os menores e maiores para cada
    # serie (tendo en conta que no eixo x está 1/temperatura).
    puntos_x = np.array(
        (
            # valor x máis a esquerda (minimo) para cada serie
            min(np.reciprocal(datos[i][0])),
            # valor x máis a dereita (maximo) para cada serie
            max(np.reciprocal(datos[i][0])),
        )
    )
    # E as coordenadas y son simplemente: y = pendente * x + ordenada. Nota: esta
    # operacion solo se pode facer asi porque 'puntos_x' é un array, por eso antes
    # se pasa de tupla a array
    puntos_y = regresions[i][2] * puntos_x + regresions[i][0]
    # Finalmente, solo queda graficalo
    lenzo.plot(puntos_x, puntos_y, color = "gray")

lenzo.legend()
plt.show()

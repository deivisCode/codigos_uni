import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sco

# Primeiro cargo os datos. Estos corresponden á práctica da balanza
# de torsion (amo esa practica). Estos son datos dunha posicion en centímetros.
# Están tomados por filas. Graficamente teñen a forma dunha sinusoide acotada
# por unha exponencial decrecente
posicions = np.loadtxt(r"datos\posicions.txt")

# Para as incertezas na posicion tomarei simplemente unha ristra de valores 1.0
incertezas_posicions = np.array([1.0]*len(posicions))

# Os datos dos tempos métoos a pelo aquí. É unha ristra entre 0 e a cantidade
# de datos de posicions, de 10 en 10. Unidades de segundos
tempos = np.arange(0,10*len(posicions),10)

# Evidentemente estos datoos metoos así aquí por ser un mero exemplo. Na
# realidade habería que xustificalos algo máis

# O que se suele pedir nas memorias é axustar series de datos deste tipo a
# algunha función arbitraria. Esto significa que debemos obter os parámetros
# característicos da funcion que queremos 'axustar' usando como modelo nosos
# datos experimentales. Ven sendo análogo aos axustes lineais de rectas, pero
# nun caso máis xeral. O que queremos ao final do dia son tuplas de valores,
# (a,b,c,d,e,...) (parámetros) que fan que certa ecuacion (a cal queremos
# axustar) replique o mellor posible nosos datos. No caso de ser lineal,
# poderíamos conformarnos cas regresións de mínimos cadrados típicas. Para
# funcións máis elaboradas (neste caso será unha exponencial) soese recurrir ao
# paquete 'scipy.optimize' e a funcion 'curve_fit'. Por trivial que pareza, ven
# sendo o que usa todo o mundo á hora de facer os análises de datos (excepto os
# psicópatas que os fan en excel)
#
# O que se fai é meter a función que queremos axustar dentro de 'curve_fit',
# xunto cos datos experimentales, seguido unha tupla de parámetros "de proba"
# (logo comento esto mellor) e unhas incertezas.
#
# curve_fit(
#     f,                        --> función a axustar
#     xdata,                    --> datos 'x' experimentales
#     ydata,                    --> datos 'y' experimentales
#     p0 = None,                --> parámetros de "proba"
#     sigma = None,             --> incerteza en 'y'
#     absolute_sigma = False,   --> incertezas absolutas ou relativas
#     **kwargs                  --> resto de opcións
# )
#
# Por exemplo. Supoñamos que definimos unha funcion 'exponencial' que queremos
# logo axustar aos datos de posicións e tempos que carguei antes, e que temos
# unha ristra de parámetros de proba (0.1, 996), e unhas incertezas absolutas
# para os valores das posicións (eixo 'y') gardadas na variable 'incertezas'
# (logo menciono todo esto mellor):
#
# curvefit(
#     exponencial,
#     tempos,
#     posicions,
#     p0 = (0.1, 996),
#     sigma = incertezas,
#     absolute_sigma = True
# )
#
# IMPORTANTÍSIMO:
#
# A función que queremos axustar, a cal metemos como primeiro argumento de
# 'curve_fit', debe aceptar como primeiro argumento o que antes chamei 'xdata'
# e logo os parámetros de proba no mesmo orde no que os metemos en 'curve_fit'.
# Ademáis debe devolver valores do mesmo estilo que 'ydata'. É dicir, no
# exemplo anterior, a función 'exponencial' debe aceptar como primeiro
# argumento, datos de tempos; e logo, debe poder aceptar 2 argumentos a
# maiores, dado que en curvefit estábamos metendo uns parámetros de proba con
# dous datos. Ousexa, a función debe ser algo tipo:
#
#                xdata   parámetros
#                  |      |     |
# def exponecial(tempos,  0.1,  996)
#     return posicions
#                |
#              ydata
#
# O que solemos facer é definir primeiro a función con todos os parámetros que
# necesitemos e logo ter en conta esto á hora de usar 'curve_fit'.
#
# DETALLES SOBRE OS PARÁMETROS
#
# Dúas cousas importantes. É necesario meter uns parámetros 'razonables' en
# 'curve_fit', e con esto quero decir que se os que se meten son totalmente
# aleatorios, a función pode non funcionar, e de feito é algo que soe pasar. O
# que se pode facer é graficar primeiro os datos e intentar inferir por onde
# deben andar aproximadamente os parámteros. Na función que vou definir logo,
# van facer falta unhas posicións de equilibrio e unhas frecuencias, as cales
# se poden sacar medio a ollo medio con calculadora. Na práctica de PVT estos
# parámetros son os coeficientes 'a' e 'b' da ecuación de Van der Waals do
# Etano, valores que están tabulados. Por desgracia, ás veces non podemos
# facelo a ollo e o único remedio é ir probando con distintos numeriños. De
# feito, non é unha idea mala de todo ofrecer resultados diferentes onde se
# explique que se consideraron parámetros iniciais diferentes (algo así se
# facía no master parece ser). Por outro lado, hai que ser cauto á hora de
# definir a función a axustar. Por exemplo, supoñamos que queremos axustar
# e^(a/b * x), sendo 'a' e 'b' parámetros, e 'x' nosa variable independiente.
# Ao meter esto, scipy non vai poder axustalo, dado que existe un número
# infinito de valores 'a' e 'b' cuxo cociente xera o mesmo resultado. En
# verdade, poderíamos executar o programa unha e outra vez, partindo de
# parámetros iniciales diferentes, e seguiríamos obtendo pares (a,b) diferentes
# pero co mesmo cociente. Para solucionalo, o que deberíamos intentar
# axustar sería e^(c * x), onde c:=a/b. Esta constante 'c' sí pode ser
# axustada, e logo solo temos que buscar algunha outra relación para obter 'a'
# e 'b' por separado. Eu este último detalle atopeino na práctica de Seebeck de
# termo

# Empezamos

# Primeiro defino a funcion que quero axustar, tendo en conta que os parámetros
# que esta acepta determinará como logo teño que meter os datos en curve_fit. O
# significado da formula esta e de cada parámetro é irrelevante neste caso,
# solo é un exemplo
def exponencial( t, y0, A, gamma, w, phi):
    """Funcion exponecial decrecente que se pide na memoria da práctica do
    pendulo de torsion.

    t     : Array de numpy cos tempos
    y0    : Punto de equilibrio
    A     : Amplitude máxima
    gamma : O coeficiente de amortecemento
    w     : frecuencia de oscilación
    phi   : fase inicial"""
    y = y0 + A * np.exp(-gamma * t) * np.sin(w * t + phi)
    return y

# O valor 't' será o noso 'xdata', e o resto TODO de argumentos, (y0, A, gamma,
# w, phi), serán parámetros iniciales. O que devolve a función son valores de
# posicións, que é o que meteremos en 'ydata'

# Para os parámetros iniciales, considerarei os seguintes:
parametros_iniciales = (145, 80, 0.01, 0.003, 1)
#                       |    |   |      |     |
#                       y0   A   |      w    phi
#                              gamma
#
# Estimeinos mirando unha gráfica dos datos, e no caso de gamma, simplemente
# probei ata dar con algo con xeito.

# Agora hai que realizar os axustes con 'curve_fit'. O detalle é que non
# mencionei qué é o que devolve a funcion 'curve_fit'. Unha vez fagamos
#
# axustes = sco.curvefit(....)
#
# na variable 'axustes' teremos unha tupla (ou tal vez era unha lista, non
# recordo), onde o primeiro elemento son os nosos parámetros ( t, y0, A, gamma,
# w, phi) optimizados, e o segundo elemento é unha matriz de covarianzas
# (véxanse os apuntes de Faustino)
#
# axuste[0] : [1.44671e+02 8.14496e+01 7.97553e-04 1.04045e-02 1.91018e+00]
#
# axuste[1] :
#
# [[ 6.03867e-03  1.70524e-03  1.83341e-08 -1.05306e-07 7.10262e-05]
#  [ 1.70124e-03  9.06640e-02  1.25642e-06 -2.15683e-07 1.95150e-04]
#  [ 1.83041e-08  1.25642e-06  2.86646e-11 -2.30663e-12 2.46396e-09]
#  [-1.05306e-07 -2.15283e-07 -2.30263e-12  2.88716e-11 -1.43936e-08]
#  [ 7.10262e-05  1.95150e-04  2.46396e-09 -1.47936e-08 1.25836e-05]]
#
#
# O primeiro elemento danos directamente os parámetros optimizados. A matriz do
# segundo elemento é algo máis rara (insisto, aparece nos apuntes de Faustino).
# O único que nos interesa do segundo elemento, da matríz, son os valores da
# diagonal (excepto que sexades uns lunáticos da estadsítica e lle saquedes uso
# ao resto da matriz). Os elementos da diagonal, en orde, son as varianzas dos
# nosos parámetros que queríamos optimizar, asique se lle sacamos a raíz
# cadrada obtemos as desviacións estándar (que veñen sendo as incertezas). Polo
# tanto, cando usamos 'curve_fit' interesanos o primeiro elemento que devolve
# (parámetros optimizados), que obtemos directamente con 'axuste[0]'; e a raíz
# da diagonal (incertezas dos parámetros), que obtemos con
# 'np.sqrt(np.diag(axuste[1]))'. Polo menos no meu caso éste foi o método xeral
# de traballo para axustar cousas.

# Sen máis lío, facemos o axuste non lineal con 'curve_fit' e gardámolo na
# variable 'axuste'
axuste = sco.curve_fit(
    exponencial,                   #  función a axustar
    tempos,                        #  datos 'x' experimentales
    posicions,                     #  datos 'y' experimentales
    parametros_iniciales,          #  parámetros de "proba"
    sigma = incertezas_posicions,  #  incerteza en 'y'
    absolute_sigma=True            #  incertezas absolutas
)

# e collo os datos interesantes en variables aparte
parametros_optimizados = axuste[0]
incerteza_parametros_optimizados = np.sqrt(np.diag(axuste[1]))

# Outra opción sería usar desempaquetamento de tuplas e facer
#
# y0 , A, gamma, w, phi = np.sqrt(np.diag(axuste[1]))
#
# a min personalmente eso non me gusta

# Algún truquillo: En xeral non imos ser tan suertudos como para facer só un
# axuste, senon que teremos que facer 10 ou 12 de golpe, un por cada serie de
# datos. Ésto pode facerse se metemos cada serie de tempos e posicions en
# listas e iteramos por elas. Véxase o programa da práctica de termo PVT, por
# exemplo

# Agora cos parámetros optimizados podemos re-executar a función 'exponencial'
# para graficar unha curva suavina, e ver a diferencia cos datos orixinais. Para
# esto vou calcular os puntos "teóricos"

# uns valores x en cantidade, pa que a funcion se vexa suave
x_teorico = np.linspace(0,max(tempos),10000)

# e os valores 'y' teoricos, ousexa as posicións axustadas, obtéñense
# simplemente aplicando a funcion 'exponencial' cos parámetros axustados
y_teorico = exponencial(
    x_teorico,  # valores x
    parametros_optimizados[0],  # y0     |
    parametros_optimizados[1],  # A      |
    parametros_optimizados[2],  # gamma  |  (optimizados)
    parametros_optimizados[3],  # w      |
    parametros_optimizados[4],  # phi    |
)


# creo unha ventana e lenzo normalmente:
ventana = plt.figure()
lenzo = ventana.add_subplot(1,1,1)

# datos experimentais
lenzo.plot(
    tempos,
    posicions,
    color  = "red",
    label  = "Datos experimentales",
    zorder = 2.5
)

# e os datos axustados
lenzo.plot(
    x_teorico,
    y_teorico,
    marker    = "",
    linestyle = "-",
    color     = "black",
    label     = "Axuste"
)

plt.legend()
plt.show()

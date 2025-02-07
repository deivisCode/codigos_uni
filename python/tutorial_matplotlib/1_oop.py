
import numpy as np
import matplotlib.pyplot as plt


# Aqui cargo uns datos de proba (son da práctica do pendulo de torsion). Son
# datos de posicións, en centímetros. As posicións axustadas son datos sacados
# con curve_fit doutro programa
posicions = np.loadtxt(r"datos\datos.csv")
posicions_axustadas = np.loadtxt(r"datos\datos_axustados.dat")

# Tamén necesitamos datos dos tempos. Invéntomos. Para os tempos, creo un array
# de 10 en 10.
tempos = np.arange(0, 10 * len(posicions), 10)

# Tamén pode ser relevante ter os residuos (experimento - axuste) e as incertezas. 
# Neste caso non as vou usar pero nalgún programa dos seguintes si
# residuos = posicions - posicions_axustadas
# incertezas = np.array([1.0] * len(posicions))

# APARTADO GRÁFICO ================

# NOMES
# Matplotlib soe ter nomes confusos para diferentes obxetos e metodos que en
# xeral non transmiten demasiada informacion (deberon coller a costumbre dos
# putos matemáticos). Por simplicidade (e por costumbre miña) non vou chamar ás
# cousas 'fig', 'axe', 'axis' nin similares, senon nomes máis suxerentes en galego.
# fig -> ventana, axe -> lenzo, axis -> eixos, etc.
# O de ventana non é 100% correcto pero creo que se entende mellor

# INTERFAZ OOP (Object Oriented Programming) (menudo level de inglish teño XD)
#
# O rollo patatero aquel de informática para 100tificos de usar a interfaz de
# pyplot non é nin comodo nin recomendado. O que se soe facer no putísimo mundo
# real é usar un método explícito onde se crean os distintos obxetos da imaxe
# que queremos. De cada obxeto podemos crear 'sub-obxetos' (xa, xa sei que non
# se chama asi nada desto). Por exemplo, creamos un obxetp de tipo 'figure' e
# metemolo nunha variable chamada 'ventana'. A partir desto podemos crear o
# seguinte obxeto, un 'axe', facendo lenzo = ventana.add_axes(...). Logo
# poderíamos seguir con un obxeto de tipo 'Line2D', grafica = lenzo.plot(...).
# A cadena continúa, pero en xeral non necesitamos meternos máis.
#
# Entonces:
# ventana --> obxeto de tipo 'figure', obxeto base
# lenzo   --> obxeto de tipo 'axe', asociado ao obxeto 'figure'
# plot, stem, scatter, ticks, label --> obxetos de tipo 'Line2D,Text', asociados a un 'axe'

# ESTILO
# Para cambiar cores, grosores, opacidades, tamaños, etc. podemos proceder
# de diferentes maneiras.
#
# DIRECTAMENTE:
#
#   Por un lado, podemos usar directamente as funcions de Matplotlib
#   especificando os parámetros que queremos. Por exemplo, ao facer
#   plot(linewidth=...,color=...,marker=...), ou plt.grid(). Este método
#   sobreescribe todos os seguintes que imos mencionar, pero ten a desvataxe de
#   que é moi 'verbose', e pouco portable polo que en principio é mellor usalo
#   para parámetros que non se poden configurar doutra maneira, ou para
#   sobreescribir os arquivos de configuracion (logo falo deles) de maneira
#   puntual.
#
#   Outra maneira no propio programa é manipular directamente a configuración,
#   a cal está gardada nun dicionario en 'matplotlib.rcParams', asique podemos
#   facer algo como:
#
#   import matplotlib as mpl
#   mpl.rcParams["axes.grid"] = True # pa activar o grid
#
#   Este método (en inglés chámanos algo así como 'runtime configuration
#   settings') é máis global, e afecta a todas as gráficas do programa, ademais
#   de que se pode sobreescribir polo método anterior; neste caso, poñendo
#   explicitamente no programa plt.grid(False). Con todo, ten a mesma
#   desvantaxe, acumular liñas de configuracion no propio programa e ser pouco
#   portable
#
# ARQUIVOS '*.mplstyle' e 'matplotlibrc'
#
#   Unha maneira de facer o programa máis limpo é separando a configuracion das
#   gráficas (cores, tamaños, etc.) do programa principal. Estas configuracións
#   poden gardarse en arquivos chamados 'matplolibrc' ou '*.mplstyle' (este
#   último so ten o requerimento de ter esa extension). Non son máis que arquivos
#   de texto plano cun formato específico, véxase:
#   https://matplotlib.org/stable/users/explain/customizing.html#the-default-matplotlibrc-file
#   Hai unha diferenza principal entre estos dous tipos de arquivos. O arquivo
#   'matplotlibrc' lese automáticamente sempre que estea no mesmo directorio
#   que o programa que teamos rulando, polo que non temos que requerilo nin
#   importalo. No caso dunha configuración *.mplstyle, debemos importala no
#   programa usando plt.style.use("meu_estilo.mplstyle").
#
# A orde de preferencia das configuracións é
# rcParams > *.mplstyle > matplotlibrc
#
# Neste caso uso unha 'matplolibrc', para activar o grid, ticks grandes e
# pequenos arriba e na dereita, grosor das liñas, tipo de lenda, tamaño de
# letra, tipografía, tamaño da ventana, calidade, etc.

# TOCA GRAFICAR ================================================

# O que normalmente sería 'fig'. O obxeto que é unha ventana e sobre o que
# iremos construindo máis cousas
ventana = plt.figure("Ventana de datos")

# Agora o que normalmente se chamaría 'axe'. É unha zona da ventana na que
# podes debuxar e tal. Hai diferentes métodos para crear estos lenzos (axes) a
# partir dunha ventana (figure), ver:
# https://matplotlib.org/stable/api/figure_api.html#adding-axes-and-subfigures
# Hai 3 maneiras principales: 'ventana.subplots(), ventana.add_subplot(),
# ventana.add_axes()'
#
# 'subplots'
#   Permite crear varios lenzos do tirón (devolve unha lista de lenzos), por exemplo:
#   >>> lenzos = ventana.subplots( nrows = 2, ncols = 1)
#   crea 2 lenzos, distribuidos como en 2 filas e 1 columna
# 'add_subplot'
#   Similar ao anterior pero crea un lenzo de cada vez.
#   >>> lenzo_1 = ventana.add_subplot(3,1,[1,2])
#   >>> lenzo_2 = ventana.add_subplot(3,1,3)
#   Esto serían dous lenzos, onde o primeiro ocuparia as filas 2-3 nunha
#   distribucion de 3 filas e 1 columna; e o segundo ocuparía a terceira fila,
#   nunha distribucion de 3 filas e 1 columna (npi de se me tou explicando XD)
# 'add_axes'
#   Método máis manual no que hai es especificar as coordenadas do lenzo en vez de dircirlle
#   que ocupe tantas filas ou columnas.

# Neste exemplo usarei 'add_subplot'
lenzo = ventana.add_subplot(ylim=(60,240))

# Unha vez temos os lenzos creados, podemos facerlle perradas a base de
# lenzo.plot(), lenzo.scatter(), lenzo.violinplot(), etc.
lenzo.plot(tempos, posicions_axustadas, color="gray", label="Axuste")
lenzo.plot(
    tempos, posicions, color="red", marker=".", linestyle="", label="Datos Orixinais"
)
# son os datos do axuste, as posicions experimentales

# Neste caso usamos directamente lenzo.plot() e non o gardamos nunha variable,
# variable = lenzo.plot(), porque o obxeto do 'plot' non o vamos necesitar
# máis polo que creándoo é suficiente. Sin embargo, hai casos nos que sí que
# hai crealo e nomealo, por exemplo (véxase a práctica de Laplace) ao facer un
# mapa de calor podenos interesar engadir unha barra lateral cunha escala das
# cores. Entón, deberíamos crear os puntos da gráfica (polo método que sexa,
# plot, scatter, contour, etc.) e darlle nome. Por exemplo:
# >>> LINHAS = lenzo.contour(x,y,z)
# deste xeito, logo podemos asociar unha escala a esto facendo
# >>> ventana.colorbar(LINHAS,...)
# Se non o nomeamos non o podemos chamar despois

# Podemos engadirlle algúns detalles aos lenzos:
lenzo.set(
    title  = "Gráfica sinusoide exponencial decrecente UwU",
    ylabel = "Posicions (cm)",
    xlabel = "Tempo (s)"
)

# Finalmente, para gardar a imaxe
# ventana.savefig("grafica.png")
# E mostrámola!
plt.show()


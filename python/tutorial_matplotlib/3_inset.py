import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Neste caso vamos facer a mesma gráfica pero en vez de engadir un rectángulo
# imos meter unha especie de 'zoom' para resaltar parte da gráfica. Como antes,
# uso os mesmos datos, asique non me paro a explicalo demasiado. Véxase o
# arquivo '1_oop.py' pa mais detalles. A única diferencia é que neste caso sí
# necesitarei unhas incertezas (invéntomas e pista)
posicions = np.loadtxt(r"datos\datos.csv")
posicions_axustadas = np.loadtxt(r"datos\datos_axustados.dat")
tempos = np.arange(0, 10 * len(posicions), 10)
incertezas = np.array([1.0] * len(posicions))

# As mesmas gráficas de antes:
ventana = plt.figure("Ventana de datos")
lenzo = ventana.add_subplot(ylim=(60,240))
lenzo.plot(tempos, posicions_axustadas, color="gray", label="Axuste")
lenzo.plot(
    tempos,
    posicions,
    color     = "red",
    marker    = ".",
    linestyle = "",
    label     = "Datos Orixinais"
)
lenzo.set(ylabel="Posicions (cm)",xlabel="Tempo (s)")


# Agora toca montar un zoom, ou como o chaman os frikis de matplotlib,
# 'inset_axes'. Como sempre, o primeiro será crear o obxeto en sí e logo facer
# que se mostre no noso lenzo. Personalmente creo que o rollo este é algo
# lioso. O obxeto 'inset_axes' en sí é un obxeto de tipo 'Axe', unha especie de
# 'sub'-lenzo que podemos meter dentro do lenzo principal. Logo, poderemos
# engadirlle curvas e gráficas normalmente, é dicir:
#
# >>> zoom = lenzo.inset_axes(***)
# >>> zoom.plot(***)
# >>> zoom.errorbar(***)
#
# O primeiro que debemos facer é especificar as coordenadas onde queremos
# colocalo e canto queremos que ocupe. Hai que pasarlle unha tupla (ou lista)
# cos valores (x,y,ancho,alto), onde 'x' e 'y' son as posicións da esquina
# inferior esquerda. Hai dúas maneiras, dando as coordenadas 'relativas' dentro
# do propio lenzo (en porcentaxes, tipo, 0.3) ou dando as 'absolutas', ousexa
# os valores concretos x e y. O primeiro método pode ser máis cómodo porque lle
# indicamos que ocupe certo porcentaxe do lenzo, polo que se éste cambia non
# pasa nada. Mentres que no segundo caso, se lle damos a posición exacta e logo
# cambian os datos (e os eixos se reaxustan) pode quedar desaxustado, ou
# incluso fora do lenzo.
#
# Para usar posicions 'RELATIVAS':
# zoom = lenzo.inset_axes(
#     (0.2,0.3,0.2,0.3)
# )
# que corresponde á posicion 'x' nun 20% do tamaño horizontal total do lenzo,
# posición 'y' un 30% do tamaño vertical total, que teña un ancho do 20% e alto
# do 30%
#
# Para usar posicions 'ABSOLUTAS':
# zoom = lenzo.inset_axes(
#     (1350,170,400,50),
#     transform = lenzo.transData,
# )
# que corresponde a poñer o inset na coordenada 'x' 1350, 'y' 170, que ocupe
# 400 unidades de ancho e 50 de alto. O de transform=lenzo.transData é o que
# din na documentacion que hai que usar pa facelo así, non o mirei moito máis

# Personalmente prefiero as coordenadas absolutas, asique fago uso o segundo
# método. A maiores, temos que ver que o noso 'inset' é un lenzo 'Axe' en sí,
# polo que ten seus propios eixos e escalas. Se non especificamos ningún límite
# a maiores, logo ao facer zoom.plot(***) graficará TODO como se fose un lenzo
# normal, solo que máis pequeno. Sin embargo solo queremos ver un trozo dos
# datos, polo que temos que especificar o rango de datos con 'xlim' e 'ylim'
# (sinceramente esto é un lío patatero XD)
zoom = lenzo.inset_axes(
    # x,y,ancho,alto
    (1350,170,400,50),
    transform = lenzo.transData,
    # Qué trozo dos datos queremos ver no noso mini-lenzo. Non é necesario pero
    # se non se pon despois ao graficar cousas veríamos as gráficas enteiras de
    # novo, o cal é inútil. Esto sempre son coordenadas 'absolutas'
    xlim = (1600,1680),
    ylim = (140,160),
    # Finalemente, desactivolle os numeriños aos eixos, queda máis limpo
    xticklabels = [],
    yticklabels = []
)

# Como mencionei antes, lenzo.inset_axes(...) devolve outro obxeto de tipo
# 'axe', polo que podemos pintar nel, engadir titulos, etc. como se fose un
# lenzo calqueira. Podemos usar as cousas típicas como 'plot', 'stem',
# 'scatter', etc.
zoom.plot(tempos, posicions_axustadas, color="gray", label="Axuste")
zoom.errorbar(
    tempos,
    posicions,
    yerr=incertezas,
    color="red",
    ecolor = "black",
    marker=".",
    linestyle="",
    label="Datos Orixinais",
)
zoom.set(title="Zona con datos inventados")

# Todo esto era o mini-lenzo, onde graficamos outra vez parte dos datos pa que
# pareza que fixemos zoom. Se queremos señalar a zona que estamos 'aumentando',
# que corresponde á zona que delimitamos con 'xlim' e 'ylim' ao crear o inset,
# entón debemos facer
lenzo.indicate_inset_zoom(zoom,edgecolor = "blue")
# onde lle puxen cor azul pa que se vexa o que é

plt.legend()
plt.show()

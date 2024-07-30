import numpy as np
import matplotlib.pyplot as plt

# Os datos cargámolos dun arquivo CSV a un array de numpy típico. Tamén é
# posible usar pandas o cal está orientado a este tipo de datos pero por algún
# motivo (XD) é mais facil usar numpy. Os datos corresponden aos valores das
# voltaxes medidos directamente na lámina, onde a última fila corresponde á
# medida máis 'abaixo', a última columna ás medidas máis á dereita, etc. É
# dicir, son datos vistos dende arriba do plano. Tal vez non sexa a mellor
# maneira de tomalos pero é sinxelo e enténdese ben. No caso de necesitar
# reestructuralos, pódense usar funcions típicas de numpy. Como sempre, a forma
# de tomar e gardar os datos determina despois cómo se tratan. Este xeito é o
# máis sinxelo (creo) para logo crear mapas de calor, que é o que se pide na
# práctica
voltaxes = np.loadtxt("datos.csv",delimiter=',')

# Tamén fan falta as posicións. Primeiro consigo ristras de datos x e y que
# corresponden ás posicions na regla. Como está equispaciadas, créanse con
# 'arange'
x = np.arange(7,35) # [7,8,9,10,11,...,34,35]
y = np.arange(7,-6,-1) # [-5,-4,-3,...,5,6]

# para matplotlib interésanos ter unha 'matriz' con todas as posicións x e
# outra coas y. Esto faise facilmente con meshgrid. Ver o arquivo README para
# mais info. Usando desempaquetamento de tuplas queda:
coordenadas_x, coordenadas_y = np.meshgrid(x,y)

# UNHA COMPROBACIÓN. Todas estas cousas deben ter a mesma forma exactamente
if not (coordenadas_x.shape == coordenadas_y.shape == voltaxes.shape):
    raise Exception(
        "As matrices de datos non teñen o mesmo tamaño!!",
        voltaxes.shape,
        coordenadas_x.shape,
        coordenadas_y.shape,
    )


# GRÁFICAS ===================================================================

# Primeiro creamos unha ventana onde traballar. Usareina pa meter todas as
# gráficas aquí.
ventana = plt.figure("Miña ventana bonita",figsize=(10,6),dpi=150)

# usando CONTOUR --------------------------------
# Creamos o lenzo pa pintar
lenzo_1 = ventana.add_subplot(2,2,1)

# titulillo
lenzo_1.set_title("contour + contourf")

# Liñas que marcan os contornos. Aquí temos que meterlle 3 ristras de datos: as
# posicións 'x', as posicións 'y' e as posicións 'z'. Orixinalmente os datos
# que tíñamos en formato CSV corresponden aos valores 'z'. Pódese meterlle 3
# listas cos datos en 'liña', é dicir x = [1,2,3,4], y = [3,5,7,8], z =
# [10,20,30,40], e matplolib tomará as coordenadas elemento a elemento, é dicir
# (1,3,10), (2,5,20), etc. Tamén podemos meter os datos un pouco máis
# ordenados, tal e como os colocamos antes ca función 'meshgrid'. Outro detalle
# é que creamos o obxeto 'contour' explícitamente gardándoo nunha variable
# 'contornos'. Esto non é necesario (podemos facer simplemente
# lenzo_1.contour(**)), pero facéndoo así poderemos referirnos a este obxeto
# para modificalo máis (beneficios da interfaz OOP)
contornos = lenzo_1.contour(
    coordenadas_x,
    coordenadas_y,
    voltaxes,
    levels     = 20,
    linewidths = 0.45,
    linestyles = "dashed",
    colors     = 'k',
    alpha      = 0.5
)

# cores entre as liñas. contourf -> contour fill
contornof = lenzo_1.contourf( # o mapa ese pixelado
    coordenadas_x,
    coordenadas_y,
    voltaxes,
    cmap   = "RdBu", # que estilo de cores usar
    levels = 20, # nivel de detalle
)

# poñerlle numeritos ás liñas
lenzo_1.clabel(contornos, inline=True, fontsize=6)
# no arquivo matplotlibrc teño activado o grid sempre, neste caso non o quero
lenzo_1.grid(False)

# poñer unha escala de color asociada aos niveles entre as liñas
ventana.colorbar(
    contornof, # a qué cousa (e valores) está asociada esta barra
    ax = lenzo_1 # en qué lenzo (matplotlib.axes) o colocamos
)


# usando TRICONTOUR -----------------------------
# Este método usaríamolo se tomásemos datos de forma NON equispaciada na
# lámina. No caso anterior podíanse introducir de 2 maneiras, 3 vectores fila
# ou 3 matrices, pero en ambos casos eran puntos no plano ben colocados. Usando
# tricontour podemos obter un resultado similar inda que os datos estivesen
# desperdigados pola lámina. Neste caso, só podemos introducir os datos en forma
# de vectores fila, polo que usamos 'flatten'
lenzo_2 = ventana.add_subplot(2,2,2)
lenzo_2.set_title("tricontour + tricontourf")

tricontornos = lenzo_2.tricontour(
    coordenadas_x.flatten(),  # Fixarse, agora só se poden meter ristras de
    coordenadas_y.flatten(),  # datos en fila. O de MESHGRID aquí non sirve
    voltaxes.flatten(),       #
    levels     = 20,
    linewidths = 0.45,
    linestyles = "dashed",
    colors     = "k",
    alpha      = 0.5
)

# análogo ao caso anterior. trocontourf -> trocontour fill
tricontornosf = lenzo_2.tricontourf(
    coordenadas_x.flatten(),
    coordenadas_y.flatten(),
    voltaxes.flatten(),
    levels = 20,
    cmap   = "RdBu"
)

lenzo_2.clabel(tricontornos, inline=True, fontsize=6)
lenzo_2.grid(False)
ventana.colorbar(tricontornosf, ax = lenzo_2)


# usando SCATTER --------------------------------
# Agora en 3D. Hai que crear un lenzo tridimensional, que se fai facilmente
# especificando 'projection="3d"' á hora de crealo.
lenzo_3 = ventana.add_subplot(2,2,3,projection='3d')
lenzo_3.set_title("3D scatter")

puntos = lenzo_3.scatter(
    coordenadas_x,
    coordenadas_y,
    voltaxes,
    c = voltaxes, # qué eixo usar pa determinar as cores
    cmap = "cool"
)

ventana.colorbar(
    puntos,
    ax = lenzo_3,
    shrink=0.6 # reducirlle o tamaño pa que quede mellor
)

# usando PLOT_SURFACE ---------------------------

# Pouco que dicir, é idéntico ao anterior pero usando plot_surface
lenzo_4 = ventana.add_subplot(2,2,4,projection="3d")
lenzo_4.set_title("plot_surface")

superficie = lenzo_4.plot_surface(
    coordenadas_x,
    coordenadas_y,
    voltaxes,
    cmap="inferno",
)
ventana.colorbar(superficie, ax = lenzo_4, shrink=0.7)


plt.show()


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


# GRÁFICA 3D ==============

# Primeiro creamos unha ventana onde traballar
ventana = plt.figure("Miña ventana bonita",dpi=150)

# Creamos o lenzo pa pintar
lenzo = plt.axes(projection='3d')

# Un nomes dos eixos
lenzo.set_xlabel("Posición X")
lenzo.set_ylabel("Posición Y")
lenzo.set_zlabel("Voltaxe")

# Usamos o método 'scatter'. Aquí temos que meterlle 3 ristras de datos: as
# posicións 'x', as posicións 'y' e as posicións 'z'. Orixinalmente os datos
# que tíñamos en formato CSV corresponden aos valores 'z'. Pódese meterlle 3
# listas cos datos en 'liña', é dicir x = [1,2,3,4], y = [3,5,7,8], z =
# [10,20,30,40], e matplolib tomará as coordenadas elemento a elemento, é dicir
# (1,3,10), (2,5,20), etc. Tamén podemos meter os datos un pouco máis
# ordenados, tal e como os colocamos antes ca función 'meshgrid'
puntos = lenzo.scatter(
    coordenadas_x, # coordenadas x
    coordenadas_y, # coordenadas y
    voltaxes, # coordenadas z
    c = voltaxes, # qué eixo usar pa determinar as cores
    cmap = "cool" # que estilo de cores usar
)

# engado unha barra de color á dereita como referencia
ventana.colorbar(
    puntos, # a qué cousa (e valores) está asociada esta barra
    ax = lenzo, # en qué lenzo (matplotlib.axes) o colocamos
    shrink=0.6 # reducirlle o tamaño pa que quede mellor
)

plt.show()


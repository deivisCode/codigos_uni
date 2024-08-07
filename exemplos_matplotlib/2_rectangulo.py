import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Neste programilla o que se fai é graficar o mesmo que no programa anterior
# '1_oop.py' pero engadindo un detalle a maiores, un rectángulo (decidín
# separar o programa en programillas pa que sexa máis sinxelo de ver). Tal vez
# non sexa moi interesante pero a min polo menos gustame poñelo pa indicar
# cousas. Aquí supoño que o programa anterior está mirado, asique cargo os
# mesmos datos e grafico o mesmo sin comentar moito.

# Primeiro cargamos uns datos de proba. Véxase o arquivo 1_oop.py pa mais detalles
posicions = np.loadtxt(r"datos\datos.csv")
posicions_axustadas = np.loadtxt(r"datos\datos_axustados.dat")
tempos = np.arange(0, 10 * len(posicions), 10)

# Esta é a gráfica do arquivo anterior, explicada no programa correspondente, asique
# non o volvo comentar
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

# Agora toca crear un rectángulo. En esencia o rectángulo é un obxeto de tipo
# 'Patch' que se pode crear especificando seu tamaño, coordenadas, etc. Hai
# máis obxetos deste tipo, véxase:
# https://matplotlib.org/stable/api/patches_api.html
#
# Neste caso quero un rectángulo (obsesióname o rectángulo) que se contrúe
# facendo
# >>> rectangulo = matplotlib.patches.Rectangle((x,y),width,heith)
# onde (x,y) é o 'punto de aclaxe', as coordenadas da esquina inferior
# esquerda, e width e height os anchos e as alturas. Da documentación oficial:
#
#                +------------------+
#                |                  |
#              height               |
#                |                  |
#              (x,y)---- width -----+


# Primeiro determino as coordenadas (x,y) do punto de anclaxe. Pode ser calquer
# punto do lenzo, pero neste caso eu quero que vaia desde a parte inferior da
# gráfica (limite 'y' inferior) e ata a parte superior. Podería escribir a man
# as coordenadas, pero no caso do valor 'y', éste pode cambiar (o eixo pode
# estirarse) dependendo dos datos que teñamos, se cambiamos os límites da
# gráfica, etc. É mellor coller directamente o punto inferior de todo do lenzo.
# Para eso uso 'get_ylim' que devolve os valores y do lenzo, da forma
# (inferior,superior). A coordenada 'y' da anclaxe será, entón,
# lenzo.get_ylim()[0]
anclaxe_rectangulo = (
    250 , # coordenada x
    lenzo.get_ylim()[0] # coordenada y
)

# Agora necesito o ancho e a altura. O ancho é sinxelo, escolloo directamente a
# man. No caso da altura, collo a diferencia de valores máximos e mínimos do
# lenzo usando get_ylim() polo mesmo motivo que antes
alto = lenzo.get_ylim()[1] - lenzo.get_ylim()[0]
ancho = 100

# O propio obxeto rectángulo.
rectangulo = mpl.patches.Rectangle(
    anclaxe_rectangulo, # (x,y)
    ancho,              # width
    alto,               # height
    # Os obxetos de tipo 'Patch' aceptan multitude de parámetros adicionais
    # comúns a todos eles, véxase:
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch
    facecolor = "orange",
    alpha = 0.3,
    label = "Zona interesante"
)

# Agora o obxeto 'rectangulo' de tipo 'Patch' está creado. Para mostralo solo
# hai que facer:
lenzo.add_patch(rectangulo)

# Como sempre, activamos a lenda LOGO de colocar todas as cousas na gráfica
ventana.legend(loc = (0.7,0.1))

plt.show()

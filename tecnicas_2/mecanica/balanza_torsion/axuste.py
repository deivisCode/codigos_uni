
import numpy as np
import numpy.typing as npt  # opcional, pa especificar os tipos de datos nas funcions
import scipy.optimize as sco
import matplotlib.pyplot as plt

pi = np.pi  # para non andar escribindo 'np.' todo o rato

# Neste caso consideramos que os datos estaban gardados por filas en dous
# arquivos diferentes, un arquivo para cada serie de datos. É posible ordenalos
# deste xeito de diferentes maneiras, no meu caso usei o arquivo
# limpar_datos.py porque orixinalmente tiña os datos en formato CSV.
posicions_1 = np.loadtxt(r"datos\datos_1_estirados.csv")
posicions_2 = np.loadtxt(r"datos\datos_2_estirados.csv")
posicions = [posicions_1,posicions_2]

# Para analizar os datos e tamén graficalos é necesario ter os valores dos
# tempos. No noso caso simplemente tomamos medidas das posicións e consideramos
# os tempos como unha lista equispaciada de valores e con incertezas iguales.
# Para ambos casos tomamos medidas cada 10s, pero por ser un número diferente
# de medidas, fai falta crear eixos 'x' con valores diferentes. Usando
# np.arange creo arrays empezando en 0 e acabando en 10 * (numero de medidas).
# Se hai 178, empeza en 0 e acaba en 1780. Obviamente os valores van de 10 en
# 10
tempos = [
    np.arange(0,10*len(posicions_1),10),
    np.arange(0,10*len(posicions_2),10)
]

# Agora os arrays cas incertezas
incertezas = [
    np.array([1.0]*len(posicions_1)),
    np.array([1.0]*len(posicions_2))
]

# A funcion exponencial a axustar
def exponencial(
    t: npt.ArrayLike, y0: float, A: float, gamma: float, w: float, phi: float
) -> float:
    """Funcion exponecial decrecente que se pide na memoria da práctica.

    t     : Array cos tempos
    y0    : Punto de equilibrio
    A     : Amplitude máxima
    gamma : O coeficiente aquel (non sei que e XD)
    w     : frecuencia de oscilación
    phi   : fase inicial"""
    y = y0 + A * np.exp(-gamma * t) * np.sin(w * t + phi)
    return y

# Parámetros iniciales na mesma orden na que aparece na función que logo se vai
# axustar, é dicir: (y0,A,gamma,w,phi). Deben ser razonables para que se poida
# axustar. Pa eso podese graficar primeiro os datos, ou mirar o que se ten
# apuntado na libreta do lab, pa ter unha idea.
parametros = [
    (145,80,0.01,0.003,1), # parametros da primeira serie
    (155,-50,0.01,0.003,np.pi) # e da segunda
]

# Agora axustamos os nosos datos con curvefit. A función devolve unha tupla con
# dous valores, o primeiro é outra tupla cos parámetros optimizados e o segundo
# unha matriz de covarianzas, onde a raíz da súa diagonal nos da as incertezas
# dos parámetros
axustes = []
parametros_axustados = []
posicions_axustadas = []
incertezas_parametros_axustados = []
for i in range(2):
    axustes.append(
        sco.curve_fit(
            exponencial,  # Primeiro metemos a funcion que queremos axustar
            tempos[i],  # Os valores 'x' que acepta a funcion, experimentales
            posicions[i],  # Os valores 'y' que devolve a funcion, experimentales
            p0 = parametros[i],  # Parmámetros iniciales de proba
            sigma = incertezas[i],  # Erro no eixo 'y'
            absolute_sigma = True,  # Erro absoluto (si) ou relativo
        )
    )
    # Meto os parámetros axustados na lista correspondente
    parametros_axustados.append(axustes[i][0])
    # Temos os parámetros axustados. Agora rulamos a funcion exponencial con
    # eles pa obter unha curva ben suaviña (esperemos)
    posicions_axustadas.append(
        exponencial(
            # Eixo x. Poderíamos crear outro array con mais puntos se fose
            # necesario
            tempos[i],
            parametros_axustados[i][0], # punto de equilibrio
            parametros_axustados[i][1], # amplitude
            parametros_axustados[i][2], # gamma
            parametros_axustados[i][3], # omega
            parametros_axustados[i][4], # phi
        )
    )
    # Finalmente, tamén nos van ser útiles as incertezas dos parámetros
    # axustados. Recordar que o segundo elemento que nos devolve scipy.optimize
    # é unha matriz de covarianzas. A raíz da súa diagonal contén as incertezas
    # (varianzas) que queremos
    incertezas_parametros_axustados.append(
        np.sqrt(np.diag(axustes[i][1]))
    )

# Tamén é interesante ter a diferenza entre o valor experimental e o axustado
# (residuo)
residuos = [
    posicions[0] - posicions_axustadas[0],
    posicions[1] - posicions_axustadas[1]
]

# Vai ser util ter as frecuencias angulares máis a man
W = [
    parametros_axustados[0][3],
    parametros_axustados[1][3],
]
# E súas incertezas
sW = [
    incertezas_parametros_axustados[0][3],
    incertezas_parametros_axustados[1][3],
]
# Primeiro creo listas de python e agora pasoo a array porque me gusta máis
# facer .append() en listas que en ndarrays (vicio meu, sin máis)
W  = np.array(W)
sW = np.array(sW)
T  = 2 * pi / W
sT = 2 * pi * sW / (W ** 2)

# Finalmente, nosas frecuencias e periodos, en unidades do SI
frecuencia_angular = np.mean(W)
incerteza_frecuencia_angular = np.std(W) ** 2
periodo = 2 * pi / frecuencia_angular
incerteza_periodo = 4 * pi * incerteza_frecuencia_angular / (frecuencia_angular**2)

# Un dato hiper importante, a diferenza de posicións de equiibrio.
# Corresponden aos parámetros axustados, na posición 0 de cada serie de datos
posicions_equilibrio = [parametros_axustados[0][0], parametros_axustados[1][0]]
incertezas_posicion_equilibrio = [
    incertezas_parametros_axustados[0][0],
    incertezas_parametros_axustados[1][0],
]

# E as diferenzas, no SI
dx = abs(posicions_equilibrio[1] - posicions_equilibrio[0]) /100
sdx = np.sqrt(posicions_equilibrio[1] ** 2 + posicions_equilibrio[0] ** 2) / 100


# Agora unha parte puñetera. Fannos falta moitos datos e constantes pa calcular
# G. Aquí unha lista completa. En xeral á hora de programar débense usar nomes
# suxerentes e fácilemte distinguibles para as variables. Cousas como 'v', 'b'
# ou monosílabos similares non son aceptables, a pesar da mala costumbre que
# teñen os profesores de informática para científicos. Sin embargo, neste caso
# penso (igual me equivoco) que é razonable facelo así, xa que estas variables
# se escriben igual (ou moi parecido) en papel. Por exemplo 'M' -> unha masa
# grande, 'sM' -> s(M) (varianza de M) 'd' -> distancia, sd -> s(d) (varianza
# de d). NOTA: non recordo de donde saquei os datos (do lab, si) asique non vos
# fiedes moito
M   = 1.5             # kg, masa grande
sM  = 0.01            # kg
R   = 0.03158         # m, radio medio esferas grandes
sR  = 0.00001         # m
r   = 0.0082          # m, radio medio esferas pequenas
sr  = 0.0001          # m
m   = M * (r/R)**3    # kg, masa pequena, calculada coa densidade das bolas
sm  = 0.001           # kg
d   = 0.050           # m, distancia eixo de xiro ao centro das masas pequenas
sd  = 0               # m
L   = 5.809           # m, distancia espello-pared
sL  = 0.014           # m
b   = R + r + 0.002   # m, distancia bolas pequenas e grandes
sb  = 0.001           # m

# constante do resorte e incertezas
k   =    ( 8 * (pi**2) * m * (d**2)) / (periodo**2)  # (kg·m^2·s^-2)
k_T =  - ( 8 * (pi**2) * m * (d**2)) / (periodo**3)  # (kg·m^2·s^-2), k respecto de T
k_m =    ( 8 * (pi**2) * (d**2))     / (periodo**2)  # (m^2·s^-2), k respecto de m
sk  = np.sqrt((k_m * sm) ** 2 + (k_T * sT) ** 2)     # (kg·m^2·s^-2), incerteza de k

# a 'beta' aquela, tampouco me acordo de qué era
beta = (b**3) / ((b**2 + 4 * (d**2)) ** (3 / 2))
sbeta = 0 # non recordo por qué pero digo que é 0

# Agora a parte máis puñetera. A constante G. Aplicando a fórmula directamente:
def constante_G(
    distancia_bolas: float,
    distancia_eixo_xiro: float,
    diferenza_equilibrio: float,
    masa_grande: float,
    distancia_parede: float,
    periodo: float,
    beta: float,
) -> float:
    """Calcula a constante G

    distancia_bolas (b) : distancia entre bolas pequenas e grandes
    distancia_eixo_xiro (d) : distancia eixo de xiro ao centro das masas pequenas
    diferenza_equilibrio (dx) : diferenza na posición de equillibrio
    masa_grande (M) : masa grande
    distancia_parede (L) :  distancia espello-parede
    periodo (T) : periodo de oscilación do pendulo
    beta : non sei que e beta
    """
    G = (pi**2 * distancia_bolas * diferenza_equilibrio) / (
        masa_grande * distancia_parede * periodo**2 * (1 - beta)
    )

    print(periodo)

    return G

G = constante_G(b,d,dx,M,L,periodo,beta)

def incerteza_constante_G(
    distancia_bolas: float,
    distancia_eixo_xiro: float,
    diferenza_equilibrio: float,
    masa_grande: float,
    distancia_parede: float,
    periodo: float,
    beta: float,
    incerteza_distancia_bolas: float,
    incerteza_distancia_eixo_xiro: float,
    incerteza_diferenza_equilibrio: float,
    incerteza_masa_grande: float,
    incerteza_distancia_parede: float,
    incerteza_periodo: float,
    incerteza_beta: float
) -> float:
    """ Calcula a incerteza da constante G por propagación

    distancia_bolas (b) : distancia entre bolas pequenas e grandes
    distancia_eixo_xiro (d) : distancia eixo de xiro ao centro das masas pequenas
    diferenza_equilibrio (dx) : diferenza na posición de equillibrio
    masa_grande (M) : masa grande
    distancia_parede (L) :  distancia espello-parede
    periodo (T) : periodo de oscilación do pendulo
    beta : non sei que e beta

    As variables finales son as incertezas na mesma orde aqui escrita
    """

    # Para a sua incerteza, hai que calcular MOITAS derivadas, asique creo varias
    # variables e vamos pouco a pouco.

    # G respecto a b
    parcial_b    = ( (pi ** 2) *  2 * b   * d * dx     ) /  (  M    *    L    *   (periodo ** 2) * (1-beta) )
    # G respecto a dx
    parcial_dx   = ( (pi ** 2) * (b ** 2) * d          ) /  (  M    *    L    *   (periodo ** 2) * (1-beta) )
    # G respecto a M
    parcial_M    = ( (pi ** 2) * (b ** 2) * d * dx     ) /  ( (M ** 2) * L    *   (periodo ** 2) * (1-beta) )
    # G respecto a L
    parcial_L    = ( (pi ** 2) * (b ** 2) * d * dx     ) /  (  M    *  (L ** 2) * (periodo ** 2) * (1-beta) )
    # G respecto a T
    parcial_T    = ( (pi ** 2) * (b ** 2) * d * dx * 2 ) /  (  M    *    L    *   (periodo ** 3) * (1-beta) )
    # G respecto a beta
    parcial_beta = ( (pi ** 2) * (b ** 2) * d * dx     ) /  (  M    *    L    *   (periodo ** 2) * ((1-beta) ** 2))

    return np.sqrt(
        parcial_b * incerteza_distancia_bolas * 2
        + parcial_dx * incerteza_diferenza_equilibrio ** 2
        + parcial_M * incerteza_masa_grande ** 2
        + parcial_L * incerteza_distancia_parede ** 2
        + parcial_T * incerteza_periodo ** 2
        + parcial_beta * incerteza_beta ** 2
    )

sG = incerteza_constante_G(
    b, d, dx, M, L, periodo, beta, sb, sd, sdx, sM, sL, periodo, sbeta
)


# E con esto xa estaría. Sin embargo, por desgracia tamén piden que calculemos ante qué
# variable é mais sensible 'G'. Personalmente o que fixen foi incrementar as
# incertezas nun 10% e logo ver en qué caso hai mais diferenza
# incremento_b    = sb    + 0.1 * sb
# incremento_dx   = sdx   + 0.1 * sdx
# incremento_M    = sM    + 0.1 * sM
# incremento_L    = sL    + 0.1 * sL
# incremento_T    = incerteza_periodo    + 0.1 * incerteza_periodo
# incremento_beta = sbeta + 0.1 * sbeta

# E gardamos os datos nun ficheiro
with open("resultados.txt",'w') as ficheiro:
    ficheiro.write(f"{G}\n")
    ficheiro.write(f"{sG}")


# APARTADO GRÁFICO ================

# Pos toca a parte bonica, graficar

# Unha ventana pa poñer cousas
ventana = plt.figure("Ventana de datos",figsize=(9,5), dpi=150)

# Con esto creo 3 lenzos, onde o primeiro ten o doble de altura co resto
lenzos = ventana.subplots(
    nrows = 3,
    ncols = 1,
    height_ratios = (2,1,1),
    sharex = True # Pa que teñan os mesmos valores no eixo 'x'
)

cores = ("blue","red")
marcadores = ("b_", "r_")  # os marcadores que quero usar, bonitos
for i in range(2):

    # Primeiro os axustes e os datos experimentales, ne mesma fila
    lenzos[0].plot(tempos[i],posicions_axustadas[i],color="gray")
    lenzos[0].plot(tempos[i],posicions[i],color=cores[i],marker='.',linestyle='')

    # Logo os residuos, nas segundas e terceiras filas
    lenzos[i+1].stem(
        tempos[i], residuos[i], linefmt="gray", markerfmt=marcadores[i], basefmt="k"
    )

# Poño esto pa que os lenzos dos residuos teñan os mesmos eixos 'y'
# e para que se vexa ven colocado horizontalmente
lenzos[1].sharey(lenzos[2])
lenzos[1].set_xlim([-20,180*10])
lenzos[2].set_xlabel("Tempos (s)")

# ventana.savefig("imaxe_preciosa.png")
# plt.show()

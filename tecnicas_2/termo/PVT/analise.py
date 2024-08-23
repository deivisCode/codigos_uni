import numpy as np
import numpy.typing as npt  # opcional, pa especificar os tipos de datos nas funcions
# import matplotlib.pyplot as plt
import scipy.optimize as sco
# from scipy.interpolate import CubicSpline
from regresion_lineal import regresion
# import pandas as pd

# Á hora de tomar os datos o que eu fixen foi ir gardando pares de valores de
# volumen e presion por FILAS, en contra do standard de tidydata. Meto todas as
# series nunha lista, así logo poderemos iterar por ela pa facer cousas, en vez
# de escribir as cousas 12 veces (hai 12 series)
series = [
    np.loadtxt(r"datos\t_10.numpydata"   , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_12_3.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_14_1.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_17_8.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_22.numpydata"   , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_25_9.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_27_8.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_29_8.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_31_3.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_31_9.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_32_5.numpydata" , dtype=np.float64, delimiter=","),
    np.loadtxt(r"datos\t_35.numpydata"   , dtype=np.float64, delimiter=",")
]
cantas_series = len(series)

# As temperaturas
temperaturas = np.loadtxt(r"datos\temperaturas.numpydata")

# Por desgracia todos estos datos de P e V están nun sistema de unidades
# arcaico e descoñecido (bar e mL) asique hai que pasalos ao SI
for i in range(cantas_series):
    series[i][0] = series[i][0] / (10 ** 6) # Volumes. mL -> m^3
    series[i][1] = series[i][1] * (10 ** 5) # Presions. bar -> Pa

# Agora gardo estos datos ben colocadiños. Así poderemos usalos noutros programillas
for i in range(cantas_series):
    np.savetxt(rf"resultados\serie_{i+1}_volumen_presion.txt",series[i])


# A continuacion as incertezas. Considerámolas de 0.1 mL e 0.1 bar
sv = 0.1 / (10 ** 6) # m^3, incerteza no volumen
sp = 0.1 * (10 ** 5) # Pa, incerteza na presion

# E a constante dos gases
R = 8.31446261815324  # J / mol K , Tabulada pola wikipedia

# CACLULO DOS MOLES ===========================

# Hai que coller os datos da zona de baixa presion. Esto é algo feito a ollo,
# asique é recomendable facer algunha mini gráfica antes para elixilos ben. No
# meu caso, collin os datos onde os volumes eran maiores de 0.0000032 m^3
limite_ideal = 0.0000032

# É necesario truncar os datos, asique creo unha lista nova e vou metendo as
# cousas ahí
series_zona_ideal = []
for serie in series:
    # unha lista tempora onde meterei os dous arrays de V e P limitados
    temp = []
    # Unhas aclaracións. 'serie' evidentemente corresponde a cada serie de
    # datos, cada unha composta por dous arrays, V e P, polo que serie[0] é o
    # volumen e serie[1] a presion. A comparación entre corchetes,
    # serie[0]>limite_ideal, devolve un array do tipo
    # [False,False,False,...,False,True,True]. Podemos usar esto para
    # seleccionar elementos dun array que cumplen certa condición, facendo
    # meu_array[ expresion ] que será un array creado a partir de 'meu_array'
    # pero collendo solo os elemento nas mesmas posicións que os valores True
    # da expresión. No noso caso, serie[0][ serie[0] > limite_ideal ].
    temp.append(serie[0][ serie[0] > limite_ideal ])
    temp.append(serie[1][ serie[0] > limite_ideal ])
    series_zona_ideal.append(np.array(temp))

# E borro esta variable porque xa na necesito
del(temp)

# Tamén o gardo en ficheiros aparte
for i in range(cantas_series):
    np.savetxt(rf"resultados\serie_{i+1}_volumen_presion_ideal.txt",series_zona_ideal[i])


# REGRESIONS LINEALES PARA OS MOLES

# Como temos todos os datos en listas podemos coller e iterar cun bucle
# facilmente pa facer as regresions de golpe. Neste caso uso unha funcion que
# fixen eu, importada ao comezo. A funcion 'regresion' devolve datos da forma
# (ordenada, erro ordenada, pendente, erro pendente). Ao rematar o bucle,
# deberíamos ter unha lista de listas, do tipo
#
# regresions_moles = [
# (ordenada, erro ordenada, pendente, erro pendente) # serie 1
# (ordenada, erro ordenada, pendente, erro pendente) # serie 2
# (ordenada, erro ordenada, pendente, erro pendente) # serie 3
# ... etc.
# ]
#
# O que nos interesa son os moles, é dicir, os elementos nas posicións '2'
# (pendente) de cada serie, e súas incertezas, na posición '3'


regresions_moles = []
moles = []
incerteza_moles = []
for temperatura, serie in zip(temperaturas,series_zona_ideal):

    regresions_moles.append(
        regresion(
            R * temperatura * (1 / serie[0]), # valores 'x', RT/V
            serie[1], # valores 'y', P
            [sp] * len(serie[1]) # incerteza no eixo 'y', s(P)
        )
    )

# Convirto esto nun array porque será máis cómodo
regresions_moles = np.array(regresions_moles)
np.savetxt(r"resultados\regresions_moles.txt",regresions_moles)

# O noso array debería verse algo tal que así:
#
# [[ 1.5244800e+05  3.8070605e+04  1.9911528e-03  5.8224115e-05]
#  [ 4.5184000e+04  3.8071383e+04  2.2315979e-03  5.7776164e-05]
#  [ 7.8400000e+03  3.8071051e+04  2.3393035e-03  5.7393303e-05]
#  [ 4.7616000e+04  3.8071402e+04  2.3154616e-03  5.6663583e-05]
#  [ 2.0764800e+05  3.8071395e+04  2.1564960e-03  5.6430708e-05]
#  [ 2.6758400e+05  3.8070703e+04  2.0768046e-03  5.5685934e-05]
#  [ 1.9315200e+05  3.8070754e+04  2.1954179e-03  5.4778891e-05]
#  [-3.4048000e+04  3.8070754e+04  2.3653507e-03  5.4778891e-05]
#  [ 3.6704000e+04  3.8071184e+04  2.2712946e-03  5.3795873e-05]
#  [ 1.2777600e+05  3.8071184e+04  2.1821260e-03  5.3795873e-05]
#  [ 6.0576000e+04  3.8070754e+04  2.3640990e-03  5.4778891e-05]
#  [ 2.4124800e+05  3.8070754e+04  2.1531582e-03  5.4778891e-05]]
#
# onde a terceira columna son as pendentes (moles)

# Meto os moles nun array propio para simplificar a vida
moles = regresions_moles[:,2]
incertezas_moles = regresions_moles[:,3]

# Deberíase obter un array como este con tantos valores como series teñamos
# moles = [0.00199115  0.00218213   ...   0.0023641  0.00215316]

# Para a media, calcúloa normalmente. Para a incerteza, como non sei
# estadística, sácolle a varianza directamente
media_moles = np.mean(moles)  # 0.0022201885
incerteza_media_moles = np.std(moles) ** 2  # 1.2618173e-08
np.savetxt(r"resultados\moles.txt",np.vstack([media_moles,incerteza_media_moles]))

# Para a masa da sustancia necesitamos a masa molar do etano, a cal está
# tabulada
masa_molar_etano = 0.03007 # kg / mol
masa_etano = masa_molar_etano * media_moles


# Cálculo dos coeficientes esos do virial. Ollo aquí usamos volumes molares
# (m^3/mol). A fórmula é
#
# Pv/RT - 1 = B / v
#
# Axustarei a unha recta da forma y = mx sendo y:= PV/RT-1, m:=B e x:=1/v
virial_x = []
virial_y = []
incertezas_virial_y = []

for serie,temperatura in zip(series_zona_ideal,temperaturas):

    virial_x.append( # 1 / v
        1 / (serie[0] / media_moles)
    )

    virial_y.append( # P * v / R * T - 1
        serie[1] * (serie[0] / media_moles) / (R * temperatura) - 1
    )

    incertezas_virial_y.append( # intertezas en y, por propagacion
        (1 / (R * temperatura))
        * np.sqrt(
            (serie[0] / media_moles) ** 2 * sp **2
            + serie[1] ** 2 * sv ** 2
        )
    )

# Como sempre, paso estas listas a arrays. Pa que quede claro, 'virial_x' é
# unha lista de arrays. Cada array corresponde a unha serie de datos. Cada
# array ten 16 (creo) datos, que corresponden aos 16 valores que temos na zona
# ideal. En total temos 12 arrays (series). As 3 variables seguintes teñen a
# mesma estructura
virial_x = np.array(virial_x)
virial_y = np.array(virial_y)
incertezas_virial_y = np.array(incertezas_virial_y)

regresions_virial = []
for i in range(cantas_series):

    regresions_virial.append(
        regresion(
            virial_x[i],
            virial_y[i],
            incertezas_virial_y[i],
        )
    )

regresions_virial = np.array(regresions_virial)

# gardo os datos pa usalos cos outros programas
np.savetxt(r"resultados\virial_x.txt",virial_x)
np.savetxt(r"resultados\virial_y.txt",virial_y)
np.savetxt(r"resultados\incertezas_virial_y.txt",incertezas_virial_y)
np.savetxt(r"resultados\regresions_virial.txt",regresions_virial)

# Os axustes deberían ser da forma
#
# [[ 1.0902393e-01  2.6196459e-02 -1.7296689e-04  4.2094453e-05]
#  [ 6.8544388e-02  2.5995016e-02 -5.2490272e-05  4.1770763e-05]
#  [ 6.6852570e-02  2.5822632e-02 -1.2690201e-05  4.1493768e-05]
#  [ 1.0715103e-01  2.5493862e-02 -5.2141026e-05  4.0965475e-05]
#  [ 2.4980354e-01  2.5389688e-02 -2.2573769e-04  4.0798084e-05]
#  [ 2.8206635e-01  2.5054663e-02 -2.7494505e-04  4.0259743e-05]
#  [ 2.3986626e-01  2.4646608e-02 -2.0311400e-04  3.9604052e-05]
#  [ 2.3254395e-02  2.4646521e-02  3.2335520e-05  3.9603907e-05]
#  [ 6.7592621e-02  2.4204513e-02 -3.4239143e-05  3.8893657e-05]
#  [ 1.5032959e-01  2.4203796e-02 -1.3899244e-04  3.8892504e-05]
#  [ 1.4620399e-01  2.4646334e-02 -6.8034977e-05  3.9603616e-05]
#  [ 2.7980423e-01  2.4646668e-02 -2.4802983e-04  3.9604147e-05]]

# Os coeficientes B do virial correspóndense ás pendentes, é dicir, a terceira
# columna. E súas incertezas na última
coef_B_virial = regresions_virial[:,2]
incertezas_coef_B_virial = regresions_virial[:,3]

# A media será
media_B = np.mean(coef_B_virial)
incerteza_media_B = np.std(coef_B_virial) ** 2

# Agora o axuste de Van der Waals

# Será necesario usar curvefit para realizar o axuste. Para eso necesitamos
# meterlle unha funcion que queremos axustar, os valores x,y e os parámetros
# iniciales. O problema é que temos unha función de 3 variables (P,V,T) e 2
# constantes (a,b). Usando curvefit só lle poderíamos meter 2 variables (e.g.
# volumen na 'x' e presión na 'y'), e deberíamos meter a restante (temperatura)
# como un dos parámetros adicionales. Sin embargo, non o considerei aceptable
# porque a temperatura é un dato experimental. O que fixen foi definir unha
# funcion dentro doutra función. Sinceramente non me vexo capaz de explicar
# esto (levo unhas 20 e pico horas desperto), pódese buscar en google como
# 'nested/inner/encapsulated functions'. (O de chamalo 'xerador' é cousa miña,
# con malo pos nomes)
def xerador_van_der_waals(t: float) -> npt.ArrayLike:
    """Calcula o valor da presion en funcion do volumen
    molar e da temperatura.

    t : temperatura
    v : volumen molar
    a,b : constantes da ecuación

    Esta función usa encapsulación.
    Os primeiros parámetros son (t)
    Os da funcion interior son (v,a,b)"""

    def van_der_waals(v: npt.ArrayLike,a,b):

        R = 8.31446261815324  # J / mol K , Tabulada pola wikipedia
        presion = (R * t)/(v - b) - a/(v**2)

        return presion

    return van_der_waals

# Como somos espabilados e sabemos que ten que dar,
# podemos partir directamente dos parámetros optimizados tabulados para
# asegurarnos de que curvefit furrule. Os valores tabulados son
parametros_correctos = (0.5562,0.0000638) # a, b, no sistema internacional

# Agora iteramos normalmente.
axustes_vdw = []
parametros_optimizados = []
incertezas_parametros_optimizados = []
for serie,temperatura in zip(series,temperaturas):

    axustes_vdw.append(
        sco.curve_fit(
            xerador_van_der_waals(temperatura),
            serie[0] / media_moles,
            serie[1],
            p0 = parametros_correctos,
            sigma = [sp] * len(serie[1]),
            absolute_sigma = True
        )
    )

    parametros_optimizados.append(axustes_vdw[-1][0])

    incertezas_parametros_optimizados.append(
        np.sqrt(np.diag(axustes_vdw[-1][1]))
    )

parametros_optimizados = np.array(parametros_optimizados)
incertezas_parametros_optimizados = np.array(incertezas_parametros_optimizados)

# Neste caso gardo os dous arrays estackeados horizontalmente
np.savetxt(
    r"resultados\axuste_vdw.txt",
    np.hstack((parametros_optimizados, incertezas_parametros_optimizados)),
)

# Que debería verse tal que así
#
#       a                 b               s(a)           s(b)
# [[ 5.72684379e-01  6.50212212e-05  2.50379583e-04  2.44405568e-08]
#  [ 5.63826019e-01  6.41740311e-05  2.55750623e-04  2.55524003e-08]
#  [ 5.57555888e-01  6.35848329e-05  2.59141022e-04  2.62788015e-08]
#  [ 5.49536432e-01  6.25344818e-05  2.65352592e-04  2.75862606e-08]
#  [ 5.44824850e-01  6.40407648e-05  4.45057616e-04  6.29842378e-08]
#  [ 5.26045129e-01  6.14219598e-05  4.72857673e-04  7.01970654e-08]
#  [ 5.19751236e-01  5.94882576e-05  4.93381804e-04  7.52982440e-08]
#  [ 5.19499864e-01  5.98157237e-05  4.97111577e-04  7.51449856e-08]
#  [ 5.02135384e-01  5.47210440e-05  8.88360577e-04  1.73395473e-07]
#  [ 3.14474474e-01 -2.93604925e-08  2.11296134e+00  8.29918624e-04]
#  [ 3.03528812e-01  8.31609329e-09  1.32958716e+00  5.31555711e-04]
#  [ 2.64412643e-01 -3.19707305e-09  5.05079647e-01  2.01928174e-04]]

parametro_a = parametros_optimizados[:,0]
parametro_b = parametros_optimizados[:,1]

incerteza_parametro_a = incertezas_parametros_optimizados[:,0]
incerteza_parametro_b = incertezas_parametros_optimizados[:,1]


media_a = np.mean(parametro_a[:9])
incerteza_media_a = np.std(media_a) ** 2

media_b = np.mean(parametro_b[:9])
incerteza_media_b = np.std(media_b) ** 2


# densidades

temp_critica = 304.55

campana_entrada = np.loadtxt(
    r"datos\campana_entrada.numpydata",
    unpack = True,
    delimiter = ','
)
v_campana_entrada = campana_entrada[0] / (10 ** 6)
p_campana_entrada = campana_entrada[1] * (10 ** 5)

campana_salida = np.loadtxt(
    r"datos\campana_salida.numpydata",
    unpack = True,
    delimiter = ','
)
v_campana_salida = campana_salida[0] / (10 ** 6)
p_campana_salida = campana_salida[1] * (10 ** 5)


# As incertezas, a ollo
incerteza_v_campana_entrada = 0.25e-7 # en m^3 directamente, a ollo
incerteza_v_campana_salida = 1.5e-7 # en m^3 directamente, a ollo
incerteza_p_campana_entrada = 0.01e6 # incerteza presions ao entrar na campana

densidades_entrada = masa_etano / v_campana_entrada
incerteza_densidades_entrada = np.sqrt(
    masa_etano * incerteza_v_campana_entrada / (v_campana_entrada ** 2)
)

densidades_salida = masa_etano / v_campana_salida
incerteza_densidades_salida = np.sqrt(
    masa_etano * incerteza_v_campana_salida / (v_campana_salida ** 2)
)

suma_densidades = (densidades_entrada + densidades_salida) / 2
incerteza_suma_densidades = np.sqrt(
    (incerteza_densidades_entrada**2 + incerteza_densidades_salida**2) / 2
)

regresion_densidades = regresion(
    temperaturas[temperaturas < temp_critica],
    suma_densidades,
    incerteza_suma_densidades,
)
ordenada_densidades = regresion_densidades[0]
incerteza_ordenada_densidades = regresion_densidades[1]
pendente_densidades = regresion_densidades[2]
incerteza_pendente_densidades = regresion_densidades[3]


densidades_totales = np.concatenate((densidades_entrada, np.flip(densidades_salida)))
incerteza_densidades_totales = np.concatenate(
    (incerteza_densidades_entrada, np.flip(incerteza_densidades_salida))
)
temperaturas_totales = np.concatenate(
    (
        temperaturas[temperaturas < temp_critica],
        np.flip(temperaturas[temperaturas < temp_critica]),
    )
)

def pol_cuadrado(x,a,b,c):
    return a * (x**2) + b * x + c

axuste_densidades = sco.curve_fit(
    pol_cuadrado,
    densidades_totales,
    temperaturas_totales,
    p0 = (1,1,1),
)

dens_a = axuste_densidades[0][0]
dens_b = axuste_densidades[0][1]
dens_c = axuste_densidades[0][2]

s_dens_a = np.sqrt(np.diag(axuste_densidades[1]))[0]
s_dens_b = np.sqrt(np.diag(axuste_densidades[1]))[1]
s_dens_c = np.sqrt(np.diag(axuste_densidades[1]))[2]

np.savetxt(
    r"resultados\densidades_entrada.txt",
    np.vstack((densidades_entrada, incerteza_densidades_entrada)),
)

np.savetxt(
    r"resultados\densidades_salida.txt",
    np.vstack((densidades_salida, incerteza_densidades_salida)),
)

np.savetxt(
    r"resultados\densidades_suma.txt",
    np.vstack((
        suma_densidades,
        incerteza_suma_densidades,
    ))
)

np.savetxt(
    r"resultados\densidades_coeficientes.txt", np.vstack((dens_a, dens_b, dens_c))
)

np.savetxt(
    r"resultados\densidades_regresion.txt",
    np.vstack((
        pendente_densidades,
        ordenada_densidades,
    ))
)


#
















#

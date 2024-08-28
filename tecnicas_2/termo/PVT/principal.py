import os
import sys
import pathlib

import numpy as np
import scipy.optimize as sco

import funcions

# Este é o arquivo principal do análise de datos da práctica de PVT.
#
# Varias funcions están definidas aparte no arquivo funcions.py.
#
# O arquivo este está feito para que se lle poidan cambiar os datos facilmente.
# Os datos 'crudos' atópanse todos no directorio '.\datos'
#
# Intentei comentalo todo o máximo posible, pero evidentemente de cara ao final
# fun cansándome

# RUTAS E DIRETORIOS =========================================================

# Por si acaso, primeiro consigo as rutas absolutas deste ficheiro, o que logo
# me permitirá cargar ou gardar cousas en sub-directorios de forma segura. Esto
# é porque rutas relativas como '.datos\...' cambian dependendo do sitio desde
# o que se executa python

# Este é o directorio onde ta o ficheiro principal, en ruta absoluta. Logo po
# resto poderemos facer cousas como DIRETORIO_PRINCIPAL +
# "\\subdirectorio\\sub\\sub2"
DIRETORIO_PRINCIPAL = str(pathlib.Path(__file__).parent.resolve())

# CARGAMOS OS DATOS ==========================================================

# Primeiro a ristra de datos das temperaturas
temperaturas = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperaturas.txt")

# e a temperatura crítica
temperatura_critica = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\temperatura_critica.txt")

# Necesitamos todos os datos de V e P. Dependendo da cantidade de series de
# datos que teñamos, teremos máis ou menos ficheiros, asique primeiro
# listámolos todos
nomes_ficheiros = os.listdir(DIRETORIO_PRINCIPAL + "\\datos\\volumes_presions\\")

# Meto todas as series nunha lista, así logo poderemos iterar por ela pa facer
# cousas, en vez de escribir as cousas 12 veces (hai 12 series no meu caso)
series = []
for nome in nomes_ficheiros:
    series.append(
        np.loadtxt(
            DIRETORIO_PRINCIPAL + "\\datos\\volumes_presions\\" + nome,
            dtype     = np.float64,
            unpack    = True, # os datos están por columnas
            delimiter = ",", # separados por comas
        )
    )

# Agora temos todos os datos nuha lista de arrays (unha lista de series).
# Podemos iterar por esta lista para manipular\usar cada serie individualmente.
# Este é o numero de series de datos que tomamos no laboratorio, no meu caso 12
cantas_series = len(series)

# unha pequena comprobación, por si acaso. Resulta ser un erro tipico (polo
# menos para min)
if cantas_series != len(temperaturas):
    print("Comproba a cantidade de datos de V, P e T")
    sys.exit()
else:
    print(f"Hai {cantas_series} series de cada cousa, parece que a cantidade de datos é correcta")

# as incertezas dos volumes e presions. Consideradas CONSTANTES
incerteza_v = funcions.ml_a_m3(
    np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\incerteza_volumen.txt")
)
incerteza_p = funcions.bar_a_pascal(
    np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\incerteza_presion.txt")
)

# E o valor de R
R = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\R.txt")

# Xa están todos os datos cargados. Por desgracia todos estos datos de P e V
# están nun sistema de unidades arcaico e descoñecido (bar e mL) asique hai que
# pasalos ao SI. Uso unha das funcións que están no arquivo aparte
for i in range(cantas_series):
    series[i][0] = funcions.ml_a_m3(series[i][0])      # Volumes. mL -> m^3
    series[i][1] = funcions.bar_a_pascal(series[i][1]) # Presions. bar -> Pa

# Agora que temos os datos nunhas unidades correctas, gardámolos para poder
# usar cando queiramos dende calquer outro programas. Primeiro borro os contidos do
# directorio onde logo gardarei os datos de V e P. Esto faise porque no meu
# caso teño 12 series, pero se tu tes 11 enton reescribirás solo 11 (e quedará
# 1 solta). Eso pode dar problemas. Ollo, usar o paquete 'os' a veces tamén da
# problemas
ficheiros_preexistentes = os.listdir(
    DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI"
)
if len(ficheiros_preexistentes) != 0:
    for ficheiro in ficheiros_preexistentes:
        os.remove( # Estiven tentado a poñer C:\Windows\System32
            DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI\\" + ficheiro
        )

# Agora gardo estos datos ben colocadiños. Así poderemos usalos noutros programillas.
# Ollo, eu estou usando 'os.listdir' para obter os nomes dos ficheiros nun
# directorio. Éstos ordénanse algo raro, tipo 'serie_10', 'serie_11',
# 'serie_12', 'serie_2', 'serie_3', etc. Asique chamarlle con numeros decimales
# faría que logo ao importalos estivesen desordenados. Por eso prefiero
# poñerlle de nome a temperatura correspondente, a cal é unívoca e non xera
# problemas (creo)
for i in range(cantas_series):
    np.savetxt(
        DIRETORIO_PRINCIPAL
        + f"\\resultados\\volumes_presions_SI\\t_{str(temperaturas[i]).replace('.','_')}_volumen_presion.txt",
        np.transpose(series[i]),
    )

# CALCULO DOS MOLES ==========================================================

# Hai que coller os datos da zona de baixa presion. Esto é algo feito a ollo,
# asique é recomendable facer algunha mini gráfica antes para elixilos ben. No
# meu caso, collin os datos onde os volumes eran maiores de 0.0000032 m^3
limite_ideal = funcions.ml_a_m3( np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\limite_ideal.txt") )

# Un problema que aparece aquí é que cada serie pode ter un número diferentes
# de valores por encima do limite. Nunha serie poden ser 13, noutra 16. Esto da
# problemas despois porque me interesa metelo todo nun array perfectamente
# rectangular. Se non quixese facer eso non importaría. Entonces, o que fago é
# crear unha variable 'cantos_elementos_ideales' que teña, valga a redundancia,
# o número de valores na zona ideal. Este número calcúloo solo para unha serie,
# por exemplo pa primeira. Pode que outras series teñan mais valores nesa zona,
# pero non me importa. Logo simplemente haberá que coller ese número de datos
# dos arrays correspondentes.
#
# A comparación entre corchetes, [series[0][0]>limite_ideal], devolve un array
# do tipo [False,False,False,...,False,True,True]. Podemos usar esto para
# seleccionar elementos dun array que cumplen certa condición, facendo
# meu_array[ expresion ] que será un array creado a partir de 'meu_array' pero
# collendo solo os elemento nas mesmas posicións que os valores True da
# expresión. No noso caso, series[0][0][ series[0][0] > limite_ideal ], serán
# os valores de serie[0][0] que cumplen que son maiores que o limite ideal
# antes mencionado. Evidentemente, serie[0][0] é a primeira serie, e a súa
# primeira columna
cantos_elementos_ideales = len(series[0][0][ series[0][0] > limite_ideal])

# Con este número creo un obxeto de tipo 'slice' para logo poder seleccionar
# facilmente os elementos necesarios sen necesidad de estar escribindo
# constantemente cousas como [1:15:1]. Importante recordar a orde dos arrays de
# datos orixinais, primeiro empecei a tomar datos cando V era grande, e logo
# iba diminuindo. Entón, será necesario sacar os datos do COMEZO dos arrays.
corte_ideal = slice(cantos_elementos_ideales)

# É necesario truncar os datos, asique creo unha lista nova e vou metendo as
# cousas ahí
series_zona_ideal = []
for serie in series:
    # unha lista temporal onde meterei os dous arrays de V e P limitados
    temp = []
    # Unhas aclaracións. 'serie' evidentemente corresponde a cada serie de
    # datos, cada unha composta por dous arrays, V e P, polo que serie[0] é o
    # volumen e serie[1] a presion. Uso un obxeto de tipo 'slice' para
    # seleccionar os da zona ideal, os primeiros 15 (por exemplo, non recordo
    # cantos son)
    temp.append(serie[0][corte_ideal])
    temp.append(serie[1][corte_ideal])

    # O de usar fliplr aquí é un punto clave, pero o día que o escribin non o
    # comentei e olvideime de pa qué era
    series_zona_ideal.append(np.fliplr(np.array(temp)))

# Agora gardamos estos datos. Van ser necesarios para representar as regresións
# dos moles e as do virial. Igual que antes, para evitar problemas vacío o
# directorio onde logo gardarei os datos
ficheiros_preexistentes = os.listdir(DIRETORIO_PRINCIPAL + "\\resultados\\volumes_presions_SI_ideales")

if len(ficheiros_preexistentes) != 0:
    for ficheiro in ficheiros_preexistentes:
        os.remove(
            DIRETORIO_PRINCIPAL
            + "\\resultados\\volumes_presions_SI_ideales\\"
            + ficheiro
        )

for i in range(cantas_series):
    np.savetxt(
        DIRETORIO_PRINCIPAL
        + f"\\resultados\\volumes_presions_SI_ideales\\t_{str(temperaturas[i]).replace('.','_')}_volumen_presion_ideal.txt",
        np.transpose(series_zona_ideal[i]),
    )

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

incerteza_moles = []
regresions_moles = []

for temperatura, serie in zip(temperaturas,series_zona_ideal): # amo usar 'zip'

    regresions_moles.append(
        funcions.regresion(
            R * temperatura * (1 / serie[0]), # valores 'x', RT/V
            serie[1], # valores 'y', P
            [incerteza_p] * len(serie[1]) # incerteza no eixo 'y', s(P)
        )
    )

# Convirto esto nun array porque será máis cómodo. E logo gárdoo
regresions_moles = np.array(regresions_moles)
np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\moles_regresions.txt", regresions_moles)

# O noso array de regresions debería verse algo tal que así (ou con datos
# diferentes)
#
# [[ 1.1084800e+05  4.3521004e+04  2.0561218e-03  6.7119261e-05]
#  [ 4.8096000e+04  4.3520586e+04  2.2250414e-03  6.6577806e-05]
#  [ 6.0800000e+02  4.3521316e+04  2.3494363e-03  6.6161723e-05]
#  [ 5.4688000e+04  4.3523098e+04  2.3033619e-03  6.5323016e-05]
#  [ 2.2339200e+05  4.3521570e+04  2.1094680e-03  6.4391206e-05]
#  [ 3.5731200e+05  4.3521148e+04  1.9202828e-03  6.3550848e-05]
#  [ 1.7062400e+05  4.3521004e+04  2.2278428e-03  6.3149426e-05]
#  [-7.0752000e+04  4.3521832e+04  2.4027824e-03  6.2733714e-05]
#  [ 5.0976000e+04  4.3522750e+04  2.2641420e-03  6.2425956e-05]
#  [ 9.1552000e+04  4.3521770e+04  2.2444725e-03  6.2301762e-05]
#  [ 3.9936000e+04  4.3522883e+04  2.3567080e-03  6.2181054e-05]
#  [ 3.0665600e+05  4.3522262e+04  2.0064116e-03  6.1675702e-05]]
#
# onde a terceira columna son as pendentes (moles)

# Para a media, calcúloa normalmente. Para a incerteza, como non sei
# estadística, sácolle a varianza directamente. Recordar que a terceira
# columna, ousexa [:,2] son os moles
media_moles = np.mean(regresions_moles[:,2])
incerteza_media_moles = np.std(regresions_moles[:,2]) ** 2

# e gardo os datos
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\moles_numero.txt",
    np.vstack([media_moles, incerteza_media_moles]),
)

# Para a masa da sustancia necesitamos a masa molar do etano, a cal está
# tabulada e gardada nun dos arquivos de datos
masa_molar_etano = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\masa_molar_etano.txt")
masa_etano = masa_molar_etano * media_moles

# E volvo gardar os datos. Aquí uso 'atleast_1d' porque o dato que quero gardar
# é un array 0-dimensional (un dato solo) e deste xeito pasa a ser un array dun
# elemento (lioso, pero qué lle imos facer)
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\masa_etano.txt",
    np.atleast_1d(masa_molar_etano),
)

# CÁLCULO DAS COUSAS DO VIRIAL ===============================================

# Cálculo dos coeficientes esos do virial. Ollo aquí usamos volumes molares
# (m^3/mol). Imos calcular unhas regresións lineales, unha por cada serie de
# datos (12 no meu caso). Estas regresións fanse usando solo os datos da zona
# 'ideal' que se mencionou antes. O que necesitamos meter na regresion son
# puntos x e y, asique primeiro calcúloos explicitamente segundo a fórmula
#
# Pv/RT - 1 = B / v
#
# sendo y:= PV/RT-1, m:=B e x:=1/v, e a pendente da recta será m:=B
virial_x = []
virial_y = []
incertezas_virial_y = []
regresions_virial = []

for serie,temperatura in zip(series_zona_ideal,temperaturas):

    # datos x
    virial_x.append( # 1 / v
        1 / (serie[0] / media_moles)
    )

    # datos y
    virial_y.append( # P * v / R * T - 1
        serie[1] * (serie[0] / media_moles) / (R * temperatura) - 1
    )

    # incertezas de y. Calculadas por propagacion
    incertezas_virial_y.append(
        (1 / (R * temperatura))
        * np.sqrt(
            (serie[0] / media_moles) ** 2 * incerteza_p **2
            + serie[1] ** 2 * incerteza_v ** 2
        )
    )

    # [-1] porque queremos usar o ultimo que se engadiu
    regresions_virial.append(
        funcions.regresion(
            virial_x[-1],
            virial_y[-1],
            incertezas_virial_y[-1],
        )
    )

# Como sempre, paso estas listas a arrays. Pa que quede claro, 'virial_x' é
# unha lista de arrays. Cada array corresponde a unha serie de datos. Cada
# array ten tantos datos como valores temos na zona ideal. En total temos 12
# arrays (series). As 4 variables seguintes teñen a mesma estructura (abride os
# arquivos, vense ca mesma forma)
virial_x = np.array(virial_x)
virial_y = np.array(virial_y)
incertezas_virial_y = np.array(incertezas_virial_y)
regresions_virial = np.array(regresions_virial)

# Gardo os datos pa usalos cos outros programas
np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_puntos_x.txt"     , virial_x)
np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_puntos_y.txt"     , virial_y)
np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_incertezas_y.txt" , incertezas_virial_y)
np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\virial_regresions.txt"   , regresions_virial)

# Os axustes (virial_regresions.txt) deberían ser da forma
#
# [[ 8.8224173e-02  3.0566696e-02 -1.2873765e-04  4.9967453e-05]
#  [ 7.8329086e-02  3.0319728e-02 -5.9228390e-05  4.9563740e-05]
#  [ 6.9078445e-02  3.0130196e-02 -5.5879354e-06  4.9253911e-05]
#  [ 1.2022209e-01  2.9747007e-02 -6.3363463e-05  4.8627520e-05]
#  [ 2.6028252e-01  2.9323993e-02 -2.5255233e-04  4.7936017e-05]
#  [ 3.4359169e-01  2.8942039e-02 -3.8776547e-04  4.7311634e-05]
#  [ 2.3524857e-01  2.8759362e-02 -1.8510595e-04  4.7013018e-05]
#  [-2.8419495e-03  2.8569760e-02  7.5625256e-05  4.6703070e-05]
#  [ 9.1083527e-02  2.8427616e-02 -5.1496550e-05  4.6470705e-05]
#  [ 1.4139175e-01  2.8372491e-02 -1.0550395e-04  4.6380595e-05]
#  [ 1.2327194e-01  2.8316755e-02 -4.7218055e-05  4.6289490e-05]
#  [ 3.0602455e-01  2.8086768e-02 -3.2687932e-04  4.5913526e-05]]

# Os coeficientes B do virial correspóndense ás pendentes, é dicir, a terceira
# columna. E súas incertezas na última
coef_B_virial = regresions_virial[:,2]
incertezas_coef_B_virial = regresions_virial[:,3]

# A media será
media_B = np.mean(coef_B_virial)
incerteza_media_B = np.std(coef_B_virial) ** 2

# E gardo o numeriño
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\virial_coeficiente_B.txt",
    np.vstack((media_B, incerteza_media_B)),
)

# AXUSTE VAN DER WAALS =======================================================

# Como somos espabilados e sabemos que ten que dar, podemos partir directamente
# dos parámetros optimizados tabulados para asegurarnos de que curvefit
# furrule. Os valores tabulados son
parametros_correctos = (0.5562,0.0000638) # a, b, no sistema internacional

# Agora iteramos normalmente.
axustes_vdw = []
parametros_optimizados = []
incertezas_parametros_optimizados = []

for serie,temperatura in zip(series,temperaturas): # sigo amando usar 'zip'

    axustes_vdw.append(
        sco.curve_fit(
            # checkear a funcion 'xerador_van_der_waals' no arquivo aparte
            funcions.xerador_van_der_waals(temperatura),
            serie[0] / media_moles,
            serie[1],
            p0 = parametros_correctos,
            sigma = [incerteza_p] * len(serie[1]),
            absolute_sigma = True
        )
    )

    # [-1] porque queremos usar o ultimo que se engadiu
    # [0] porque queremos os parámetros
    parametros_optimizados.append(axustes_vdw[-1][0])

    # [-1] porque queremos usar o ultimo que se engadiu
    # [1] porque queremos as incertezas dos parámetros
    incertezas_parametros_optimizados.append(
        np.sqrt(np.diag(axustes_vdw[-1][1]))
    )

# paso esto a arrays
parametros_optimizados = np.array(parametros_optimizados)
incertezas_parametros_optimizados = np.array(incertezas_parametros_optimizados)

# collo os arrays correspondentes aos parámtros a e b
parametro_a = parametros_optimizados[:,0]
parametro_b = parametros_optimizados[:,1]

# e suas incertezas
incerteza_parametro_a = incertezas_parametros_optimizados[:,0]
incerteza_parametro_b = incertezas_parametros_optimizados[:,1]

# calculo a media dos parámetros. Uso os datos por debaixo de Tc porque por
# enriba os axustes tolean
media_a = np.mean(parametro_a[temperaturas < temperatura_critica])
media_b = np.mean(parametro_b[temperaturas < temperatura_critica])

# e as varianzas
incerteza_media_a = np.std(parametro_a[temperaturas < temperatura_critica]) ** 2
incerteza_media_b = np.std(parametro_b[temperaturas < temperatura_critica]) ** 2

# Gardo os datos
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\vdw_coeficientes_a_b.txt",
    np.vstack(([media_a, incerteza_media_a], [media_b, incerteza_media_b])),
)

# Neste caso gardo os dous arrays estackeados horizontalmente
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\vdw_axustes.txt",
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
#
# Firxarse como as últimas 3 filas son mais diferentes (están por riba da Tc)


# ZONA DE COEXISTENCIA =======================================================

# Hai que cargar os datos da zona de entrada e salida da campana. Están
# gardados por filas asique hai que usar 'unpack'. Logo pásoos ao SI
campana_entrada = np.loadtxt(
    DIRETORIO_PRINCIPAL + "\\datos\\campana_entrada.txt",
    unpack = True,
    delimiter = ','
)
v_campana_entrada = funcions.ml_a_m3(campana_entrada[0])
p_campana_entrada = funcions.bar_a_pascal(campana_entrada[1])

campana_salida = np.loadtxt(
    DIRETORIO_PRINCIPAL + "\\datos\\campana_salida.txt",
    unpack = True,
    delimiter = ','
)
v_campana_salida = funcions.ml_a_m3(campana_salida[0])
p_campana_salida = funcions.bar_a_pascal(campana_salida[1])

# non collemos todos os datos, asique logo usarei esto pa truncar cousas
cantos_datos_entrada = len(v_campana_salida)
corte_campana = slice(cantos_datos_entrada)

# Estas son as temperaturas (truncadas) que imos usar
np.savetxt( DIRETORIO_PRINCIPAL + "\\resultados\\campana_temperaturas.txt", temperaturas[corte_campana])

# Tamén cargo as incertezas do volumen e presion. Os da presion na salida non
# os necesito
incerteza_v_campana_entrada = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\campana_incerteza_v_entrada.txt")
incerteza_v_campana_salida  = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\campana_incerteza_v_salida.txt")
incerteza_p_campana_entrada = np.loadtxt(DIRETORIO_PRINCIPAL + "\\datos\\campana_incerteza_p_entrada.txt")

# Necesitamos as densidades e súas incertezas
densidades_entrada = masa_etano / v_campana_entrada
incerteza_densidades_entrada = np.sqrt(
    masa_etano * incerteza_v_campana_entrada / (v_campana_entrada ** 2)
) # por propagación

densidades_salida = masa_etano / v_campana_salida
incerteza_densidades_salida = np.sqrt(
    masa_etano * incerteza_v_campana_salida / (v_campana_salida ** 2)
)

# Gardamos os datos
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\densidades_entrada.txt",
    np.vstack((densidades_entrada, incerteza_densidades_entrada)),
)

np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\densidades_salida.txt",
    np.vstack((densidades_salida, incerteza_densidades_salida)),
)

# 'mitad_densidades' non é mais que d1+d2 / 2
mitad_densidades = (densidades_entrada + densidades_salida) / 2
incerteza_mitad_densidades = np.sqrt(
    (incerteza_densidades_entrada**2 + incerteza_densidades_salida**2) / 2
)

# Gardamos os datos por enésima vez
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\densidades_mitad.txt",
    np.vstack((mitad_densidades, incerteza_mitad_densidades)),
)

# E calculo a regresion lineal correspondente. Ollo, aquí non uso todos os
# datos, trúncoos para non coller os que están por encima da Tc, por enriba de
# ahí non da ben
regresion_densidades = funcions.regresion(
    temperaturas[temperaturas <= temperatura_critica],
    mitad_densidades,
    incerteza_mitad_densidades,
)

# as pendentes e ordenadas e tal son estas
ordenada_densidades = regresion_densidades[0]
incerteza_ordenada_densidades = regresion_densidades[1]
pendente_densidades = regresion_densidades[2]
incerteza_pendente_densidades = regresion_densidades[3]

# gardo os datos estackeados verticalmente
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\densidades_regresion.txt",
    np.vstack((pendente_densidades, ordenada_densidades)),
)

# Eu decidín separar os datos da campana en dous trozos, pero como queremos
# axustar as densidades a unha parábola, deberei arrexuntalos (tal vez o de
# separalos era mala idea, non sei)
densidades_totales = np.concatenate((densidades_entrada, np.flip(densidades_salida)))
incerteza_densidades_totales = np.concatenate(
    (incerteza_densidades_entrada, np.flip(incerteza_densidades_salida))
)

# Non me preguntedes que fixen aquí. Funciona e ala :_)
temperaturas_totales = np.concatenate(
    (
        temperaturas[temperaturas <= temperatura_critica],
        np.flip(temperaturas[temperaturas <= temperatura_critica]),
    )
)

# E finalmente, axusto as densidades a un polinomio de grado 2, definido no
# arquivo aparte
axuste_densidades = sco.curve_fit(
    funcions.pol_cuadrado,
    densidades_totales,
    temperaturas_totales,
    p0 = (1,1,1),
)

# os coeficientes do polinomio
# a * (x**2) + b * x + c
densidade_a = axuste_densidades[0][0]
densidade_b = axuste_densidades[0][1]
densidade_c = axuste_densidades[0][2]

# Gardo solamente os coeficientes e non suas incertezas. Dame pereza
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\densidades_coeficientes.txt",
    np.vstack((densidade_a, densidade_b, densidade_c)),
)

# FINALMENTE clapeyron e calor de vaporizacion

# calculo todo na zona de coexistencia da ENTRADA da campana, por ter mellores datos.
# Importante como collo solamente parte dos datos de temperaturas
axuste_clapeyron = funcions.regresion(
    temperaturas[corte_campana],
    p_campana_entrada,
    [incerteza_p_campana_entrada] * len(temperaturas[corte_campana]),
)
ordenada_clapeyron = axuste_clapeyron[0]
incerteza_ordenada_clapeyron = axuste_clapeyron[1]
pendente_clapeyron = axuste_clapeyron[2]
incerteza_pendente_clapeyron = axuste_clapeyron[3]

# gardo solo os datos da pendente e da ordenada
np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\clapeyron_regresions.txt",
    np.vstack((pendente_clapeyron, ordenada_clapeyron)),
)

# Esto era aplicar as formulillas
delta_v = v_campana_entrada - v_campana_salida
calores = pendente_clapeyron * temperaturas[corte_campana] * delta_v
incerteza_calores = np.sqrt(
    (temperaturas[corte_campana] * delta_v * incerteza_pendente_clapeyron) ** 2
    + (pendente_clapeyron * delta_v * 0.1) ** 2
    + (pendente_clapeyron * temperaturas[corte_campana] * incerteza_v_campana_salida)
    ** 2
)

np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\calores.txt",calores)
np.savetxt(DIRETORIO_PRINCIPAL + "\\resultados\\calores_incerteza.txt",incerteza_calores)


axuste_calores = funcions.regresion(
    temperaturas[corte_campana], calores, incerteza_calores
)
ordenada_calores = axuste_calores[0]
incerteza_ordenada_calores = axuste_calores[1]
pendente_calores = axuste_calores[2]
incerteza_pendente_calores = axuste_calores[3]

np.savetxt(
    DIRETORIO_PRINCIPAL + "\\resultados\\calores_regresions.txt",
    np.vstack((pendente_calores, ordenada_calores)),
)

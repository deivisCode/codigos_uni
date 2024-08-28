![axustes de Van der Waals](imaxe_portada.jpg)

# Estudio PVT dun fluído

Esto é unha serie de programas que calculan multitude de cousas (non todo) da
practica PVT.

**INSISTO, NON É COMPLETO**

## ✨features✨
O arquivo principal fai o seguinte:

- Pasa os datos ao SI
- Calcula o numero de moles mediante regresions lineales
- Calcula o coeficiente 'B' do virial mediante regresions lineales
- Calcula os coeficientes 'a' e 'b' da ecuación de Van der Waals mediante axustes non lineais
- Calcula as densidades do fluido nas zonas de entrada e saida da campana de coexistencia, e axusta os datos a un polinomio de grao 2
- Calcula as regresións lineais dos puntos medios destas densidades
- Calcula as regresions lineais de Clapeyron
- Calcula os calores de vaporizacion
- (creo que nada máis)

Aparte, hai 8 arquivos para realizar as gráficas correspondentes. Penso que se
ven decentes.

## Uso

Crear un entorno virtual normalmente e activalo. En windows powershell:
```
python -m venv venv
.\venv\Scripts\activate
```
Instalar as dependencias con
```pip install -r requirements.txt```

O programa importante é o chamado `principal.py`, éste lee os datos e xera os
resultados principales. Primeiro hai que executar ese, e logo podería
executarse calquera programa das gráficas en calqueira orde.

## Datos

Veñen incluídos os datos que tomamos no lab meu compañeiro e eu. Sodes 100%
libres de usalos sen máis. Para usar datos propios vosos, o único que hai que
toquetear é o diretorio `datos`. Ahí están todos os datos necesarios en
ficheiros diferentes. A estructura é a seguinte:

```
datos
├─ volumes_presions
│  ├─ t_10.csv
│  ├─ t_12_3.csv
│  ├─ ...
│  ├─ t_32_5.csv
│  └─ t_35.csv
├─ incerteza_presion.txt
├─ incerteza_volumen.txt
├─ R.txt
├─ temperatura_critica.txt
├─ temperaturas.txt
├─ campana_entrada.txt
├─ campana_incerteza_v_entrada.txt
├─ campana_incerteza_v_salida.txt
├─ campana_salida.txt
├─ limite_ideal.txt
└─ masa_molar_etano.txt
```

Os únicos ficheiros que non fai falta tocar son os do valor de R e o da masa
molar do etano. O resto hai que tocalos todos

### volumes_presions
Aquí están os ficheiros de texto plano que conteñen arrays de datos tomados por
filas (para seguir o estandar de TidyData). A primeira columna corresponde ao
volumen e a segunda as presións, en mL e bar respectivamente. Cada arquivo
corresponde a unha serie de datos, ousexa a unha temperatura diferente. Para
usar os datos que se tomen no lab, solo hai que reemplazar estos datos. Os
nomes dos ficheiros non son relevantes, o único importante é que se poidan
ordenar automáticamente. Con esto quero dicir que nomes como blabla\_1,
blabla\_2, ... , blabla\_10, blabla_11 NON SON VÁLIDOS, xa que se ordenarían
alfabéticamente primeiro os que teñen o sufixo 1, 10, 11, e logo 2, 3 , etc.
Quitando eso non debería haber problema (esto é culpa da funcion listdir do
paquete os)

### incerteza_presion|volumen.txt
É facil de explicar. Cada ficheiro ten 1 so numero que é a incerteza que
considerei para V e P. Eu supuxen ambas constantes, asique para facelo doutro
modo habería que cambiar medio programa :_(

### R.txt
A constante dos gases. Preferin metela ahí inda que tal vez non
sexa o mellor sitio

### campana_entrada|salida.txt
Son os datos da zona de coexistencia, os valores de volumen e presion gardados
por columnas. Gardei por separado os datos da zona e de entrada e de salida
porque me deu así a venada

### temperaturas.txt
Son os datos por filas das temperaturas en KELVIN

### temperatura_critica.txt
É o valor crítico que consideramos no lab, moi necesario

### limite_ideal.txt
É o valor do volumen por debaixo do cal deixamos de considerar que o
comportamento do gas é ideal

### masa_molar_etano.txt
a masa molar do etano :)

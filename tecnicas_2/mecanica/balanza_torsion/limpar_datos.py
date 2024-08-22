import numpy as np
import pandas as pd

# Importar os datos CSV. Prefiero manter os datos de ambas medicións en variables
# separadas
datos_1 = pd.read_csv(r"datos\datos_1.csv", dtype=np.float64, header=None)
datos_2 = pd.read_csv(r"datos\datos_2.csv", dtype=np.float64, header=None)

# Hai que sumarlle varios centimetros a cada medicion (columna)
desplazamento_1 = (160,80,0,80,160,160,80,80,160,160,80,80,160)
desplazamento_2 = (80,160,160,80,80,160,160,80,80,160,160,80)

# A cada columna súmolle o desplazamento correspondente
for i in range(len(desplazamento_1)):
    datos_1[i] = datos_1[i] + desplazamento_1[i]

for i in range(len(desplazamento_2)):
    datos_2[i] = datos_2[i] + desplazamento_2[i]

# E agora apilo os datos. 'melt' apílaos, 'dropna' elimina os baleiros (Nan), e
# logo usa 'drop' pa eliminar a primeira columna. Esto último faise porque ao
# usar melt créase unha columna adicional ao principio que corresponde aos
# valores do header orixinal
datos_1 = pd.melt(datos_1).dropna().drop(columns=["variable"])
datos_2 = pd.melt(datos_2).dropna().drop(columns=["variable"])

# E finalmente gardo todo en formato CSV
datos_1.to_csv("datos\datos_1_estirados.csv",header=False,index=False)
datos_2.to_csv("datos\datos_2_estirados.csv",header=False,index=False)

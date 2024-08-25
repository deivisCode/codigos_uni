import numpy.typing as npt

def pol_cuadrado(x: npt.ArrayLike, a: float, b: float, c: float) -> npt.ArrayLike:
    """Un polinomio de segundo grado tipico"""
    return a * (x**2) + b * x + c

def ml_a_m3(array: npt.ArrayLike) -> npt.ArrayLike:
    """Pasa de mililitros a metros cubicos"""
    return array / (10**6)

def bar_a_pascal(array: npt.ArrayLike) -> npt.ArrayLike:
    "Pasa de bares a pascales"
    return array * (10**5)

def regresion(datos_x, datos_y, datos_sigma_y) -> tuple[float]:
    """Calcula unha regresion lineal sinxela acorde aos apuntes de estadística
    de Faustino. Só ten en conta o erro no eixo 'y'.

    Devolve unha tupla de datos tipo
    (ordenada, erro ordenada, pendente, erro pendente)
    """

    import numpy as np
    import numpy.linalg as npl

    # pasalo todo a arrays
    x = np.array(datos_x, dtype=np.float32)
    y = np.array(datos_y, dtype=np.float32)
    sigma_y = np.array(datos_sigma_y, dtype=np.float32)

    # tamaños das cousas
    len_x = x.size
    len_y = y.size
    len_sigma_y = sigma_y.size

    if (len_x != len_y) or (len_y != len_sigma_y):
        print("\nChequea as lonxitudes das cousas\n")
        print(f"len(x): {len_x}\nlen(y): {len_y}\nlen(sigma y): {len_sigma_y}")

    # a matriz esa do axuste
    H = np.empty((2, 2), np.float32)

    H[0, 0] = np.sum(np.reciprocal(np.power(sigma_y, 2)))
    H[0, 1] = np.sum(np.divide(x, np.power(sigma_y, 2)))
    H[1, 0] = np.sum(np.divide(x, np.power(sigma_y, 2)))
    H[1, 1] = np.sum(np.divide(np.power(x, 2), np.power(sigma_y, 2)))

    # determinante de H
    det_H = npl.det(H)

    Z = np.empty((2, 1), dtype=np.float32)
    Z[0, 0] = np.sum(np.divide(y, np.power(sigma_y, 2)))
    Z[1, 0] = np.sum(np.divide(np.multiply(x, y), np.power(sigma_y, 2)))

    coeficientes = np.matmul(npl.inv(H), Z)

    a = coeficientes[0, 0]
    b = coeficientes[1, 0]

    sigma_a = np.sqrt(
        np.multiply(
            np.reciprocal(det_H),
            np.sum(np.divide(np.power(x, 2), np.power(sigma_y, 2))),
        )
    )

    sigma_b = np.sqrt(
        np.multiply(np.reciprocal(det_H), np.sum(np.reciprocal(np.power(sigma_y, 2))))
    )

    return (a, sigma_a, b, sigma_b)

# Esta é a funcion que usei para VdW, a cal logo se meterá en curve_fit. Para
# usar curvefit necesitamos meterlle unha funcion que queremos axustar, os
# valores x,y e os parámetros iniciales. O problema é que temos unha función de
# 3 variables (P,V,T) e 2 constantes (a,b). Usando curvefit só lle poderíamos
# meter 2 variables (e.g. volumen na 'x' e presión na 'y'), e deberíamos meter
# a restante (temperatura) como un dos parámetros adicionales a axustar. Sin
# embargo, non o considerei aceptable porque a temperatura é un dato
# experimental. O que fixen foi definir unha funcion dentro doutra función.
# Sinceramente non me vexo capaz de explicar esto (levo unhas 20 e pico horas
# desperto), pódese buscar en google como 'nested/inner/encapsulated
# functions'. (O de chamalo 'xerador' é cousa miña, son malo pos nomes)
def xerador_van_der_waals(t: float) -> npt.ArrayLike:
    """Calcula o valor da presion en funcion do volumen
    molar e da temperatura.

    t : temperatura
    v : volumen molar
    a,b : constantes da ecuación

    Esta función usa encapsulación.
    Os primeiros parámetros son (t)
    Os da funcion interior son (v,a,b)"""

    def van_der_waals(v: npt.ArrayLike, a: float, b: float) -> npt.ArrayLike:
        R = 8.31446261815324  # J / mol K , Tabulada pola wikipedia
        presion = (R * t) / (v - b) - a / (v**2)

        return presion

    return van_der_waals


import numpy as np
import numpy.linalg as npl


def regresion(datos_x, datos_y, datos_sigma_y) -> tuple[float]:
    """Calcula unha regresion lineal sinxela acorde aos apuntes de estadística
    de Faustino. Só ten en conta o erro no eixo 'y'.

    Devolve unha tupla de datos tipo
    (ordenada, erro ordenada, pendente, erro pendente)
    """
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


if __name__ == "__main__":
    datos_x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    datos_y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    datos_sigma_y = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
    print(regresion(datos_x, datos_y, datos_sigma_y))

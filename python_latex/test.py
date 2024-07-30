# Esto so é unha funcion que garda un par de datos nun ficheiro de texto plano,
# separados por comas. Rulando a funcion varias veces podemos engadir máis e
# máis datos. Este arquivo NON é necesario. O importante é o .tex
def garda_dato(valor1, valor2, ficheiro="datos.dat"):
    """Garda unha parexa de datos nun ficheiro específico.

    Os datos gárdanse fila a fila separados por unha coma
    Se o ficheiro xa ten datos, éstos deben ter o formato antes mencionado"""
    import csv
    import os

    # dicionario auxiliar pa gardar os datos do arquivo pre-existente
    dict_datos = {}
    ruta = os.path.join(os.getcwd(), ficheiro)

    # tal vez son moitos try-except...
    try:
        with open(ruta,'r') as file:
            lector = csv.reader(file, delimiter=",")
            # gardamos os datos que xa estén no arquivo
            for fila in lector:
                dict_datos[fila[0]] = fila[1]

    except FileNotFoundError as erro:
        print(f"Non existe arquivo {ruta} anterior")
        print("Intentarase crealo")

    # engadimos o novo dato
    dict_datos[valor1] = valor2

    try:
        # e escribímolos todos outra vez
        with open(ruta, "w") as f:
            for chave in dict_datos.keys():
                f.write(f"{chave},{dict_datos[chave]}\n")

    except IOError as erro: # por se pasa algo raro
        print("Eres tontísimo, toma este erro:\n", erro)


if __name__ == "__main__":
    garda_dato("constante_G", 59)

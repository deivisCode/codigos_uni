# Esto so é unha funcion que garda un par de datos nun ficheiro de texto plano,
# separados por comas. Rulando a funcion varias veces podemos engadir máis e
# máis datos. Esta función non é totalmente necesaria no proceso, simplemente é
# un exemplo. Sempre que teñamos os datos gardados nun ficheiro co formato
# adecuado, e éste se lea correctamente dende LaTeX con datatool, debería estar
# ben (de feito, tamén hai alternativas a datatool)
def garda_dato(nome, valor, erro, unidade, ficheiro="\\resultados.csv"):
    """Garda datos nun ficheiro específico seguindo o formato

    nome,valor,erro,unidades

    Os datos gárdanse fila a fila separados por unha coma
    Se o ficheiro xa ten datos, éstos deben ter o formato antes mencionado"""
    import csv
    import pathlib

    # Esta liña de aquí é para o caso no que se use o paquete qex(f)py (a f é
    # muda) para manexar unidades. O problema é que qexpy por defecto usa o
    # caracter algo peligroso \U+22C5 como simbolo de multiplicacion, o cal
    # python non acepta. Neste caso concreto NON usei qexpy, pero inda así
    # deixoo aquí como comentario
    #
    # unidade = unidade.replace('⋅','.')

    # dicionario auxiliar pa gardar os datos do arquivo pre-existente
    dict_datos = {}

    # ruta das cousas que imos usar
    diretorio = str(pathlib.Path(__file__).parent.resolve())
    ruta_ficheiro = diretorio + ficheiro

    try:
        with open(ruta_ficheiro, "r") as ficheiro:
            filas = csv.reader(ficheiro, delimiter=",")
            # gardamos os datos que xa estén no arquivo
            for fila in filas:
                # Esto é un pequeno chequeo porque cada fila debe ter 4
                # elementos exactamente.
                assert len(fila) == 4, f"\nDebe haber 4 elementos en cada fila!! [nome,valor,erro,unidade]\nSin embargo, a fila {fila} ten {len(fila)} elementos!"

                dict_datos[fila[0]] = {
                    "valor": fila[1],
                    "erro": fila[2],
                    "unidades": fila[3],
                }

    except FileNotFoundError:
        print(f"Non existe arquivo .{ficheiro} anterior")
        print(f"Intentouse crear o arquivo {ficheiro} no diretorio {diretorio}\\")

    # engadimos o novo dato
    dict_datos[nome] = {"valor": valor, "erro": erro, "unidades": unidade}

    try:
        # e escribímolos todos outra vez
        with open(ruta_ficheiro, "w") as ficheiro:
            for chave in dict_datos.keys():
                ficheiro.write(
                    f"{chave},"
                    + f"{dict_datos[chave]['valor']},"
                    + f"{dict_datos[chave]['erro']},"
                    + f"{dict_datos[chave]['unidades']}\n"
                )

    except IOError as error:  # por se pasa algo raro
        print("Eres tontísimo, toma este erro:\n", error)


if __name__ == "__main__":
    garda_dato("VARIABLE_DE_PROBA", 100, 0.1, "m/s^2")

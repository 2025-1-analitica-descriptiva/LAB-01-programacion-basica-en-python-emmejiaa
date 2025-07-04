"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    resultados = {}

    with open("files/input/data.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            col5 = columnas[4].split(",")  # Lista de 'clave:valor'

            for par in col5:
                clave, valor = par.split(":")
                valor = int(valor)

                if clave not in resultados:
                    resultados[clave] = [valor, valor]  # [min, max]
                else:
                    if valor < resultados[clave][0]:
                        resultados[clave][0] = valor
                    if valor > resultados[clave][1]:
                        resultados[clave][1] = valor

    resultado_final = [(clave, resultados[clave][0], resultados[clave][1]) for clave in sorted(resultados)]
    return resultado_final
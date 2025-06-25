"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columnas = line.strip().split("\t")  # usa "\t" si está separado por tabulaciones
            if len(columnas) >= 2:
                try:
                    suma += int(columnas[1])  # usa float() si hay decimales
                except ValueError:
                    continue  # ignora encabezados o líneas inválidas
    return suma
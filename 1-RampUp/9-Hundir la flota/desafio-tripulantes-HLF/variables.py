import numpy as np

filas_por_letras = {chr(ord("A") + i): i for i in range(10)}

barcos = {"Buque de guerra": {"tamano": 4, "cantidad": 1},
    "Submarino": {"tamano": 3, "cantidad": 2},
    "Patrullero": {"tamano": 2, "cantidad": 3},
    "Dron naval": {"tamano": 1, "cantidad": 4}}
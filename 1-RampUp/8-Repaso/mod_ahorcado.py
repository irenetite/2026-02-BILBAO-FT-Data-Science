# el archivo debería llamarse funciones, para otra vez tenerlo en cuenta

import time

def ahorcado(palabra_azar):
    rayas = ["_"]*len(palabra_azar)
    num_errores = []
    perdiste = False
    print(" ".join(rayas))
    while "_" in rayas:
        letra_usuario = input("Escribe una letra:")
        letra_usuario = letra_usuario.lower()
        acierto = False
        if letra_usuario in num_errores or letra_usuario in rayas:
            print("Ya probaste esa letra.")
            continue
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Introduce solo una letra.")
            continue
        for i, letra in enumerate(palabra_azar):
            if letra == letra_usuario:
                rayas[i] = letra
                acierto = True
        if acierto:
            print(" ".join(rayas))
        else:
            print("Esa letra no está.")
            num_errores.append(letra_usuario)
            if len(num_errores) == 6:
                print("Perdiste, fin del juego.")
                perdiste = True
                break
        time.sleep(0.1)
    if perdiste:
        print(f"La palabra era: {palabra_azar}. Cometiste {len(num_errores)} errores: {num_errores}.")
    else:
        print("¡Ganaste!")
        print(f"La palabra era: {palabra_azar}. Cometiste {len(num_errores)} errores: {num_errores}.")
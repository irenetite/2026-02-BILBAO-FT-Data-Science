
# aquí van las funciones auxiliares

def menu_jugador():
    while True:
        print("\n--- MENÚ DEL JUGADOR ---")
        print("1. Disparar")
        print("2. Ver mi tablero con mis barcos y los impactos del enemigo")
        print("3. Ver tablero de la máquina con mis disparos")
        print("4. Salir del juego")
        opcion = input("Elige una opción (1/2/3/4): ").strip()
        
        if opcion in ("1", "2", "3", "4"):
            return opcion
        else:
            print("Entrada no válida. Debes elegir un número del 1 al 4.")



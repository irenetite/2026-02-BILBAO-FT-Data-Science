from clases import Tablero, Jugador
from variables import barcos
from funciones import menu_jugador

# bienvenida al jugador
print("=========================================")
print("      BIENVENIDO A HUNDIR LA FLOTA     ")
print("=========================================\n")
print("Instrucciones:")
print("-Introduce coordenadas para disparar (ej: A5, C9, J0).")
print("-Si aciertas, vuelves a disparar.")
print("-Si fallas, dispara la máquina.")
print("-Gana quien hunda todos los barcos del rival.\n")

# inicializo los tableros
tablero_jugador = Tablero("jugador", barcos)
tablero_maquina = Tablero("maquina", barcos)


# coloco los barcos, solo una vez
tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()

# creo los jugadores
jugador_jugador = Jugador("Jugador", "jugador")
jugador_maquina = Jugador("Máquina", "maquina")

# empezamos:
turno = "jugador"

while True:
    print("\n---------------------------------------")
    print(f"           TURNO DEL {turno.upper()}           ")
    print("---------------------------------------\n")


    if turno == "jugador": # muestro los tableros del jugador al empezar su turno
        print("\n===== TU TABLERO ======")
        tablero_jugador.mostrar(modo="real")
        print()
        print("\n===== TUS DISPAROS =====")
        tablero_jugador.mostrar(modo="disparos")
        print()

        while True: # menú para el jugador
            opcion = menu_jugador()
            if opcion == "1":
                fila, columna = jugador_jugador.coordenadas(tablero_jugador.tablero_disparos)
                print(f"Disparas a {chr(fila + 65)}{columna + 1}")
                acierto = tablero_jugador.disparar(tablero_maquina, jugador_jugador, fila, columna)
                if not acierto:
                    turno = "maquina"
                    break  # sales del menú y termina tu turno si fallas
            elif opcion == "2":
                print("\nTu tablero:")
                tablero_jugador.mostrar(modo="real")
            elif opcion == "3":
                print("\nTablero de la máquina con tus disparos:")
                tablero_jugador.mostrar(modo="disparos")
            elif opcion == "4":
                print("Saliendo del juego...")
                exit()
            else:
                print("Opción no válida.")

        if tablero_jugador.todos_hundidos(tablero_maquina): # ganó el jugador?
            print("\n🎉💃¡GANASTE!💃🎉 Todos los barcos enemigos están hundidos.")
            break

    else: # turno de la máquina
        print("La máquina está disparando...\n")
        acierto = tablero_maquina.disparar(tablero_jugador, jugador_maquina) # la máquina dispara automáticamente
        if not acierto:
            turno = "jugador"
        if tablero_maquina.todos_hundidos(tablero_jugador):
            print("\n💀💀LA MÁQUINA GANÓ💀💀 Todos tus barcos están hundidos.")
            break

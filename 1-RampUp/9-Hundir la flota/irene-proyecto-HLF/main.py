from clases import Tablero, Jugador
from variables import barcos
from funciones import menu_jugador

# bienvenida al jugador
print("=======================================")
print("      BIENVENIDO A HUNDIR LA FLOTA     ")
print("=======================================\n")
print("Instrucciones:")
print("-Introduce coordenadas para disparar (ej: A5, C9, J0).")
print("-Si aciertas, vuelves a disparar.")
print("-Si fallas, dispara la máquina.")
print("-Gana quien hunda todos los barcos del rival.\n")

# inicializo los tableros
tablero_usuario = Tablero("usuario", barcos)
tablero_maquina = Tablero("maquina", barcos)

# coloco los barcos, solo una vez
tablero_usuario.colocar_barcos()
tablero_maquina.colocar_barcos()

# creo los jugadores
jugador_usuario = Jugador("Usuario", "usuario")
jugador_maquina = Jugador("Máquina", "maquina")

# empezamos:
turno = "usuario"

while True:
    print("\n---------------------------------------")
    print(f"           TURNO DE {turno.upper()}           ")
    print("---------------------------------------\n")


    if turno == "usuario": # muestro los tableros del usuario al empezar su turno
        print("\n===== TU TABLERO ======")
        tablero_usuario.mostrar(modo="real")
        print()
        print("\n===== TUS DISPAROS =====")
        tablero_usuario.mostrar(modo="disparos")
        print()

        while True: # menú para el jugador
            opcion = menu_jugador()
            if opcion == "1":
                acierto = tablero_usuario.disparar(tablero_maquina, jugador_usuario)
                if not acierto:
                    turno = "maquina"
                    break  # sales del menú y termina tu turno si fallas
            elif opcion == "2":
                print("\nTu tablero:")
                tablero_usuario.mostrar(modo="real")
            elif opcion == "3":
                print("\nTablero de la máquina con tus disparos:")
                tablero_usuario.mostrar(modo="disparos")
            elif opcion == "4":
                print("Saliendo del juego...")
                exit()
            else:
                print("Opción no válida.")

        if tablero_usuario.todos_hundidos(tablero_maquina): # ganó el jugador?
            print("\n🎉💃¡GANASTE!💃🎉 Todos los barcos enemigos están hundidos.")
            break

        if tablero_maquina.tablero[jugador_usuario.ultima_fila, jugador_usuario.ultima_columna] == " ": 
            turno = "maquina" # si falló, cambia el turno a la máquina

    else: # turno de la máquina
        print("La máquina está disparando...\n")

        acierto = tablero_maquina.disparar(tablero_usuario, jugador_maquina)
        if not acierto:
            turno = "usuario"
        if tablero_maquina.todos_hundidos(tablero_usuario): # ganó la máquina?
            print("\n💀💀LA MÁQUINA GANÓ💀💀 Todos tus barcos están hundidos.")
            break

        if tablero_usuario.tablero[jugador_maquina.ultima_fila, jugador_maquina.ultima_columna] == " ":
            turno = "usuario"  # si la máquina falla, vuelve el turno al usuario
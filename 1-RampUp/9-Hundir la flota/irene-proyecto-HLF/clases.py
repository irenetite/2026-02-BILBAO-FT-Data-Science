import numpy as np
import random
from variables import filas_por_letras

class Jugador: # creo una clase Jugador para diferenciar al usuario y al ordenador
    def __init__(self, nombre, tipo):
        self.nombre = nombre # nombre del jugador u ordenador
        self.tipo = tipo # usuario o máquina
    def coordenadas(self, tablero_disparos=None):
        '''añado el parámetro 'tablero_disparos' para que la máquina pueda consultar
        el tablero donde guarda sus disparos anteriores. El usuario no lo usa,
        pero la máquina sí lo necesita para evitar repetir coordenadas'''
        if self.tipo == "usuario": # si es el usuario, pido coordenadas manualmente
            while True:  # como el usuario puede meter coordenadas erróneas, voy a hace run while que se repite hasta que el usuario meta coordenadas válidas
                coord = input("Introduce las coordenadas de tu disparo (ej: B4, F10): ").upper().strip() # lo pido así porque en el juego, de toda la vida, se han dado las coordenadas por letra y número
                if len(coord) < 2: # longitud mínima, al menos 2 caracteres de letra + número
                    print("No es válido, usa formato como B4 o F10.")
                    continue
                letra = coord[0] # como str es un iterable, digo que el primer índice corresponde a la letra de la fila
                numero = coord[1:] # el resto, que es un número, son las columnas
                if letra not in filas_por_letras: # compruebo que la letra está dentro de mi diccionario
                    print("La fila debe ser una letra entre la A y la J.")
                    continue
                if not numero.isdigit(): # compruebo que es un número entero
                    print("La columna debe ser un número.")
                    continue
                column_num = int(numero)
                if not (1 <= column_num <= 10): # compruebo que es un número del 1 al 10
                    print("La columna debe estar entre el 1 y el 10.")
                    continue
                fila = filas_por_letras[letra] # Si todo es válido, convierto letra a índice para que lo entienda python
                columna = int(numero) - 1 # resto 1 porque quiero que el usuario no se líe, ya que para él lo natural es que las columnas no empiecen por 0, sino por 1
                return fila, columna # devuelvo las coordenadas en índices de python           
        else: # si es la máquina, elige coordenadas aleatorias
            while True: # la máquina elegirá coordenadas aleatorias, pero comprobando antes que no haya disparado ya en esa casilla
                fila = random.randint(0, 9) # desde la fila 0 hasta la fila 9
                columna = random.randint(0, 9) # desde la columna 0 hasta la 9
                if tablero_disparos[fila, columna] == " ": # para que la máquina no repita miramos si en el tablero de disparos de la máquina, esa casilla está vacía (" "). si está vacía, significa que la máquina nunca disparó ahí
                    print(f"El ordenador dispara a {chr(fila + 65)}{columna + 1}") # ahora sumamos 1 porque el ordenador la elegirá con las coordenadas de python
                    return fila, columna # devuelvo las coordenadas en índices de python 
 

class Tablero:
    def __init__(self, id_jugador, barcos):
        self.id_jugador = id_jugador # para saber a quién pertenece el tablero
        self.tablero = np.full((10, 10), " ", dtype=str)  # creo tableri vacío de 10x10 # en este tablero es donde se colocan barcos
        self.tablero_disparos = np.full((10, 10), " ", dtype=str) # el tablero que verá el rival, solo relfeja los disparos, nunca muestra los barcos colocados
        self.barcos = barcos # es un diccionario con los barcos

    # voy a colocar los barcos:
    ''' creo un método que haga que cada barco esté dentro del tablero,
    que no se solape con otros, y que tenga orientación horizontal o vertical '''
    def colocar_barcos(self):
        for nombre, info in self.barcos.items(): # recorro cada tipo de barco del diccionario en el que nombre es la clave e info el valor asociado
            tam = info["tamano"] # número de casillas que ocupa el barco
            cant = info["cantidad"] # cuántas unidades de ese barco hay
            letra = nombre[0] # símbolo del barco (primera letra del nombre) # cojo la primera letra del nombre del barco para usarlo como símbolo para representarlo en el tablero # Porque el tablero es una matriz 10×10 y cada casilla solo puede contener un carácter. Si intentara poner "Submarino" entero, rompería el formato del tablero.

            for _ in range(cant): # ahora coloco tantas unidades como sea la 'cantidad'
                colocado = False # 'colocado' empieza en False porque el barco todavía no está posicionado
                while not colocado: # mientras no encuentre una posición válida, se sigue probando
                    orient = random.choice(["H", "V"]) # elijo aleatoriamente la orientación horizontal o vertical
                    fila = random.randint(0, 9) # elijo una fila inicial aleatoria dentro del tablero
                    col = random.randint(0, 9) # elijo una columna inicial aleatoria dentro del tablero

                    if orient == "H": # primero compruebo que el barco cabe horizontalmente:
                        if col + tam <= 10 and np.all(self.tablero[fila, col:col+tam] == " "): # la col más el tam debe ser <= 10 para no salirnos del tablero # y, A LA VEZ,# compruebo que todas las casillas estén vacías 
                            self.tablero[fila, col:col+tam] = letra # coloco el barco: rellenamos ese tramo con la primera letra del nombre del barco ## 'fila' fija una fila concreta del tablero. 'col:col+tam' selecciona un rango de columnas consecutivas, desde 'col' hasta 'col+tam - 1'. El resultado es un trozo horizontal del tablero del tamaño exacto del barco.
                            # asigna la misma letra a todas las casillas comprendidas entre la columna col y la columna col + tam - 1 dentro de la fila indicada. Es decir, rellena de una sola vez el tramo horizontal donde debe colocarse el barco, marcando cada casilla con el símbolo elegido para representarlo.
                            colocado = True # ya está colocado, salgo del while
                    else: # si la orientación es vertical, compruebo que el barco cabe verticalmente:
                        if fila + tam <= 10 and np.all(self.tablero[fila:fila+tam, col] == " "): # 'fila + tam' debe ser <= 10 para no salirnos por abajo # Y, ADEMÁS # compruebo que las casillas están libres
                            self.tablero[fila:fila+tam, col] = letra # si están libres, colocamos el barco verticalmente con la primera letra del nombre del barco
                            colocado = True # ya está colocado, ya no necesitamos seguir buscando posición
    
    # voy a crear un método para mostrar los tableros:
    '''me sirve para ver el tablero con coordenadas y la cuadrícula
    para este juego necesito dos versiones: una para el tablero real y
    otra para mostrar el tablero de disparos (lo que ve el rival)'''
    def mostrar(self, modo="real"): # Muestra el tablero en consola, modo "real" muestra el tablero con barcos y modo "disparos" muestra el tablero con los disparos hechos
        if modo == "real": # elijo el tablero que quiero printear
            tablero_a_mostrar = self.tablero
        else:
            tablero_a_mostrar = self.tablero_disparos

        encabezado = "   |" + "|".join(f"{i:^3}" for i in range(1, 11)) + "|"
        print(encabezado)
        print("   +" + "---+" * 10) # pongo para que salga el tablero como una cuadrícula (este crea la cuadrícula superior)
        
        for i in range(10): # printeo cada fila con su número delante ## Recorre cada fila del tablero, y con el join construye una cadena con todas sus casillas separadas por espacios, y muéstrala junto al número de fila para que el tablero quede bien formateado ##
            letra_fila = chr(65 + i)  # convierto el índice de fila en letra
            fila_str = f" {letra_fila} |" # pongo una barra vertical para separar el nombre de las filas del resto
            for j in range(10): # j como índice de la columna
                celda = tablero_a_mostrar[i, j] # obtengo el contenido de la casilla en [fila i, columna j]
                contenido = celda if celda != " " else " "
                contenido = f" {contenido} "   # fuerza ancho fijo de 3 caracteres
                fila_str += contenido + "|"
            print(fila_str) # printeo la fila completa ya construida
            print("   +" + "---+" * 10) # printeo la línea inferior de la cuadrícula para esa fila


    def disparar(self, tablero_rival, jugador):
        ''' voy a crear un método disparar que gestionará
        cuando los jugadores hagan un disparo al tablero del rival'''
        while True: # mantengo un bucle para obligar a repetir si el disparo ya se hizo antes
            fila, columna = jugador.coordenadas(self.tablero_disparos) # la máquina necesita recibir el tablero de disparos para no repetir disparos
            if self.tablero_disparos[fila, columna] != " ": # compruebo si el jugador tiene un disparo registrado en tablero_disparos. Si ya estaba, obligo a elegir otra coordenada
                print("Ya disparaste ahí. Prueba con otra coordenada.")
                continue # vuelvo al inicio del bucle para elegir otra
            if tablero_rival.tablero[fila, columna] in ("X", "O"): # evitar disparar a casillas ya impactadas en el tablero real del rival
                print("Esa casilla ya fue disparada antes. Elige otra.")
                continue
            if tablero_rival.tablero[fila, columna] != " ": # si en el tablero del rival no hay un espacio en blanco, significa que había un barco, entonces es impacto
                print("¡Tocado!") # si no hay nada,
                if jugador.tipo == "maquina":
                    print(f"La máquina te dio en {chr(fila + 65)}{columna + 1}.")
                letra_original = tablero_rival.tablero[fila, columna] # guardo la letra original antes de sobreescribirla
                self.tablero_disparos[fila, columna] = "X" # marco la 'x' del impacto al barco en el tablero de disparos del jugador
                tablero_rival.tablero[fila, columna] = "X" # marco la 'x' en el tablero del rival
                jugador.ultima_fila = fila # guardo la última coordenada disparada por el jugador
                jugador.ultima_columna = columna 
                if self.barco_hundido(tablero_rival, letra_original): # uso el método creado para comprobar si ese disparo hundió el barco entero
                    print("¡Tocado y hundido!")
                    if jugador.tipo == "maquina":
                        print(f"La máquina te dio en {chr(fila + 65)}{columna + 1} y hundió uno de tus barcos.")
                    if jugador.tipo == "usuario":
                        print(f"Hundiste un barco enemigo en {chr(fila + 65)}{columna + 1}.")
                return True # devuelvo True para indicar el impacto (jugador repite turno)
            else: # si hay espacio es que es agua
                print("¡Agua!")
                if jugador.tipo == "maquina":
                    print("La máquina falló, te toca.")
                self.tablero_disparos[fila, columna] = "O" # marcamos 'o' en tablero_disparos del jugador
                jugador.ultima_fila = fila # guardo la última coordenada disparada
                jugador.ultima_columna = columna
                return False # devuelvo False para indicar que fue agua y se cambia el turno
   
    def barco_hundido(self, tablero_rival, letra_barco):
        '''este método comprueba si el disparo hundió un barco. usa la letra del barco en la casilla impactada
        y mira si quedan más casillas con esa misma letra en el tablero del rival.
        'tablero_rival' es el tablero REAL del oponente, donde están los barcos y los impactos
        'letra_barco' es la letra que identifica a un barco concreto (por ejemplo, "A", "B", "C"...).
        En este punto, ya hemos impactado una casilla de ese barco y queremos saber si quedan más partes de ese mismo barco sin hundir.
        '''
        if not np.any(tablero_rival.tablero == letra_barco): # busco en todo el tablero si queda algun casilla con esa letra, si no es así, el barco está hundido
        # np.any(tablero_rival.tablero == letra_barco) devuelve True si existe
        # al menos una casilla en el tablero que todavía tenga esa letra de barco.
        # Si NO existe ninguna (not np.any(...)), significa que todas las casillas
        # de ese barco han sido sustituidas por "X" en impactos anteriores.
        # Por tanto, el barco está completamente hundido.
            return True
    # Si aún queda alguna casilla con esa letra en el tablero,
    # significa que todavía hay partes del barco sin impactar.
    # En ese caso, el barco no está hundido.
        return False # si aún queda alguna casilla con esa letra, el barco no está hundido

    def todos_hundidos(self, tablero_rival):
        ''' recorre el tablero del rival, si encuentra cualquier letra, significa que aún queda barco,
        peros i no encuentra ninguna letra es que están todos hundidos '''
        for fila in tablero_rival.tablero: # recorro cada fila
            for casilla in fila: # recorro cada casilla de esa fila
                if casilla.isalpha():  # solo las letras representan que hay barcos en pie
                    return False # aún queda barco
        return True # si no encuentro ninguna letra, todos están hundidos
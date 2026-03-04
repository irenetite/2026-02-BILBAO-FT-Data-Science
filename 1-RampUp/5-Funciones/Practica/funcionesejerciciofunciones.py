def num_a_dia(num):
    dias = {1: "Lunes",
            2: "Martes",
            3: "Miércoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sábado",
            7: "Domingo"}
    return dias.get(num, "Número fuera de rango")


def piramide_invertida(n):
    for inicio in range(n, 0, -1):
        for i in range(inicio, 0, -1):
            print(i, end=" ")
        print()
        
        
        
def piramide2(filas):
    for i in range(filas,0,-1):
        for j in list(range(i,0,-1)):
            print(j, end=" ")
        print()
        
        
        
def comparacion(n1, n2):
    if n1 == n2:
        return "Son iguales"
    if n1 > n2:
        return f"{n1} es mayor que {n2}"
    if n1 < n2:
        return f"{n1} es menor que {n2}"
    
    
def comparar (a,b):
    match (a,b):
        case (a,b) if a==b:
            print(f"{a} = {b}")
        case (a,b) if a>b:
            print(f"{a} mayor que {b}")
        case (a,b) if a<b:
            print(f"{a} menor que {b}")
            
            
def contar_letra(texto, letra):
    texto = texto.lower()
    letra = letra.lower()
    contador = 0
    for caracter in texto:
        if caracter == letra:
            contador += 1
    return contador



def contador(texto, letra):
    contador=texto.lower().count(letra.lower())
    return contador


def contador_letras(palabra):
    return {letra: palabra.count(letra) for letra in set(palabra)}


def gendict(string):
    d = {}
    for letra in string:
        if letra in d.keys():
            d[letra] = d[letra]+1 # cada vez q pases por la letra suma 1 a la cantidad de veces q pasas
        else:
            d[letra] = 0
            d[letra] += 1
    return d


def anad_elim_lista(lista, comando, elemento=None):
    if comando == "add":
        if elemento is not None:
            lista.append(elemento)
        return lista
    elif comando == "remove":
        if elemento in lista:
            lista.remove(elemento)
        return lista
    else:
        return "Ese comando no es válido"
    
    
def modif_lista(lista, comando, elemento=None):
    match comando:
        case "add":
            lista.append(elemento)
        case "remove":
            try:
                lista.remove(elemento)
            except:
                pass
    print(modif_lista)
    
    
    
def crear_frase(*palabras):
    return " ".join(palabras)


def fibonacci(lenght, n1=0, n2=1):
    if lenght == 0:
        return n1
    if lenght == 1:
        return n2
    return fibonacci(lenght-1, n2, n1+n2)


def fibonacci_con_for(lenght, n1=0, n2=1):
    f = 0
    for i in renge(lenght-1):
        f=n1+n2
        n1=n2
        n2=f
    return f



# JUEGO DEL AHORCADO
# el archivo debería llamarse "main", para otra vez tenerlo en cuenta

import random
import Palabras
import mod_ahorcado


def main():
    palabra_azar = random.choice(Palabras.palabras)
    
    mod_ahorcado.ahorcado(palabra_azar)

if __name__ == "__main__":
    main()
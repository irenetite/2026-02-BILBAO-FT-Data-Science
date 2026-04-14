# main.py
'''
script para organizar archivos de la carpeta Descargas por tipo

uso: python main.py [ruta_carpeta]

si no se proporciona ruta, usa la carpeta Descargas por defecto


ventajas:
flexible: puedes especificar cualquier carpeta desde la línea de comandos
reutilizable: se puede usar en cualquier sistema cambiando la ruta
'''

import sys
import os

from variables import DEFAULT_DOWNLOADS_FOLDER
from funciones import organize_files


def main():
    # Obtener carpeta desde argumentos o usar la por defecto
    if len(sys.argv) > 1:
        folder_to_organize = sys.argv[1]
    else:
        folder_to_organize = DEFAULT_DOWNLOADS_FOLDER
    
    if not os.path.exists(folder_to_organize):
        print(f'Error: La carpeta "{folder_to_organize}" no existe.')
        return
    
    print(f'Organizando archivos en: {folder_to_organize}')
    print('-' * 50)
    
    files_moved = organize_files(folder_to_organize)
    
    print('-' * 50)
    print(f'¡Organización completada! Se movieron {files_moved} archivos.')


if __name__ == '__main__':
    main()
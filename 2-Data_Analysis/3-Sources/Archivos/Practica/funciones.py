# funciones.py
import os
import shutil

from variables import (
    doc_types,
    img_types,
    software_types,
    FOLDER_IMAGENES,
    FOLDER_DOCUMENTOS,
    FOLDER_SOFTWARE,
    FOLDER_OTROS
)


def get_folder_category(extension):
    ext_lower = extension.lower()
    if ext_lower in img_types:
        return FOLDER_IMAGENES
    elif ext_lower in doc_types:
        return FOLDER_DOCUMENTOS
    elif ext_lower in software_types:
        return FOLDER_SOFTWARE
    else:
        return FOLDER_OTROS


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def organize_files(source_folder):
    files_moved = 0
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            category = get_folder_category(ext)
            dest_folder = os.path.join(source_folder, category)
            
            create_folder_if_not_exists(dest_folder)
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f'Movido: {filename} -> {category}')
            files_moved += 1

    return files_moved


'''
importa las variables desde variables.py
usa las constantes FOLDER_IMAGENES, etc., en lugar de strings hardcoded
es más profesional y escalable
'''
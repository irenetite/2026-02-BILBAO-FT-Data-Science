# variables.py
# tipos de archivos por categoría (los del pricipio, pero vuelvo a ponerlos):
doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx') # documentos
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif') # imágenes
software_types = ('.exe', '.py', '.ipynb') # software

# carpetas de destino, la IA me dijo que las constantes hay que ponerlas en mayúsculas,
# que es una convención, pero no sé si en la teoría David lo dijo
FOLDER_IMAGENES = 'Imagenes'
FOLDER_DOCUMENTOS = 'Documentos'
FOLDER_SOFTWARE = 'Software'
FOLDER_OTROS = 'Otros'

# carpeta por defecto (Descargas), lo mismo de arriba respecto a las mayúsculas
DEFAULT_DOWNLOADS_FOLDER = r'C:\Users\titea\Downloads'


'''
por qué separar las variables?
reutilización: otros scripts pueden importar estas constantes
mantenimiento: oambias las extensiones en un solo lugar
legibilidad: el código es más claro
convención: las constantes en MAYÚSCULAS indican que no deben modificarse
'''
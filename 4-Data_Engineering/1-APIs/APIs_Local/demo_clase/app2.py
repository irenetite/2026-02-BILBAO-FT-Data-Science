from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/books/all', methods=['GET'])
def get_all():
    connection = sqlite3.connect('books.db') # se conecta a la base de datos, ruta en la que esté la base de datos
    cursor = connection.cursor()
    select_books = "SELECT * FROM books" # NOS CONECTAMOS COMO EN SQL
    result = cursor.execute(select_books).fetchall()
    connection.close() # CIERRO CONEXION
    return {'books': result} # DEVUELVO RESULT

@app.route('/api/v1/resources/book/<string:author>', methods=['GET']) # AHOR PUEDO PASAR NOMBRE AUTOR
def get_by_author(author):
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    select_books = "SELECT * FROM books WHERE author=?" # AHORA PONE LO DE WHERE AUTHOR
    result = cursor.execute(select_books, (author,)).fetchall()
    connection.close()
    return {'books': result}

@app.route('/api/v1/resources/book/filter', methods=['GET'])
def filter_table():
    query_parameters = request.get_json() # PARAMETROS DE BUSQUEDA POR ID, PUBLISHED, AUTHR
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    query = "SELECT * FROM books WHERE"  # PETICIONES DE SQL:
    to_filter = []
    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
        if not (id or published or author):
            return "page not found 404"
    query = query[:-4] + ';' # QUITAR LOS 4 ULTIMOS (EL AND Y EL ESPACIO DE ANTES). ASÍ CONCATENO EL CIERRE DE CONSULTA CON ;
    result = cursor.execute(query, to_filter).fetchall()
    connection.close()
    return {'books': result}

app.run()

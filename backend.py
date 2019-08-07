import sqlite3
# Crea una base de datos local con sqlite3
# //Coneccion con base de datos


def connect():
    conn = sqlite3.connect("cards.db")
    # cursor objeto para ejecutar comandos con la base de datos
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY, title TEXT)")
    # base de datos Commit cambios
    conn.commit()
    conn.close()


def insert(item):
    conn = sqlite3.connect("cards.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (NULL,?)", (item,))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("cards.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("cards.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE id=?", (id,))
    conn.commit()
    conn.close()

# CREAR NUEVA TABLA


def create_table():
    conn = sqlite3.connect("cards.db")
    # cursor objeto para ejecutar comandos con la base de datos
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS categorias(id INTEGER , title TEXT,categoriaId INTEGER)")
    # base de datos Commit cambios
    conn.commit()
    conn.close()


def insert_row(item, categoria_id):
    conn = sqlite3.connect("cards.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO categorias VALUES (NULL,?,?)",
                (item, categoria_id))
    conn.commit()
    conn.close()


def search_row(categoria_id):
    conn = sqlite3.connect("cards.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM categorias WHERE categoriaId=?",
                (categoria_id,))
    rows = cur.fetchall()
    print(categoria_id)
    conn.close()
    return rows


def delete_row(id):
    conn = sqlite3.connect("cards.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM categorias WHERE id=?", (id,))
    conn.commit()
    conn.close()


connect()
create_table()
print(search_row(1))

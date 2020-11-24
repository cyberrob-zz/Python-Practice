import sqlite3

def connect():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn text)')
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_all():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM book')
    rows = cursor.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows

connect()
# insert(title='Old man and the sea', author='Ernest Hemingway', year=1954, isbn='1781396809')
# print(search(author='Ernest Hemingway'))
delete(7)
print(view_all())

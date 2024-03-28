import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Successfully connected to SQLite database: {db_file}')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS authors
                     (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS publishers
                     (id INTEGER PRIMARY KEY, name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                     (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER, publisher_id INTEGER,
                     FOREIGN KEY(author_id) REFERENCES authors(id),
                     FOREIGN KEY(publisher_id) REFERENCES publishers(id))''')
    conn.commit()

if __name__ == '__main__':
    db_file = 'database.db'
    conn = create_connection(db_file)
    if conn is not None:
        create_tables(conn)
        close_connection(conn)

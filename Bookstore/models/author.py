import sqlite3

class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def create(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO authors (name, age) VALUES (?, ?)", (self.name, self.age))
            conn.commit()
            return "Author created successfully."
        except sqlite3.Error as e:
            return f"Failed to create author: {e}"

    @staticmethod
    def get_all(conn):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM authors")
            return cursor.fetchall(), "Authors listed successfully."
        except sqlite3.Error as e:
            return None, f"Failed to retrieve authors: {e}"

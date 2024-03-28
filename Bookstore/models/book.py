class Book:
    def __init__(self, title, author_id, publisher_id):
        self.title = title
        self.author_id = author_id
        self.publisher_id = publisher_id

    def create(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO books (title, author_id, publisher_id) VALUES (?, ?, ?)",
                           (self.title, self.author_id, self.publisher_id))
            conn.commit()
            return "Book has been successfully created."
        except Exception as e:
            return f"Failed to create book: {e}"

    @staticmethod
    def get_all(conn):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            return [Book(*row) for row in cursor.fetchall()], "Books listed successfully."
        except Exception as e:
            return None, f"Failed to retrieve books: {e}"

    def update(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE books SET title = ?, author_id = ?, publisher_id = ? WHERE id = ?",
                           (self.title, self.author_id, self.publisher_id, self.id))
            conn.commit()
            return "Book has been successfully updated."
        except Exception as e:
            return f"Failed to update book: {e}"

    @staticmethod
    def delete(conn, book_id):
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
            conn.commit()
            return "Book has been successfully deleted."
        except Exception as e:
            return f"Failed to delete book: {e}"

class Publisher:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def create(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (self.name,))
            conn.commit()
            return "Publisher has been successfully created."
        except Exception as e:
            return f"Failed to create publisher: {e}"

    @staticmethod
    def get_all(conn):
        cursor = conn.cursor()
        try:
              cursor.execute("SELECT * FROM publishers")
              return [Publisher(row[1], row[0]) for row in cursor.fetchall()], "Publishers listed successfully."
        except Exception as e:
              return None, f"Failed to retrieve publishers: {e}"


    def update(self, conn):
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE publishers SET name = ? WHERE id = ?", (self.name, self.id))
            conn.commit()
            return "Publisher has been successfully updated."
        except Exception as e:
            return f"Failed to update publisher: {e}"

    @staticmethod
    def delete(conn, publisher_id):
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM publishers WHERE id = ?", (publisher_id,))
            conn.commit()
            return "Publisher has been successfully deleted."
        except Exception as e:
            return f"Failed to delete publisher: {e}"

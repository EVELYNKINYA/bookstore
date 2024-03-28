from database import create_connection, close_connection, create_tables
from models.author import Author
from models.publisher import Publisher
from models.book import Book

def test_create_author():
    conn = create_connection(':memory:')
    if conn is not None:
        create_tables(conn)
        author = Author('John Doe', 30)
        result = author.create(conn)
        assert result == "Author created successfully."
        close_connection(conn)

def test_get_all_authors():
    conn = create_connection(':memory:')
    if conn is not None:
        create_tables(conn)
        author1 = Author('John Doe', 30)
        author2 = Author('Jane Smith', 25)
        author1.create(conn)
        author2.create(conn)
        authors, message = Author.get_all(conn)
        assert len(authors) == 2
        assert authors[0].name == 'John Doe'
        assert authors[1].name == 'Jane Smith'
        close_connection(conn)

# Similar tests can be written for other classes and methods (Publisher, Book, etc.)

if __name__ == '__main__':
    test_create_author()
    test_get_all_authors()
    print("All tests passed successfully.")

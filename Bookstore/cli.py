import sqlite3
from database import create_connection, close_connection, create_tables
from models.author import Author
from models.publisher import Publisher
from models.book import Book

def create_author(conn):
    name = input("Enter author name: ")
    age = int(input("Enter author age: "))
    author = Author(name, age)
    message = author.create(conn)
    print(message)

def create_publisher(conn):
    name = input("Enter publisher name: ")
    publisher = Publisher(name)
    message = publisher.create(conn)
    print(message)

def create_book(conn):
    title = input("Enter book title: ")
    author_id = int(input("Enter author id: "))
    publisher_id = int(input("Enter publisher id: "))
    book = Book(title, author_id, publisher_id)
    message = book.create(conn)
    print(message)

def list_authors(conn):
    authors, message = Author.get_all(conn)
    if authors:
        for author in authors:
            print(f"{author[0]}. {author[1]}, {author[2]}")  # Assuming id is at index 0, name at index 1, and age at index 2
    else:
        print(message)


def list_publishers(conn):
    publishers, message = Publisher.get_all(conn)
    if publishers:
        for publisher in publishers:
            print(f"{publisher.id}. {publisher.name}")
    else:
        print(message)

def list_books(conn):
    books, message = Book.get_all(conn)
    if books:
        for book in books:
            author = Author.get(conn, book.author_id)
            publisher = Publisher.get(conn, book.publisher_id)
            print(f"{book.id}. {book.title}, {author.name}, {publisher.name}")
    else:
        print(message)

def update_book(conn):
    book_id = int(input("Enter the book id to update: "))
    title = input("Enter new book title: ")
    author_id = int(input("Enter new author id: "))
    publisher_id = int(input("Enter new publisher id: "))
    book = Book(title, author_id, publisher_id)
    book.id = book_id
    message = book.update(conn)
    print(message)

def delete_book(conn):
    book_id = int(input("Enter the book id to delete: "))
    message = Book.delete(conn, book_id)
    print(message)

def main():
    db_file = 'database.db'
    conn = create_connection(db_file)
    if conn is not None:
        create_tables(conn)  # Creating tables
        while True:
            print("\n1. Create author")
            print("2. Create publisher")
            print("3. Create book")
            print("4. List authors")
            print("5. List publishers")
            print("6. List books")
            print("7. Update book")
            print("8. Delete book")
            print("9. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                create_author(conn)
            elif choice == '2':
                create_publisher(conn)
            elif choice == '3':
                create_book(conn)
            elif choice == '4':
                list_authors(conn)
            elif choice == '5':
                list_publishers(conn)
            elif choice == '6':
                list_books(conn)
            elif choice == '7':
                update_book(conn)
            elif choice == '8':
                delete_book(conn)
            elif choice == '9':
                close_connection(conn)
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

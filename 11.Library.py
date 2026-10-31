
import os

FILE_NAME = "library.txt"


def add_book():
    """Add a new book to the catalogue."""
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    transaction_id = input("Enter transaction ID: ").strip()

    if not title or not author or not transaction_id:
        print("All fields are required.")
        return

    # Append book details to the text file
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(f"{title}|{author}|{transaction_id}\n")

    print("Book added successfully!")


def read_books():
    """Read all books from the text file."""
    books = []

    if not os.path.exists(FILE_NAME):
        return books

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("|")

            if len(parts) == 3:
                books.append({
                    "title": parts[0],
                    "author": parts[1],
                    "transaction_id": parts[2]
                })

    return books


def display_books(books):
    """Display a list of books."""
    if not books:
        print("No books found.")
        return

    print("\n--- Library Catalogue ---")

    for number, book in enumerate(books, start=1):
        print(f"{number}. Title: {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Transaction ID: {book['transaction_id']}")


def search_book():
    """Search books by title or author."""
    books = read_books()

    if not books:
        print("The catalogue is empty.")
        return

    print("1. Search by title")
    print("2. Search by author")

    choice = input("Choose search option: ").strip()

    if choice == "1":
        keyword = input("Enter title: ").strip().lower()
        results = [
            book for book in books
            if keyword in book["title"].lower()
        ]

    elif choice == "2":
        keyword = input("Enter author: ").strip().lower()
        results = [
            book for book in books
            if keyword in book["author"].lower()
        ]

    else:
        print("Invalid search option.")
        return

    display_books(results)


def generate_report():
    """Generate catalogue reports."""
    books = read_books()

    print("\n--- Library Reports ---")
    print("Total number of books:", len(books))

    author = input(
        "Enter an author name for the report: "
    ).strip().lower()

    if author:
        author_books = [
            book for book in books
            if book["author"].lower() == author
        ]

        print(
            f"Books by {author.title()}: "
            f"{len(author_books)}"
        )

        display_books(author_books)


def main():
    """Display the main menu."""
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Search for a book")
        print("4. Generate reports")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            display_books(read_books())

        elif choice == "3":
            search_book()

        elif choice == "4":
            generate_report()

        elif choice == "5":
            print("Thank you for using the library system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

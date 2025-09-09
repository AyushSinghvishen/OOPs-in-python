class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                book.is_available = False
                print(f"You borrowed '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_available:
                book.is_available = True
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not borrowed from this library.")


# Example usage
if __name__ == "__main__":
    library = Library()

    # Add books
    book1 = Book("The Alchemist", "Paulo Coelho")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)

    # Show books
    library.show_books()

    # Borrow and return
    library.borrow_book("1984")
    library.show_books()
    library.return_book("1984")
    library.show_books()

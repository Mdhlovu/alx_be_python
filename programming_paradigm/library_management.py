class Book:

    def __init__(self, title, author):
        self.title = title            # Public attribute for the title of the book
        self.author = author          # Public attribute for the author of the book
        self._is_checked_out = False   # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book is already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book was not checked out

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:

    def __init__(self):
        self._books = []  # Private list to store instances of Book

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book titled '{title}' not found.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book titled '{title}' not found.")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")



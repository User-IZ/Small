from interface import LibraryInterface

class LibraryServer(LibraryInterface):
    def __init__(self):
        self.books = {
            "DSA": None,
            "OS": None,
            "CN": None
        }

    def search_book(self, title):
        if title in self.books:
            return "Available" if self.books[title] is None else f"Issued to {self.books[title]}"
        return "Book not found"

    def issue_book(self, title, user):
        if title not in self.books:
            return "Book not found"

        if self.books[title] is None:
            self.books[title] = user
            return f"{title} issued to {user}"
        return f"{title} already issued"

    def return_book(self, title, user):
        if title in self.books and self.books[title] == user:
            self.books[title] = None
            return f"{title} returned by {user}"
        return "Return failed"

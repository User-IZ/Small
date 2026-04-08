class LibraryInterface:
    def search_book(self, title):
        raise NotImplementedError

    def issue_book(self, title, user):
        raise NotImplementedError

    def return_book(self, title, user):
        raise NotImplementedError

class LibraryClient:
    def __init__(self, server):
        self.server = server  # acts like remote reference

    def search(self, title):
        return self.server.search_book(title)

    def issue(self, title, user):
        return self.server.issue_book(title, user)

    def return_book(self, title, user):
        return self.server.return_book(title, user)

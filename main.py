from server import LibraryServer
from client import LibraryClient

# create server
server = LibraryServer()

# create clients
client1 = LibraryClient(server)
client2 = LibraryClient(server)

# simulate distributed calls
print(client1.search("DSA"))
print(client1.issue("DSA", "Alice"))

print(client2.search("DSA"))
print(client2.issue("DSA", "Bob"))

print(client1.return_book("DSA", "Alice"))
print(client2.issue("DSA", "Bob"))

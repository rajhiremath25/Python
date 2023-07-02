import socket

server = socket.socket()
print("socket created")

server.bind(("localhost", 9999))
server.listen(5)
print("waiting for connections")

while True:
    client, address = server.accept()
    print("connected with ", address)

    serverName = client.recv(1024).decode()
    print(serverName)

    client.send(bytes("message from server", "utf-8"))
    client.close()


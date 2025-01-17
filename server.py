import socket
import os

import faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "./socket_file"
faker = faker.Faker()

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f"Starting up on {server_address}")

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)
        while True:
            data = faker.name()
            data_str = data
            print("Received " + data_str)
            if data:
                connection.sendall(data.encode())
            else:
                print("no data from", client_address)
                break

    finally:
        print("Closing current connection")
        connection.close()

# import os
# import socket

# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(("localhost",9999))

# file = open("sent.txt","rb")
# file_size = os.path.getsize("sent.txt")

# client.send("recieved.txt".encode())
# client.send(str(file_size).encode())

# data = file.read()
# client.sendall(data)
# client.send(b"<END>")

# print("File sent successfully")
# client.close()
# file.close()

import socket
import os

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))

file = open("sent.txt","rb")
file_size = os.path.getsize("sent.txt")

client.send("recieved.txt".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

print("File sent successfully")
client.close()
file.close()

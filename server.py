# import socket

# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(("localhost",9999))

# server.listen()

# client,addr = server.accept()

# file_size = client.recv(1024).decode()

# file = open("recieved.txt","wb")
# file_bytes = b""

# done = False
# while not done:
#     data = client.recv(1024)
#     if file_bytes[-5:] == b"<END>":
#         done = True
#     else:
#         file_bytes = file_bytes + data

# file_bytes = file_bytes[:-5]
# file_bytes = file_bytes[2:]
# file.write(file_bytes)
# print("File recieved successfully")
# server.close()
# file.close()
# client.close()


import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))

server.listen()
print("Server is listeneing")

client,addr = server.accept()
file_size = client.recv(1024).decode()

file = open("recieved.txt","wb")
file_bytes = b""

done = False
while not done:
    data = client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes+=data
file_bytes = file_bytes[0:-5]
file_bytes = file_bytes[2:]
file.write(file_bytes)
print("File recieved Success")
file.close()
client.close()
server.close()
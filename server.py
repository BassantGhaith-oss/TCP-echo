import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("192.168.1.4",5000))

server.listen(1)

print("Waiting for client.....")

conn,addr = server.accept()

print("Client connected: ",addr)

data = conn.recv(1024)

print("Server received: ",data.decode())

conn.sendall(b"Hello from server...")

conn.close()
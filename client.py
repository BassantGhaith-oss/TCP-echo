import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("0.0.0.0",5000))

client.sendall(b"Hello from client...")

data = client.recv(1024)

print("Client received: ",data.decode())

client.close()

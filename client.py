import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("192.168.1.4",5000))

client.sendall(b"Hello from client...")

data = client.recv(1024)

print("Client received: ",data.decode())

client.close()

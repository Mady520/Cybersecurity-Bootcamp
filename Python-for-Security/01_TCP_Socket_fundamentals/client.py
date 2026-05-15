import socket as s
client_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
message= input("Enter the message: ")
client_socket.send(message.encode())
response = client_socket.recv(1024)
print(f"Recieved from server: {response.decode()}")
client_socket.close()
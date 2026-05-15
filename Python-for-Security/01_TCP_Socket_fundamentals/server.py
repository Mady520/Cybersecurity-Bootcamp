import socket as s
server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is running on the port 12345")

while True:
    conn,addr = server_socket.accept()
    print(f"Connected by address {addr}")
    data = conn.recv(1024)
    if not data:
        break
    print(f"Recieved from client:{data.decode()}")
    response = "message recieved"
    conn.send(response.encode())
    conn.close()





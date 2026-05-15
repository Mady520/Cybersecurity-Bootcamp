import socket
def banner_grab(ip, port):
    try:
        s = socket.socket()
       # s.settimeout(1)
        s.connect((ip, port))
        s.send(b'\n')
        banner = s.recv(1024)
        print (f"Banner : {banner.decode().strip()}")
    except Exception as e:
        print(f"Error : {e}")
    finally:
        s.close()

ip = input("Enter the Target IP: ")       
port = int(input("Enter the port: "))
banner_grab(ip, port)         
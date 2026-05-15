import socket
def port_scan(target_ip, ports):
    print(f"Scanning {target_ip} for open ports")
    for port in ports:
        s= socket.socket()
        s.settimeout(1)
        try:
            s.connect((target_ip,port))
            print(f"port {port} is open")
        except(socket.timeout,socket.error):
            pass
        finally:
            s.close()

target = input("Enter the target IP")
ports = range(1,100)
port_scan(target,ports)                
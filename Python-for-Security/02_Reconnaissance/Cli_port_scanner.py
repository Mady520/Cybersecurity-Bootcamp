import sys
import socket
from datetime import datetime

#define our target 
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid arguments!")
    print("Syntax: python3 scanner.py <IP>")

print("_"* 50)
print("Scanning target" + str(target))
print("Time started at " + str(datetime.now()))
print("_"* 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result =s.connect_ex((target ,port))
        if result == 0:
            print(f"The port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\n Exiting program!")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Could not connect to server!")
    sys.exit()        
    


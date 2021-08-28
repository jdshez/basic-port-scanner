import sys
import socket
from datetime import datetime

if len(sys.argv) == 2;
    target = socket.gethostbyname(sys.argv[1])
else: 
    print("Invalid no. of arguments, please try again...")

print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
                print("Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()




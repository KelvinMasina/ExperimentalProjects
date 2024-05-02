import socket
import sys
import time

# Connect the socket to the port where the server is listening
server_address = ('192.168.4.1', 80)

data = ''

while (data != "OK"):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(server_address)

    sock.sendall(b"OPEN")

    print("receive starting")
    sock.settimeout(10)

    try:
        data = sock.recv(2).decode('utf-8')
        print("received ")
        print(data)     
    except socket.timeout: # fail after 1 second of no activity
        print("Didn't receive data! [Timeout]")
    finally:
        time.sleep(5)
        sock.close()

print('done')
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("192.168.10.102", 2390))
count = 0
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    count = count +1
    print("received message: %s" % data)
    print(count)
import socket
import time
from datetime import datetime

HOST = "127.0.0.1"
PORT = 7789

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

counter = 5

while True:
    now = datetime.utcnow()
    s.send(b"hello")
    counter -= 1
    print(f"Send 'Hello' at {now}")
    data = s.recv(1024)
    print(f"Receive data: {data}")
    time.sleep(1)

# s.close()
# s.send(b"hello")

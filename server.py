import socket
import time
from datetime import datetime
import threading


bind_ip = "0.0.0.0"
bind_port = 7789

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print(f"Listening on: {bind_ip}:{bind_port}")

LAST_CONNECTION = None


def check_is_connected():
    while True:
        if LAST_CONNECTION is not None:
            now = datetime.utcnow()
            if (now - LAST_CONNECTION).seconds > 10:
                print("*" * 50)
                print("Connection lost")
                print("*" * 50)

        # print("Checking")
        time.sleep(1)


def main():
    global LAST_CONNECTION

    t = threading.Thread(target=check_is_connected)  #
    t.setDaemon(True)
    t.start()

    while True:
        client, addr = server.accept()
        print(f"Client: {client} - Address: {addr}")
        while True:
            try:
                data = client.recv(1024)
                print(data)
                client.send(b"ACK!")
                now = datetime.utcnow()
                LAST_CONNECTION = now
                print(f"Now: {now}")
            except BrokenPipeError:
                print(f"Client is close: {client}")
                client.close()
                break


main()

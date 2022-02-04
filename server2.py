import socket
import random

conn = socket.socket()
conn.bind(('127.0.0.2', 8080) )
conn.listen(1)

while True:
    try:
        client, addr = conn.accept()
    except socket.error:
        pass
    else:
        client.send(str(random.randint(1,1000)).encode("utf-8"))
        try:
            data = client.recv(1024)
            print(data)
        except:
            pass
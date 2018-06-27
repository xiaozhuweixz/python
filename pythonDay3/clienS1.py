import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8001))
#conn_str = str(sk.recv(1024), encoding='utf-8')
#print(conn_str)
sk.sendall(bytes('方法是的发送到', encoding='utf-8'))



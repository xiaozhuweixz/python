import socket


sk = socket.socket()
sk.bind(('127.0.0.1',8001))
sk.listen()

while True:
    conn, adder = sk.accept()
    while True:
        conn_str = sk.recv(1024)
        conn_date = str(conn_str, encoding='utf-8')
        print(conn_date)
        #conn.sendall(bytes(conn_date+'hello', encoding='utf-8'))
    conn.close()

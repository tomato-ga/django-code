import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('db', 3306))
    print('Connected to db on port 3306')
except Exception as e:
    print('Cannot connect to db: ', e)
s.close()


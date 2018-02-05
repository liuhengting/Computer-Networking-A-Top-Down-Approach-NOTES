import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 80))
# 接收欢迎消息:
# print(s.recv(1024).decode('utf-8'))
sendHeader = 'GET ' \
             '/HelloWorld.html ' \
             'HTTP/1.1\n' \
             'Host: 127.0.0.1\n' \
             'Connection: Kepp-alive\n'
s.send(sendHeader.encode())
message = s.recv(8192)

while message != b'':
    message = s.recv(8192)
    print(message)

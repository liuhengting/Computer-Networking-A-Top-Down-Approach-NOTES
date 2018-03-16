#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('127.0.0.1', 80))
serverSocket.listen(5)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        header = "HTTP/1.1 200 OK\n" \
                 "Connection: close\n" \
                 "Content-Type: text/html\n" \
                 "Content-Length: %d\n\n" % (len(outputdata))
        connectionSocket.send(header.encode())
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            print(outputdata[i])
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        header = ' HTTP/1.1 404 Found'
        connectionSocket.send(header.encode())
        #Fill in end

        #Close client socket
        connectionSocket.close()
        #Fill in start
        #Fill in end
serverSocket.close()
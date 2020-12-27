import socket
import sys
import time

server = socket.socket()
host = input(str("Please enter the host name: "))
port = 4321
server.connect((host,port))
print("Connected to server")
print("Let him send the message first please don't do anything...")
while True:
    incoming_message = server.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server =>> ", incoming_message)
    print("He/She is waiting for your message...")
    message = input("You =>> ")
    message = message.encode()
    server.send(message)
    print("Wait for his/her message...")

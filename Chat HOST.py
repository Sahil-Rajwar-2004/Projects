import socket
import sys
import time

server = socket.socket()
host = socket.gethostname()
print("Server will start on host:",host)
port = 4321
server.bind((host,port))
print("Server is bound successfully")
server.listen(1) #only 1 client can join at one time
conn, addr = server.accept()
print(addr,"has connected")
print("He/She is waiting for your message...")
while True:
    message = input("You =>> ")
    message = message.encode()
    conn.send(message)
    print("Wait for his/her message...")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client =>>", incoming_message)

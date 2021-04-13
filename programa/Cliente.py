import socket
HEADER = 64
PORT = 5050
FORMAT = 'uft-8'
DISCONNECT_MESSAGE= "!DISCONNECT"
SERVER = "192.168.1.41"
ADDR= (SERVER,PORT)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length= len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cliente.send(send_length)
    cliente.send(message)
    print(cliente.recv(2048).decode(FORMAT))
send("Distribuidas")
input()
send("¿Como estas?") 
input()
send(" very good")   

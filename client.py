import socket
host=socket.gethostname()
port=1255
sc=socket.socket()
sc.connect((host,port))
con=True
while con:
    msg=input("Enter the message to the server: ")
    sc.send(msg.encode("utf-8"))
    data=sc.recv(1024)
    data=data.decode("utf-8")
    print("Message from server side:")
    print(data)
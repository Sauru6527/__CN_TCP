import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1255
s.bind((host,port))
s.listen(2)
sk,address=s.accept()
print("Got connection from",address)
con=True
while con:
    msg=sk.recv(1024)
    msg=msg.decode("utf-8")
    print("Message from client side:",msg)
    data=input("Enter message:")
    data=data.encode("utf-8")
    sk.send(data)












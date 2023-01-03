import socket
host=socket.gethostname()
port=1256
s=socket.socket()
s.bind((host,port))
s.listen(2)
sk,address=s.accept()
print("Waiting to connect")
print("Connected Client Adress is:",address)
data=sk.recv(1024)
data=data.decode("utf-8")
file=open("Dhanu2.txt","w")
file.write(data)
file.close()

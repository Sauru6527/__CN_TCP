import socket
host=socket.gethostname()
port=1256
s=socket.socket()
s.connect((host,port))
file=open("Dhanu.txt","r")
data=file.read()
data=data.encode("utf-8")
s.send(data)
print("File Send Successfully.....")


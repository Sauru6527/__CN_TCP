
import socket
host=socket.gethostname()
PORT = 8080
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")
sk, Address = server.accept()
print("Connected client :", Address)
msg = ''
while True:
	data = sk.recv(1024)
	msg = data.decode()
	print("Equation is recievied")
	print(msg)
	result = eval(msg)
	print(result)
	output = str(result)
	sk.send(output.encode())

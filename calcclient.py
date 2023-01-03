# Import socket module
import socket
host=socket.gethostname()
PORT = 8080
s=socket.socket()
s.connect((host, PORT))
while True:
	print("Example : 4 + 5")
	inp = input("Enter the operation in \the form opreand operator oprenad: ")
	s.send(inp.encode())
	answer = s.recv(1024)
	print("Answer is "+answer.decode())


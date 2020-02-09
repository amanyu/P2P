import socket               
 
s = socket.socket()         

port = 12347              
 
s.connect(('172.24.193.20', port))
 

print s.recv(1024)
while True:
#	port = port + 1
#	#s.bind(('', port))
#	s.listen(5)
#	c, addr = s.accept()
	x = raw_input()
	s.send(x)
	reply = s.recv(1024)
	print reply
	if reply == "END CHAT":
		s.close()
	

s.close() 

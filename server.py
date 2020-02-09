import socket               
 

s = socket.socket()         
print "Socket successfully created"
 

port = 12345               

s.bind(('', port))        
print "socket binded to %s" %(port)
 

s.listen(99)     
print "socket is listening"           


while True:
 
   c, addr = s.accept()     
   print 'Got connection from', addr
 
   while True:
	x = raw_input()
   	c.send(x)
   	reply = c.recv(1024)
	print reply
	if reply == "END CHAT":
		c.close()


	

   c.close()

import socket # Import socket module

# Server
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port

s.listen(5) # Now wait for client connection.
while True:
    c, addr = s.accept() # Establish connection with client.
    print ('Got connection from', addr)
    c.send(b'Thank you for connecting') # Data to be sent should be bytes
    c.close() # Close the connection

# Client
s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345 # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024).decode()) # Decode bytes to string
s.close() # Close the socket when done

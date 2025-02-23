# import socket module
import socket
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)

  #Prepare a server socket
  serverSocket.bind(("", port))

  # The server listens on the specified port
  serverSocket.listen()

  while True:
    #Establish the connection
    #print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
      # Client sends a message containing the file
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      #opens the client requested file.
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')
      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?
      #Content-Type is an example on how to send a header as bytes. There are more!
      header = b"HTTP/1.1 200 OK\r\n"
      header += b"Content-Type: text/html; charset=UTF-8\r\n"
      header += b"Server: CarterPortnoyPythonServer/2.1.2024\r\n"
      header += b"Connection: close\r\n\r\n"

      #connectionSocket.sendall(header)

      for i in f: #for line in file
      #Send the content of the requested file to the client (don't forget the headers you created)!
        header += i#.encode()
      connectionSocket.sendall(header)
      connectionSocket.close() #closing the connection socket
      f.close()

    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      notfound = b"HTTP/1.1 404 Not Found\r\n"
      notfound += b"Content-Type: text/html; charset=UTF-8\r\n\r\n<html><h2>404 Not Found</h2></html>"
      #notfound += b"Connection: keep-alive\r\n"
      #notfound += b"Server: CarterPortnoyServer/2.1.2024\r\n\r\n"
      connectionSocket.sendall(notfound)

      #Close client socket
      connectionSocket.close()
      # Next, close the file and server socket, right?

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)


'''# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)

  # Prepare a server socket
  serverSocket.bind(("127.0.0.1", port))
  serverSocket.listen(1)

  while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # Fill in start -are you accepting connections?     #Fill in end

    try:
      message =  connectionSocket.recv(1024) # Fill in start -a client is sending you a message   #Fill in end
      filename = message.split()[1]

      # opens the client requested file.
      # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rb")

      # This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?

      # Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"Server: CarterPortnoy\r\n\r\n"

    # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html

      for i in f:
        outputdata += i
        connectionSocket.send(outputdata)
        connectionSocket.close()  # closing the connection socket

    except Exception as e:
      oops = b"HTTP/1.1 404 Not Found\r\n"
      oops += b"Content-Type: text/html; charset=UTF-8\r\n"
      #oops += b"Connection: keep-alive\r\n\r\n"
      connectionSocket.send(oops)
      connectionSocket.close() # close connection socket
# Send response message for invalid request due to the file not being found (404)
# Remember the format you used in the try: block!

# Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
# serverSocket.close()
# sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
  webServer(13331)
'''
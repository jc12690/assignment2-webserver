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
  serverSocket.listen(port)

  while True:
    #Establish the connection
    #host = serverSocket.getsockname()
    #print(host)
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()


    try:
      # Client sends a message containing the file
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      #opens the client requested file.
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], 'rb')
      outputdata = f.read()
      f.close()

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?
      #Content-Type is an example on how to send a header as bytes. There are more!
      #outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      header = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\nServer: CarterPortnoyPythonServer/2.1.2024\r\n' #+ outputdata
      connectionSocket.send(header.encode())

      for i in f: #for line in file
      #Send the content of the requested file to the client (don't forget the headers you created)!
        connectionSocket.send(outputdata.encode())

        connectionSocket.close() #closing the connection socket

    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      header = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: keep-alive\r\nServer: CarterPortnoyPythonServer/2.1.2024\r\n' #+ outputdata
      connectionSocket.send(header.encode())

      #Close client socket
      connectionSocket.close()
      # Next, close the file and server socket, right?

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #f.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)

from bluetooth import *
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("98:D3:41:FD:5C:6D", 1))
while True:
    data = client_socket.recv(1024)
    print data
print "Finished"
client_socket.close()

from bluetooth import *
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("98:D3:41:FD:5C:6D", 1))

while True:
    data = client_socket.recv(1024)
    if data.find("!"):
        temp = data.split("!")
        for x in range(0,len(temp)-1):
            readData += x
        data = temp[len(temp)-1]
print "Finished"
client_socket.close()

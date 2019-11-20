from bluetooth import *
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("98:D3:41:FD:5C:6D", 1))
readData = ""
data = ""
while True:
    data += str(client_socket.recv(1),"utf-8")
    #print(data)
    if data.find("!"):
        temp = data.split("!")
        for x in range(0,len(temp)):
            readData += str(temp[x])
        data = temp[len(temp)-1]
        print(readData)
        readData = ""

print("Finished")
client_socket.close()

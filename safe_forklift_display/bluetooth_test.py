from bluetooth import *
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("98:D3:41:FD:5C:6D", 1))
readData = ""
data = ""
while True:
    data += str(client_socket.recv(3),"utf-8")
    data.replace("\n", "")

    #print(data)
    if data.find("!") != -1 :
        temp = data.split("!")
        readData = temp[0]
        data = temp[1]
        dataList = readData.split("#")
            for x in range(1,5):
		dataList[x] < distance:
		if x == 0: #Front
			sector = dataList[0]
			inputSector = (sector-18)%360/36
			print(inputSector)
		elif x == 1: #Back
			sector = (data[0] + 90)
			inputSector = (sector-18)%360/36

		elif x == 2: #Left
			sector = (data[0] + 180)%360
			inputSector = (sector-18)%360/36

		elif x == 3: #Right
			sector = (data[0] + 270)%360
			inputSector = (sector-18)%360/36
        print(readData)
        readData = ""


print("Finished")
client_socket.close()

import sys
import os
from threading import Thread
import time

from bluetooth import *
# Create the client socket
matrix = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def setObjectBackground(row,column,color):
    matrix[row][column] = color
def ledOn(led):
    if led == 0:
        setObjectBackground(0,2,'#')
    elif led == 1:
        setObjectBackground(1,3,'#')
    elif led == 2:
        setObjectBackground(2,4,'#')
    elif led == 3:
        setObjectBackground(3,4,'#')
    elif led == 4:
        setObjectBackground(4,3,'#')
    elif led == 5:
        setObjectBackground(5,2,'#')
    elif led == 6:
        setObjectBackground(4,1,'#')
    elif led == 7:
        setObjectBackground(3,0,'#')
    elif led == 8:
        setObjectBackground(2,0,'#')
    elif led == 9:
        setObjectBackground(1,1,'#')
def ledReset():
    setObjectBackground(0,2,' ')
    setObjectBackground(1,3,' ')
    setObjectBackground(2,4,' ')
    setObjectBackground(3,4,' ')
    setObjectBackground(4,3,' ')
    setObjectBackground(5,2,' ')
    setObjectBackground(4,1,' ')
    setObjectBackground(3,0,' ')
    setObjectBackground(2,0,' ')
    setObjectBackground(1,1,' ')
def printLed():
    for x in range(0,6):
        print(matrix[x])
    
def connectBluetooth():
    client_socket=BluetoothSocket( RFCOMM )
    client_socket.connect(("98:D3:41:FD:5C:6D", 1))
    readData = ""
    data = ""
    distance = 80
    while True:
        data += str(client_socket.recv(2),"utf-8")
        data.replace("\n", "")

        #print(data)
        distance = 40
        if data.find("!") != -1 :
            temp = data.split("!")
            readData = temp[0]
            data = temp[1]
            print(readData)
            dataList = readData.split("#")
            if len(dataList) < 5:
                continue
            sector = 0
            for x in range(1,5):
                temp = int(dataList[x])
                if temp < distance:
                    if x == 1: #Front
                        sector = int(dataList[0])
                    elif x == 2: #Back
                        sector = int(dataList[0])+ (90)
                    elif x == 3: #Left
                        sector = ((int(dataList[0]) + (180))%360)
                    elif x == 4: #Right
                        sector = ((int(dataList[0]) + 270)%360)
                    inputSector = int((sector-18)%360/36)
                    print(inputSector)
                    ledOn(inputSector)
            printLed()
            ledReset()
            #os.system('clear')
            """
                    t = Thread(target = ledOn,args = (inputSector))
                    t.start()
                    t.join()
                    t = Thread(target = ledReset)
                    t.start()
                    t.join()
"""

    print("Finished")
    client_socket.close()

connectBluetooth()
import sys,threading
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPalette
from PyQt5 import QtWidgets
from PyQt5 import uic
import time
#from bluetooth import *

# bluetooth inputType:1#1#1#1!
client_socket = ""
readData = ""
def connectBluetooth():
    client_socket=BluetoothSocket( RFCOMM )
    client_socket.connect(("98:D3:41:FD:5C:6D", 1))
def dataRead():
        data = client_socket.recv(1024)
        if data.find("!"):
            temp = data.split("!")
            for x in range(0,len(temp)-1):
                readData += x
            data = temp[len(temp)-1]






#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("untitled.ui")[0]
test = ""
#화면을 띄우는데 사용되는 Class 선언
class Form(QtWidgets.QDialog):

    def __init__(self,parent=None) :
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("untitled.ui")
        self.ui.show()
        self.matrix = []
        self.row0 = [self.ui.textEdit_00, self.ui.textEdit_01, self.ui.textEdit_02, self.ui.textEdit_03, self.ui.textEdit_04]
        self.row1 = [self.ui.textEdit_10, self.ui.textEdit_11, self.ui.textEdit_12, self.ui.textEdit_13, self.ui.textEdit_14]
        self.row2 = [self.ui.textEdit_20, self.ui.textEdit_21, self.ui.textEdit_22, self.ui.textEdit_23, self.ui.textEdit_24]
        self.row3 = [self.ui.textEdit_30, self.ui.textEdit_31, self.ui.textEdit_32, self.ui.textEdit_33, self.ui.textEdit_34]
        self.row4 = [self.ui.textEdit_40, self.ui.textEdit_41, self.ui.textEdit_42, self.ui.textEdit_43, self.ui.textEdit_44]
        self.row5 = [self.ui.textEdit_50, self.ui.textEdit_51, self.ui.textEdit_52, self.ui.textEdit_53, self.ui.textEdit_54]

        #self.textEdit_10.setStyleSheet("background-color: rgb(0,0,0);")
        self.matrix = [self.row0,self.row1,self.row2,self.row3,self.row4,self.row5]

    def setObjectBackground(self,row,column,color):
        if color == 0:
            self.matrix[row][column].setStyleSheet("background-color: rgb(0,0,0);")
        elif color == 1:
            self.matrix[row][column].setStyleSheet("background-color: rgb(255,255,255);")
        #self.matrix[row][column].repaint()
        self.update()
        #self.repaint()
        #self.matrix[row][column].setStyleSheet("background-color: rgb(0,0,0);")


def test():
    time.sleep(5)
    w.setObjectBackground(0, 4, 1)

app = QtWidgets.QApplication(sys.argv)
global w
w= Form()

w.setObjectBackground(0,4,0)
t = threading.Thread(target=test)
t.start()


sys.exit(app.exec())


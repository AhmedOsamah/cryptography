import base64
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import sql
import img
import back
import img

class UI_login(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI_login, self).__init__()
        uic.loadUi("login.ui",self)
        self.reggg.clicked.connect(self.reg)
        self.loginnn.clicked.connect(self.login)
    def login(self):
        name = self.name.text()
        passw = self.passw.text()
        ch  = sql.check(name,passw)
        if(ch):
            widget.setCurrentIndex(2)
        print(ch)
    def reg(self):
        widget.setCurrentIndex(1)
class UI_Regsiter(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI_Regsiter, self).__init__()
        uic.loadUi("Register.ui",self)
        self.exit.clicked.connect(self.exitWindow)
        self.reg.clicked.connect(self.info)

    def exitWindow(self):
            widget.close()


    def info(self):
        name = self.name.text()
        email = self.email.text()
        password = self.password.text()
        sql.add(name,email,password)
        self.name.setText("")
        self.email.setText("")
        self.password.setText("")




class wid(QtWidgets.QMainWindow):
    def __init__(self):
        super(wid, self).__init__()
        uic.loadUi("d.ui",self)

        self.RESET.clicked.connect(self.reseting)
        self.ex.clicked.connect(self.EXITTWindow)
        self.showw.clicked.connect(self.check)




    def reseting(self):
        self.lineEdit.setText(" ")
        self.lineEdit_2.setText(" ")
        self.lineEdit_3.setText(" ")
        self.lineEdit_4.setText(" ")

    def EXITTWindow(self):
            widget.close()


    def check(self):
        check = self.lineEdit_3.text()
        if(check=="E"):
            self.encode()
        elif(check=="D"):
            self.decode()
        else:
            print("wrong letter")

    # Function to encoding

    def encode(self):
        key = self.lineEdit_2.text()
        msg = self.lineEdit.text()
        enc = []
        for i in range(len(msg)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(msg[i]) +
                         ord(key_c)) % 256)
            enc.append(enc_c)
            print("enc:", enc)
        self.lineEdit_4.setText(base64.urlsafe_b64encode("".join(enc).encode()).decode())


    # Function to decode

    def decode(self):
        key = self.lineEdit_2.text()
        enc = self.lineEdit.text()
        dec = []

        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) -
                         ord(key_c)) % 256)

            dec.append(dec_c)
            print("dec:", dec)
        self.lineEdit_4.setText("".join(dec))

app= QtWidgets.QApplication(sys.argv)
ui1= UI_login()
ui2 = UI_Regsiter()
widget = QtWidgets.QStackedWidget()
widget.addWidget(ui1)
widget.addWidget(ui2)
widget.addWidget(wid())
widget.setCurrentIndex(2)
widget.setWindowTitle("Cryptography")
widget.resize(1300,670)
widget.setFixedSize(1100,670)

widget.show()
app.exec_()
import base64
from multiprocessing import connection
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import uic,  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import mysql.connector
import os
import random
from plyer import notification


mydb = mysql.connector.connect(
  host="your host name",
  user="your host username",
  password="your host password",
  database="database",
)
cur = mydb.cursor()

class hosgeldin(object):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(mainLogin)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 500)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 851, 501))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/mainGUIphoto/mainGUIphoto.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 111, 31))
        self.label_2.setStyleSheet("font: 18pt \"Coolvetica Rg\";\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 451, 91))
        self.label_3.setStyleSheet("font: 18pt \"Coolvetica Rg\";\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 111, 31))
        self.label_4.setStyleSheet("font: 18pt \"Coolvetica Rg\";\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 110, 761, 41))
        self.label_5.setStyleSheet("font: 18pt \"Coolvetica Rg\";\n"
"color:white;")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 110, 301, 51))
        self.pushButton.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font-family: coolvetica;\n"
"font-weight: regular;\n"
"font-size: 15px\n"
"")
        self.pushButton.setObjectName("pushButton2")
        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(810, 10, 31, 31))
        self.pushButton2.setStyleSheet("font-size: 16px;\n"
"background-color: transparent;\n"
"color: white;\n"
"font-family: Coolvetice;\n"
"font-weight: Bold;\n"
"")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton.clicked.connect(self.loginServer)
        self.pushButton.clicked.connect(self.createToken)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton2.clicked.connect(self.closeProgram)
        
    
    def closeProgram(self):
        pass
    def createToken(self):
        
        f = open("temporaryFile.txt","r")
        a = f.readline()
        token = str(random.randint(1000,10000))
        cur.execute("UPDATE accounts SET loginId = (%s) WHERE username = (%s)",(token,a))
        mydb.commit()
        self.label_4.setText(token)
        self.label_5.setText("Kodunuz verildi, belirtilen kod ile oyuna girebilirsiniz.")
        self.pushButton.hide()
        notification.notify(
            title = 'Black Roleplay',
            message = 'Black roleplay giriş kodunuz: '+token+" \n10 Dakika içerisinde giriş yapmazsanız kod değişecektir. Client üzerinden takip edebilirsiniz.",
            app_icon = None,
            timeout = 10,
        )
        
    def loginServer(self):
        os.startfile("mtasa://192.168.1.1")
        
    def retranslateUi(self, Dialog):
        f = open("temporaryFile.txt","r")
        a = f.readline()        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setWhatsThis(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/mainGUIphoto/mainGUIphoto.jpg\" /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Merhaba"))
        self.label_3.setText(_translate("Dialog", a))
        
        self.pushButton.setText(_translate("Dialog", "Sunucuya bağlanmak için tıkla"))
        self.pushButton2.setText(_translate("Dialog", "X"))

import guifotograflar_rc
   

class Ui_mainLogin(QLabel,QMainWindow,QWidget,object):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(mainLogin)
        
        
    def setupUi(self, mainLogin):
        mainLogin.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        mainLogin.setObjectName("mainLogin")
        mainLogin.resize(1200, 700)
        mainLogin.setStyleSheet("\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background-color: white;\n"
"\n"
"")
        self.loginImage = QtWidgets.QLabel(mainLogin)
        self.loginImage.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.loginImage.setStyleSheet("background-size: 500px,500px;")
        self.loginImage.setObjectName("loginImage")
        self.sizeLoginText = QtWidgets.QLabel(mainLogin)
        self.sizeLoginText.setGeometry(QtCore.QRect(800, 140, 211, 61))
        self.sizeLoginText.setStyleSheet("color: #29ABE2;\n"
"background-color: transparent;\n"
"font-size: 72px;\n"
"font-family: \"Nirmala UI\";\n"
"font-weight: bold;")
        self.sizeLoginText.setObjectName("sizeLoginText")
        self.cizgi = QtWidgets.QLabel(mainLogin)
        self.cizgi.setGeometry(QtCore.QRect(710, 320, 391, 3))
        self.cizgi.setStyleSheet("background-color: #29ABE2;\n"
"border: 0px;")
        self.cizgi.setText("")
        self.cizgi.setObjectName("cizgi")
        self.cizgi_2 = QtWidgets.QLabel(mainLogin)
        self.cizgi_2.setGeometry(QtCore.QRect(710, 420, 391, 3))
        self.cizgi_2.setStyleSheet("background-color: #29ABE2;\n"
"border: 0px;")
        self.cizgi_2.setText("")
        self.cizgi_2.setObjectName("cizgi_2")
        self.loginUsername = QtWidgets.QLineEdit(mainLogin)
        self.loginUsername.setGeometry(QtCore.QRect(710, 290, 391, 31))
        self.loginUsername.setStyleSheet("border: 0px, solid;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"color: #29ABE2;\n"
"font-size: 16px;\n"
"font-family: \"Nirmala UI\";\n"
"font-size: semilight;")
        self.loginUsername.setText("")
        self.loginUsername.setObjectName("loginUsername")
        self.loginPassword = QtWidgets.QLineEdit(mainLogin)
        self.loginPassword.setGeometry(QtCore.QRect(710, 390, 391, 31))
        self.loginPassword.setStyleSheet("border: 0px, solid;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"color: #29ABE2;\n"
"font-size: 16px;\n"
"font-family: \"Nirmala UI\";\n"
"font-size: semilight;")
        self.loginPassword.setText("")
        self.loginPassword.setObjectName("loginPassword")
        self.loginSend = QtWidgets.QPushButton(mainLogin)
        self.loginSend.setGeometry(QtCore.QRect(710, 460, 391, 51))
        self.loginSend.setStyleSheet("border: 0px, solid;\n"
"background-color:  #29ABE2;\n"
"color: white;\n"
"font-size: 24px;\n"
"font-family: \"Nirmala UI\";\n"
"font-weight: bold;")
        self.loginSend.setObjectName("loginSend")
        self.metin1 = QtWidgets.QLabel(mainLogin)
        self.metin1.setGeometry(QtCore.QRect(720, 520, 381, 20))
        self.metin1.setStyleSheet("border: 0px, solid;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"color: black;\n"
"font-size: 11px;\n"
"font-family: \"Nirmala UI\";\n"
"font-size: semilight;")
        self.metin1.setObjectName("metin1")
        self.metin2 = QtWidgets.QLabel(mainLogin)
        self.metin2.setGeometry(QtCore.QRect(800, 540, 201, 21))
        self.metin2.setStyleSheet("border: 0px, solid;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"color: black;\n"
"font-size: 11px;\n"
"font-family: \"Nirmala UI\";\n"
"font-size: semilight;\n"
"text-align:center;")
        self.metin2.setObjectName("metin2")
        self.loginFailed = QtWidgets.QLabel(mainLogin)
        self.loginFailed.setGeometry(QtCore.QRect(790, 220, 300, 35))
        self.loginFailed.setStyleSheet("color: transparent;\n")
        self.loginFailed.setObjectName("loginFailed")
        self.loginFailed.setHidden(True)
        self.loginSuccesfull = QtWidgets.QLabel(mainLogin)
        self.loginSuccesfull.setGeometry(QtCore.QRect(843, 220, 300, 35))
        self.loginSuccesfull.setStyleSheet("color: transparent;\n")
        self.loginSuccesfull.setHidden(True)
        self.loginSuccesfull.setObjectName("loginFailed")
        self.loginToRegister = QtWidgets.QPushButton(mainLogin)
        self.loginToRegister.setGeometry(QtCore.QRect(960, 540, 41, 21))
        self.loginToRegister.setStyleSheet("border: 0px, solid;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"color: #29ABE2;\n"
"font-size: 11px;\n"
"font-family: \"Nirmala UI\";\n"
"font-size: semilight;")
        self.loginToRegister.setObjectName("loginToRegister")

        self.retranslateUi(mainLogin)
        QtCore.QMetaObject.connectSlotsByName(mainLogin)
        self.loginSend.clicked.connect(self.failedSifirla)
        self.loginSend.clicked.connect(self.loginProg)
        

    def loginProg(self):
        
        username = self.loginUsername.text()
        password = self.loginPassword.text()
        cur.execute("SELECT username FROM accounts WHERE username = (%s)",(username,))
        if cur.fetchall():
            cur.execute("SELECT password FROM accounts WHERE password = (%s)",(password,))
            if cur.fetchall():
                self.loginSuccesfull.setHidden(False)
                self.loginSuccesfull.setStyleSheet("border: 0px, solid;\n"
"background-color: transparent;\n"
"background: transparent;\n"
"color: #24A824;\n"
"font-size: 18px;\n"
"font-family: \"Nirmala UI\";\n"
"font-weight: semilight;\n")
                time.sleep(3)
                cur.execute("SELECT username FROM accounts WHERE username = (%s) and password = (%s)",(username,password))
                g = cur.fetchall()
                all_strings = list(map(str, g))
                result = ''.join(all_strings)
                a = result.replace("('","")
                p = a.replace("',)","")
                f = open("temporaryFile.txt", "w")
                f.write(p)
                f.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = hosgeldin()
                self.ui.setupUi(self.window)
                mainLogin.hide()
                self.window.show()

            else:
                self.loginFailed.setHidden(False)
                self.loginFailed.setStyleSheet("border: 0px, solid;\n"
                                "background-color: transparent;\n"
                                "background: transparent;\n"
                                "color: #DE3636;\n"
                                "font-size: 18px;\n"
                                "font-family: \"Nirmala UI\";\n"
                                "font-weight: semilight;\n")
        else:
            self.loginFailed.setHidden(False)
            self.loginFailed.setStyleSheet("border: 0px, solid;\n"
                                "background-color: transparent;\n"
                                "background: transparent;\n"
                                "color: #DE3636;\n"
                                "font-size: 18px;\n"
                                "font-family: \"Nirmala UI\";\n"
                                "font-weight: semilight;\n")
        
    def failedSifirla(self):
        self.loginSuccesfull.setHidden(True)
        self.loginFailed.setHidden(True)
    def retranslateUi(self, mainLogin):
        _translate = QtCore.QCoreApplication.translate
        mainLogin.setWindowTitle(_translate("mainLogin", "Dialog"))
        self.loginImage.setText(_translate("mainLogin", "<html><head/><body><p><img src=\":/mainRegister/mainRegisterPhoto.png\"/></p></body></html>"))
        self.sizeLoginText.setText(_translate("mainLogin", "LOGIN"))
        self.loginSend.setText(_translate("mainLogin", "Login"))
        self.metin1.setText(_translate("mainLogin", "Log in now and take advantage of the opportunities XYZFD offers you."))
        self.metin2.setText(_translate("mainLogin", "If you do not have an account"))
        self.loginFailed.setText(_translate("mainLogin", "Username or password wrong"))
        self.loginSuccesfull.setText(_translate("mainLogin", "Login successful"))
        self.loginToRegister.setText(_translate("mainLogin", "register."))
        
import fotograflar_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainLogin = QtWidgets.QDialog()
    ui = Ui_mainLogin()
    ui.__init__(mainLogin)
    mainLogin.show()
    sys.exit(app.exec_())



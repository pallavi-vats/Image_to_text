# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rawat\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pyqt5_tools\tml222.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TEXT_TO_SPEECH(object):
    def setupUi(self, TEXT_TO_SPEECH):
        TEXT_TO_SPEECH.setObjectName("TEXT_TO_SPEECH")
        TEXT_TO_SPEECH.setWindowModality(QtCore.Qt.NonModal)
        TEXT_TO_SPEECH.resize(650, 542)
        TEXT_TO_SPEECH.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.477, y1:0.688, x2:0.517, y2:0, stop:0.0852273 rgba(0, 170, 255, 252), stop:1 rgba(255, 255, 255, 255));\n"
"QLineEdit{\n"
"background-color: rgb(51, 98, 255);\n"
"}\n"
"")
        TEXT_TO_SPEECH.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(TEXT_TO_SPEECH)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 261, 161))
        self.label.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 332, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 460, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 250, 291, 191))
        self.textEdit.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setScaledContents(True)
        self.label_2.setIndent(-1)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        TEXT_TO_SPEECH.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TEXT_TO_SPEECH)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        TEXT_TO_SPEECH.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(TEXT_TO_SPEECH)
        self.toolBar.setObjectName("toolBar")
        TEXT_TO_SPEECH.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(TEXT_TO_SPEECH)
        self.statusBar.setObjectName("statusBar")
        TEXT_TO_SPEECH.setStatusBar(self.statusBar)

        self.retranslateUi(TEXT_TO_SPEECH)
        QtCore.QMetaObject.connectSlotsByName(TEXT_TO_SPEECH)

        self.pushButton.clicked.connect(self.setImage)
        self.pushButton_2.clicked.connect(self.ocr)
        self.pushButton_3.clicked.connect(self.tts)
        
    def retranslateUi(self, TEXT_TO_SPEECH):
        _translate = QtCore.QCoreApplication.translate
        TEXT_TO_SPEECH.setWindowTitle(_translate("TEXT_TO_SPEECH", "MainWindow"))
        self.pushButton.setText(_translate("TEXT_TO_SPEECH", "select"))
        self.pushButton_2.setText(_translate("TEXT_TO_SPEECH", "Press to convert"))
        self.pushButton_3.setText(_translate("TEXT_TO_SPEECH", "Press to mp3 file"))
        self.label_2.setText(_translate("TEXT_TO_SPEECH", "        MP3 & TEXT CONVERTER"))
        self.toolBar.setWindowTitle(_translate("TEXT_TO_SPEECH", "toolBar"))

    def setImage(self):
        fileName, _=QtWidgets.QFileDialog.getOpenFileName(None, "Select Image","", "Image File(*.png *.jpg *jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.label.width(),self.label.height(),QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(pixmap)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            import pytesseract
            from PIL import Image

            pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

            result=pytesseract.image_to_string(fileName)

            with open('F:/abc.txt',mode='w') as file:
                file.write(result)
                
                

    def ocr(self):
        with open('F:/abc.txt',mode='r') as files:
            p=files.read(1000)
        self.textEdit.setText(p)

    def tts(self):
         with open('F:/abc.txt',mode='r') as files:
            p=files.read(1000)
         from gtts import gTTS
         import os
         mytext=p
         language='en'
         myobj=gTTS(text=mytext,lang=language,slow=False)
         myobj.save("F:/HELLO.mp3")
         os.system("mpg321 HELLO.mp3")
         print("Done")

         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TEXT_TO_SPEECH = QtWidgets.QMainWindow()
    ui = Ui_TEXT_TO_SPEECH()
    ui.setupUi(TEXT_TO_SPEECH)
    TEXT_TO_SPEECH.show()
    sys.exit(app.exec_())


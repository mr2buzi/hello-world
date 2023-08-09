# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Template.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 390)
        MainWindow.setStyleSheet("QFrame#frame{\n"
"    background-color: qlineargradient(spread:pad, x1:1.072045, y1:0.124, x2:0.368, y2:1, stop:0.227273 rgba(80, 214, 255, 155), stop:0.806818 rgba(112, 32,213,191));\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton#Closed{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(10,15,155,255);\n"
"    \n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#Closed:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"QPushButton#Closed:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QLineEdit#PlaylistLink{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:2px solid rgba(0,0,0,0);\n"
"    border-bottom-color: rgba(1,100,100,255);\n"
"    color:rgb(0,0,0);\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"\n"
"QPushButton#Select_Home{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(10,15,155,255);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Select_Home:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"\n"
"QPushButton#Select_Home:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 260, 350))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 13, 260, 41))
        self.label.setMaximumSize(QtCore.QSize(16777204, 16777215))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Closed = QtWidgets.QPushButton(self.frame)
        self.Closed.setGeometry(QtCore.QRect(230, 10, 20, 20))
        self.Closed.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Closed.setFont(font)
        self.Closed.setObjectName("Closed")
        self.PlaylistLink = QtWidgets.QLineEdit(self.frame)
        self.PlaylistLink.setGeometry(QtCore.QRect(30, 70, 200, 40))
        font = QtGui.QFont()
        font.setKerning(False)
        self.PlaylistLink.setFont(font)
        self.PlaylistLink.setMouseTracking(False)
        self.PlaylistLink.setAcceptDrops(False)
        self.PlaylistLink.setWhatsThis("Enter Spotify playlist Link")
        self.PlaylistLink.setStyleSheet("")
        self.PlaylistLink.setText("")
        self.PlaylistLink.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PlaylistLink.setClearButtonEnabled(True)
        self.PlaylistLink.setObjectName("PlaylistLink")
        self.PlaylistMsg = QtWidgets.QLabel(self.frame)
        self.PlaylistMsg.setGeometry(QtCore.QRect(30, 120, 201, 22))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(8)
        self.PlaylistMsg.setFont(font)
        self.PlaylistMsg.setWordWrap(True)
        self.PlaylistMsg.setObjectName("PlaylistMsg")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SongName = QtWidgets.QLabel(self.frame)
        self.SongName.setGeometry(QtCore.QRect(30, 163, 201, 71))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(10)
        self.SongName.setFont(font)
        self.SongName.setText("")
        self.SongName.setWordWrap(True)
        self.SongName.setObjectName("SongName")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 270, 201, 20))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setMinimumSize(QtCore.QSize(40, 0))
        self.label_7.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.statusMsg = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.statusMsg.setFont(font)
        self.statusMsg.setText("")
        self.statusMsg.setObjectName("statusMsg")
        self.horizontalLayout_3.addWidget(self.statusMsg)
        self.PlaylistMsg_2 = QtWidgets.QLabel(self.frame)
        self.PlaylistMsg_2.setGeometry(QtCore.QRect(30, 150, 201, 22))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(9)
        self.PlaylistMsg_2.setFont(font)
        self.PlaylistMsg_2.setWordWrap(True)
        self.PlaylistMsg_2.setObjectName("PlaylistMsg_2")
        self.CounterLabel = QtWidgets.QLabel(self.frame)
        self.CounterLabel.setGeometry(QtCore.QRect(30, 240, 201, 22))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(9)
        self.CounterLabel.setFont(font)
        self.CounterLabel.setWordWrap(True)
        self.CounterLabel.setObjectName("CounterLabel")
        self.Select_Home = QtWidgets.QPushButton(self.frame)
        self.Select_Home.setGeometry(QtCore.QRect(30, 300, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(9)
        self.Select_Home.setFont(font)
        self.Select_Home.setObjectName("Select_Home")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Spotify Downloader"))
        self.Closed.setText(_translate("MainWindow", "X"))
        self.PlaylistLink.setPlaceholderText(_translate("MainWindow", "Enter Spotify Playlist Link"))
        self.PlaylistMsg.setText(_translate("MainWindow", "Playlist Code : "))
        self.label_4.setText(_translate("MainWindow", "Created By Surenjanath"))
        self.label_7.setText(_translate("MainWindow", "Status :"))
        self.PlaylistMsg_2.setText(_translate("MainWindow", "Song Name  : "))
        self.CounterLabel.setText(_translate("MainWindow", "Counter : Songs downloaded 0"))
        self.Select_Home.setText(_translate("MainWindow", "Follow me on Medium"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

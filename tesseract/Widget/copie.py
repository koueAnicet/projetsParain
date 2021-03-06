# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/copie.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1151, 771))
        self.label_3.setStyleSheet("QLabel{\n"
"    background-color: rgb(165 ,130 ,135);\n"
"}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/img/Static/how-nature-benefits-mental-health.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(150, 100, 861, 551))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(15, 102, 125);\n"
"    border-radius:19px ;\n"
"border:0.5px solid white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lab_setImg = QtWidgets.QLabel(self.frame)
        self.lab_setImg.setGeometry(QtCore.QRect(570, 80, 241, 341))
        self.lab_setImg.setStyleSheet("QLabel{\n"
"background:rgb(28, 117, 47);\n"
"border:2px solid black;\n"
"border-radius:0px;\n"
"}")
        self.lab_setImg.setObjectName("lab_setImg")
        self.btn_transcribe = QtWidgets.QPushButton(self.frame)
        self.btn_transcribe.setGeometry(QtCore.QRect(360, 210, 141, 41))
        self.btn_transcribe.setStyleSheet("QPushButton{\n"
"background-color: rgb(24, 232, 51);\n"
"font:Italic 26 bold;\n"
"border-radius:14px;\n"
"border:0.5px  solid white;\n"
"}")
        self.btn_transcribe.setObjectName("btn_transcribe")
        self.lab_GetImg = QtWidgets.QLabel(self.frame)
        self.lab_GetImg.setGeometry(QtCore.QRect(50, 70, 241, 341))
        self.lab_GetImg.setStyleSheet("QLabel{background:rgb(238, 117, 47);\n"
"border:2px solid black;\n"
"border-radius:0px;\n"
"}")
        self.lab_GetImg.setObjectName("lab_GetImg")
        self.btn_addFile = QtWidgets.QPushButton(self.frame)
        self.btn_addFile.setGeometry(QtCore.QRect(100, 440, 141, 31))
        self.btn_addFile.setStyleSheet("QPushButton{\n"
"background-color: rgb(24, 232, 51);\n"
"font:Italic 15 bold;\n"
"border-radius:14px;\n"
"border:0.5px  solid white;\n"
"}")
        self.btn_addFile.setObjectName("btn_addFile")
        self.lab_setImg.raise_()
        self.btn_transcribe.raise_()
        self.btn_addFile.raise_()
        self.lab_GetImg.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_setImg.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">texte</p></body></html>"))
        self.btn_transcribe.setText(_translate("MainWindow", "transcribe"))
        self.lab_GetImg.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">image</p></body></html>"))
        self.btn_addFile.setText(_translate("MainWindow", "Add file"))
import ressource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

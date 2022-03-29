from distutils import command
import imp
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QTableWidgetItem
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,QPrintPreviewDialog
from Widget.imprimedata import Ui_MainWindow
import sqlite3

class AccountPage(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AccountPage, self).__init__()
        self.setupUi(self)
        #les buttons
        self.btn_print_file.clicked.connect(self.printView)
        self.btn_preview.clicked.connect(self.printPreview_dialog)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_save.clicked.connect(self.save)
        
        

    def printView(self):
        printer=QPrinter(QPrinter.ScreenResolution)
        dialog =QPrintDialog(printer ,self)

        if dialog.exec_()==QPrintDialog.accepted:
            self.view_infos.print_(printer)

    #un apperçu de pdf
    def printPreview_dialog(self):
        printer=QPrinter(QPrinter.ScreenResolution)
        printPreviewDialog= QPrintPreviewDialog(printer,self)
        printPreviewDialog.paintRequested.connect(self.printPreview)
        printPreviewDialog.exec_()

    def printPreview(self,printer):
        self.view_infos.print_(printer   )

    
    def save(self):
        if self.line_name.text()=="" or self.line_last_name.text()==""  or self.view.toPlainText()=="" :
            QMessageBox.warning(self,'Alert','Required fields!')
        else :
            
            elementSave={
                "name": self.line_name.text().upper(),
                "last_name": self.line_last_name.text().upper(),
                "comments": self.view.toPlainText()#pour obtenir le texte entrer dans "textEdit"
            } 
            
            #-----------------------connexion----------
            connexon = sqlite3.connect("data_base.db")

            c=connexon.cursor()

            command="""CREATE TABLE IF NOT EXISTS users(
                    name text,
                    last_name text,
                    comments text
                )"""
            
            c.execute(command)
            #---------------sinsertion des données-----------------------
            command1="INSERT INTO users  VALUES(:name, :last_name, :comments)"
            c.execute(command1,elementSave)

            command2="""SELECT * FROM users"""
            resultat=c.execute(command2)

            self.view_infos.setRowCount(0)

            for row_number,row_data in enumerate(resultat):
                self.view_infos.insertRow(row_number)
                
                for column_number,data in enumerate(row_data):
                    self.view_infos.setItem(row_number,column_number,QTableWidgetItem(str(data)))
            connexon.commit()
            connexon.close()
            QMessageBox.about(self,'succes','save!!')
            self.line_name.clear()
            self.line_last_name.clear()
            self.view.clear()   
    def reset(self):
        self.line_name.clear()
        self.line_last_name.clear()
        self.view.clear() 
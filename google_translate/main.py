from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton,QComboBox,QTextEdit, QMessageBox
from PyQt5 import uic
import sys
import googletrans
import textblob
import pyttsx3 #module de voice

class UI(QMainWindow):
    def __init__(self,):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi('app_ttranslate.ui', self)
        self.setWindowTitle('Translate App!')
        

        self.combo_1=self.findChild(QComboBox,"comboBox ")
        self.combo_2=self.findChild(QComboBox,"comboBox_2")

        self.text_1=self.findChild(QTextEdit,"textEdit")
        self.text_2=self.findChild(QTextEdit,"textEdit_2")

        self.t_button=self.findChild(QPushButton,"pushButton")
        self.c_button=self.findChild(QPushButton,"pushButton_2")

        #click the buttons
        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)
        
        #Add languages to the combo boxes

        self.languages = googletrans.LANGUAGES
        #print(self.languages)

        #cover to list
        self.languages_list = list(self.languages.values())
        #print(self.languages_list)

        # Add items to combo boxes
        self.comboBox.addItems(self.languages_list)
        self.comboBox_2.addItems(self.languages_list)

        #set default combo item
        self.comboBox.setCurrentText("english")
        self.comboBox_2.setCurrentText("german")
        #show app      
        self.show()

    def clear(self):
        #clear the text boxes   
        self.textEdit.setText("")
        self.textEdit_2.setText("")

        #reset the combo boxes
        self.comboBox.setCurrentText("english")
        self.comboBox_2.setCurrentText("german")
    def translate(self):
        try:
           #get translated language key
            for key, value in self.languages.items():
               if (value==self.comboBox.currentText()):
                   from_language_key= key
            
            #get translated language key
            for key, value in self.languages.items():
               if (value==self.comboBox_2.currentText()):
                   to_language_key= key
            # self.textEdit.setText(from_language_key)
            # self.textEdit_2.setText(to_language_key)

            #turn original teext into a textblob
            words = textblob.TextBlob(self.textEdit.toPlainText())

            #translate words!
            words = words.translate(from_lang=from_language_key,to=to_language_key)

            #output to text_2
            self.textEdit_2.setText(str(words))
            self.textEdit_2.setStyleSheet("font:Italic, 15, bold; color:red;")

            #Initialize  the speech engine
            engine = pyttsx3.init()

            #Pass words to speak
            engine.say(words)
            
            #run the engine
            engine.runAndWait()
        except Exception as e:
            QMessageBox.about(self,"tanslator",str(e))
    
#Initialize the App
app=QApplication(sys.argv)
UIWindow= UI()
app.exec_()
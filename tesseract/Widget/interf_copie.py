import imp
from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5.QtGui import QPixmap
from Widget.copie import Ui_MainWindow
#from tesseract import *
import pytesseract
#import cv2
from PIL import Image



class Tesseract(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Tesseract, self).__init__()
        self.setupUi(self)
        self.btn_addFile.clicked.connect(self.AddPhoto)
        self.btn_transcribe.clicked.connect(self.setTextImage)


    def AddPhoto(self):
        global photo_var
        file_name=QFileDialog.getOpenFileName(self,'Open File','Users/imac-05/Desktop')
        photo_var=file_name[0]
        self.lab_GetImg.setPixmap(QPixmap(file_name[0]))
        #self.affichLienPhoto.setText(file_name[0])
        #v=pytesseract.image_to_string(Image.open('/Users/imac-05/Desktop/fileExercice/tesseract/Static/jiuzhaigou-mountains-and-lakes-photo-by-ronan-oconnell.jpeg'))
        self.lab_setImg.setPixmap(QPixmap())
        
        return photo_var
    
    def setTextImage(self, photo_var):
        #img = cv2.imread('../Static/how-nature-benefits-mental-health.png')

        # Adding custom options
        #custom_config = r'--oem 3 --psm 6'
       print ( pytesseract.image_to_string ( 'images.txt' ))
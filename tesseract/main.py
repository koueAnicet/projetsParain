from PyQt5.QtWidgets import QApplication
from Widget.interf_copie import Tesseract
import sys


def main():
    app = QApplication(sys.argv)
    home = Tesseract()
    home.show()
    app.exec_()


if __name__ == '__main__':
    main()
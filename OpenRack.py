from ast import main
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from PyQt5.uic import loadUi
import sys
import ComicLibrary


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi(".\\mainwindow.ui", self)

        self.action_Open.triggered.connect(self.fileopener)
        self.actionScan_Library.triggered.connect(self.scanfolders)

    def fileopener(self):
        file = QFileDialog.getOpenFileName(self, ".\\")
    def scanfolders(self):
        libfiles = ComicLibrary.ReadFiles(ComicLibrary.librarydir)
        ComicLibrary.libscan('localhost','openrack','password','openrack',libfiles)
        

class PrefUI(QWidget):
    def __init__(self):
        super(PrefUI, self).__init__()
        loadUi(".\\preferences.ui", self)
    def scanfolders(self):
        for library in libraries:
            libfiles = ComicLibrary.Readfiles(ComicLibrary.librarydir)       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
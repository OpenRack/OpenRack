from ast import main
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from PyQt6.uic import loadUi
import sys
import ComicLibrary


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi(".\\mainwindow.ui", self)

        self.action_Open.triggered.connect(self.fileopener)
        self.actionScan_Library.triggered.connect(self.scanfolders)
        self.prefs = None
    def fileopener(self):
        file = QFileDialog.getOpenFileName(self, ".\\")
    def scanfolders(self):
        libfiles = ComicLibrary.ReadFiles(ComicLibrary.librarydir)
        ComicLibrary.libscan('localhost','openrack','password','openrack',libfiles)
    def openpreferences(self):
        if self.prefs is None:
            self.prefs = PrefWindow()
            self.prefs.show()
        else:
            self.prefs = None    
            
  
class PrefWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(".\\preferences.ui", self)   
    def addfolder(self):
        self.Preferences_Libraries_FolderAdd.clicked.connect(self.fileopener2)
    def fileopener2(self):
        file = QFileDialog.getOpenFileName(self, ".\\")    
    def scanfolders(self):
        for library in libraries:
            libfiles = ComicLibrary.Readfiles(ComicLibrary.librarydir)       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
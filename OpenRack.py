from ast import main
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from PyQt6.uic import loadUi
from PyQt6 import QtGui
import sys
import ComicLibrary
from configparser import ConfigParser as ConfParse
import yaml

with open('config.yml','r') as file:
    config = yaml.safe_load(file)

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi(".\\mainwindow.ui", self)

        self.action_Open.triggered.connect(self.fileopener)
        self.actionScan_Library.triggered.connect(self.scanfolders)
        self.prefs = None
    def fileopener(self):
        file = QFileDialog.getOpenFileName(self, ".\\")
        return file
    def scanfolders(self):
        libfiles = ComicLibrary.ReadFiles(ComicLibrary.librarydir)
        ComicLibrary.libscan('localhost','openrack','password','openrack',libfiles)
    def openpreferences(self):
        if self.prefs is None:
            self.prefs = PrefWindow()
            self.prefs.show()
        else:
            self.prefs = None    


libraries = yaml.reader(config.yml, file)       
  
class PrefWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi(".\\preferences.ui", self)
        self.Preferences_Libraries_FolderAdd.clicked.connect(self.addfolder)   
    def addfolder(self):
        folder = str(QFileDialog.getExistingDirectory(self))
        config['folders'].append(folder)
        with open('config.yml', 'w') as file:
            yaml.dump(config, file)           
    def scanfolders(self):
        for library in libraries:
            libfiles = ComicLibrary.Readfiles(ComicLibrary.librarydir)
    def removefolder(self):
        self.Preferences_Libraries_Folder
    def auto_write_to_db(self):
        None
    def write_comicinfo(self):
        None
    def backup_db(self):
        None
    def restore_db(self):
        None        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
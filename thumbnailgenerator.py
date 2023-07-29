import zipfile
import os
import ComicLibrary as cl
import sqlite3 as db
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from PyQt6.uic import loadUi
from PyQt6 import QtGui
import sys
#This should eventually pull paths from the db, currently using demo file
#db.connect()
library = "."

demofiles = cl.ReadFiles(library)


            
                

    
    def generatethumbs(files):
        for cbfile in files:
                if zipfile.is_zipfile(cbfile):
                    cbzip = zipfile.ZipFile(cbfile, 'r')
                    try:
                        thumbnail = cbzip.read('P00001.jpg')
                    except:
                        print("No pages found!")
        return thumbnail
    
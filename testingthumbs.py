import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QGridLayout
import zipfile
import os 

class ThumbnailGridWindow(QMainWindow):
    def __init__(self, files):
        super().__init__()
        self.setWindowTitle("Thumbnail Grid")
        self.setGeometry(100, 100, 800, 600)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        grid_layout = QGridLayout()
        
        thumbnails = generatethumbs(files)
        
        if thumbnails:
            row = 0
            col = 0
            for thumbnail in thumbnails:
                image_label = QLabel()
                pixmap = QPixmap()
                pixmap.loadFromData(thumbnail)
                pixmap = pixmap.scaled(QSize(100, 100), Qt.AspectRatioMode.KeepAspectRatio)
                image_label.setPixmap(pixmap)
                grid_layout.addWidget(image_label, row, col)
                
                col += 1
                if col == 5:  # Number of thumbnails per row
                    col = 0
                    row += 1
        
        layout.addLayout(grid_layout)
        central_widget.setLayout(layout)
        
def generatethumbs(files):
    thumbnails = []
    for cbfile in files:
        if zipfile.is_zipfile(cbfile):
            cbzip = zipfile.ZipFile(cbfile, 'r')
            try:
                thumbnail = cbzip.read('P00001.jpg')
                thumbnails.append(thumbnail)
            except:
                print("No pages found!")
    return thumbnails
librarydir = "E:\\Comics"

def ReadFiles(library):
    file_list = []
    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(library):
        # Print the name of each file
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list
if __name__ == "__main__":
    files = ReadFiles(librarydir)  # Example list of files
    app = QApplication(sys.argv)
    window = ThumbnailGridWindow(files)
    window.show()
    sys.exit(app.exec())
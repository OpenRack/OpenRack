import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
import xml.etree
from bs4 import BeautifulSoup
import sys

platform = sys.platform
if "linux" in platform:
    appdata = os.getenv('HOME')
if "win" in platform:    
    appdata = os.getenv('APPDATA')


#ComicRack DB location
dblocationcr = os.path.join(appdata, "cYo","ComicDb.xml")
#OpenRack DB location
dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )

#Function to create database
def MakeDB(directory):
    
    print('Performing initial XML structuring')
    # Sets ComicDatabase to an element tree
    ComicDatabase = ET.Element('ComicDatabase')
    # Creates a tree Element named Books inside of ComicDatabase
    Books = ET.SubElement(ComicDatabase, 'Books')
    # Creates a subelement named Book inside of Books
    Book = ET.SubElement(Books, 'Book')
    # Writes the XML tree to file
    tree = ET.ElementTree(ComicDatabase)
    f = (directory + "/OpenRack/ComicDB.xml")
    tree.write(f)
    
MakeDB(appdata)



librarydir = "C:\Users\cmathews\OneDrive - Midnight Monsters\Desktop\Test Directory"


def ReadFiles(library):
    file_list = []
    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(library):
        # Print the name of each file
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

        

library = ReadFiles(librarydir)


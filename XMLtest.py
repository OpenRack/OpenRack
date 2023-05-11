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
    #Sets ComicDatabase to an element tree named ComicDatabase
    ComicDatabase = ET.ElementTree ('ComicDatabase')
    #Creates a tree Element named Books inside of ComicDatabase
    Books = ET.Element('Books')
    #Creates a subelement named Book inside of Books
    Book = ET.SubElement(Books, 'Book')
    #ComicDatabase.write(directory+"/ComicDB.xml")

    tree = ET.ElementTree(ComicDatabase)
    f = open(directory + "/ComicDB.xml","wb")
    tree.write(f)
    
MakeDB(appdata)
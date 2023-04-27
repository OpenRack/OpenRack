import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
import xml.etree
from bs4 import BeautifulSoup
from methods import *
import sys
#All aspects of this code and repository are the intellectual property of Christopher Mathews. They may be shared and/or reused under the license specified in the repository. ("https://github.com/chrismathews393/OpenRack")
#Start in AppData
platform = sys.platform
if "linux" in platform:
    appdata = os.getenv('HOME')
if "win" in platform:    
    appdata = os.getenv('APPDATA')

#Set path to ComicRack or OpenRack Database
dblocationcr = os.path.join(appdata, "cYo","ComicDb.xml")
dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )

def MakeDB(directory):
    print('Performing initial XML structuring')
    ComicDatabase = ET.ElementTree ('ComicDatabase')
    Books = ET.Element(ComicDatabase, 'Books')
    Book = ET.SubElement(Books, 'Book')
    #ComicDatabase.write(directory+"/ComicDB.xml")

    tree = ET.ElementTree(ComicDatabase)
    f = open(directory + "/ComicDB.xml","wb")
    tree.write(f)

def CheckDB():
    global legacy
    comicdbexists = os.path.isfile(dblocationcr)
    opendbexists = os.path.isfile(dblocationor)
    if comicdbexists == True:
        legacy = 1
    elif opendbexists == True:
        legacy = 0
    else:
        legacy = 2
    return legacy

CheckDB()
print (legacy)

#bsdata = BeautifulSoup(db, "xml")

#tree = ET.parse(db)

if legacy == 1:
    print('Using ComicRack database')
    
if legacy == 0:
    print('Using OpenRack database')
    
if legacy == 2:
        MakeDB(appdata)
    


    
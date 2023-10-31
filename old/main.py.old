import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
import xml.etree
from bs4 import BeautifulSoup
#from methods import *
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
    # Creates ComicDatabase Element
    ComicDatabase = ET.Element('ComicDatabase')
    # Creates a tree Element named Books inside of ComicDatabase
    Books = ET.SubElement(ComicDatabase, 'Books')
    # Sets the tree var to the element tree
    tree = ET.ElementTree(ComicDatabase)
    f = (directory + "/OpenRack/ComicDB.xml")
    tree.write(f)

def CheckDB():
    global legacy
    comicdbexists = os.path.isfile(dblocationcr)
    opendbexists = os.path.isfile(dblocationor)
    if comicdbexists == True:
        legacy = 1
        print("1")
    elif opendbexists == True:
        legacy = 0
        print("0")
    else:
        legacy = 2
        print("2")
    return legacy

CheckDB()

if legacy == 1:
    print('Using ComicRack database')
    
if legacy == 0:
    print('Using OpenRack database')
    
if legacy == 2:
        MakeDB(appdata)


#create window after initialization

    

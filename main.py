import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from methods import *
import sys
#All aspects of this code and repository are the intellectual property of Christopher Mathews. They may be shared and/or reused under the license specified in the repository. ("https://github.com/chrismathews393/OpenRack")
#Start in AppData
platform = sys.platform
print(platform)
appdata = os.getenv('APPDATA')
#Set path to ComicRack or OpenRack Database
dblocationcr = os.path.join(appdata, "cYo","ComicDb.xml")
dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )

#Set legacy to null
legacy = 7
#Program attempts to find the comicrack database, if it exists, and sets legacy flag based on response. If no CR DB is found, it sets legacy to 0 and opens the OpenRack db

#Checks if DBs exist
comicdbexists = os.path.isfile(dblocationcr)
opendbexists = os.path.isfile(dblocationor)

if comicdbexists == True & opendbexists == False:
    legacy = 1
    #Uses CR DB
if comicdbexists == False & opendbexists == False:
    legacy = 2
    #NO DB! creates a new OR DB
if comicdbexists == False & opendbexists == True:
    legacy = 0
    #Uses existing OR DB

#Do Both DBs exist?
valueset = False   
while comicdbexists == True & opendbexists == True & valueset == False:
    print("Do you want to proceed with the OpenRack DB or the ComicRack DB?")
    whichdb = input()
    #if whichdb != '1' and whichdb != '2':
    #    print(whichdb+" is not an acceptable answer.")
    #else:
    #    break
    if whichdb == 'OpenRack':
            legacy = 0
            valueset == True
            break
    if whichdb == 'ComicRack':
            legacy = 1
            valueset == True
            break
    
    
    

#bsdata = BeautifulSoup(db, "xml")

#tree = ET.parse(db)

if legacy == 1:
    print('Using ComicRack database')
    
if legacy == 0:
    print('Using OpenRack database')
    
if legacy == 2:
        MakeDB()
    


    
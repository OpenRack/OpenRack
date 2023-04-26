import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
#All aspects of this code and repository are the intellectual property of Christopher Mathews. They may be shared and/or reused under the license specified in the repository. ("https://github.com/chrismathews393/OpenRack")
#Start in AppData
appdata = os.getenv('APPDATA')
#Set path to ComicRack or OpenRack Database
dblocationcr = os.path.join(appdata, "cYo","ComicDb.xml")
dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )

#Set legacy to null
legacy = None
#Program attempts to find the comicrack database, if it exists, and sets legacy flag based on response. If no CR DB is found, it sets legacy to 0 and opens the OpenRack db
try:
    db = open(dblocationcr,'r+', encoding="utf8")
    legacy = 1
except:
    db = open(dblocationor, 'r+', encoding="utf8")
    legacy = 0


bsdata = BeautifulSoup(db, "xml")

tree = ET.parse(db)

if legacy == 1:
    print('Using ComicRack database')
    
if legacy == 0:
    print('Using OpenRack database')
    dbexists = os.path.isfile(dblocationor)
    if dbexists == True:
        print("db exists, proceeding")
    else:
        print('Performing initial XML structuring')
        ComicDatabase = ET.Element ('ComicDatabase')
        Books = ET.SubElement(ComicDatabase, 'Books')
        Book = ET.SubElement(Books, 'Book')
        tags = ["Title","Series","Number","Count","Volume","AlternateSeries / AlternateNumber / AlternateCount","Summary","Notes","Year / Month / Day","Creator fields","Publisher","Imprint","Genre","Tags","Web","PageCount","LanguageISO","BlackAndWhite","Manga","Characters","Teams","Locations","MainCharacterOrTeam","ScanInformation","StoryArc","StoryArcNumber","SeriesGroup","AgeRating","CommunityRating","Review","GTIN","Pages / ComicPageInfo"]
        for tag in tags:
            subelement = ET.SubElement(Book, tag)


    
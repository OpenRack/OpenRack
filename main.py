import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

appdata = os.getenv('APPDATA')
dblocationcr = os.path.join(appdata, "cYo","ComicDb.xml")
dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )

legacy = None
try:
    db = open(dblocationcr,'r+', encoding="utf8")
    legacy = 1
except:
    db = open(dblocationor, 'r+', encoding="utf8")
    legacy = 0


#bsdata = BeautifulSoup(db, "xml")

tree = ET.parse(db)

if legacy == 1:
    print('Using ComicRack database')
    
if legacy == 0:
    print('Using OpenRack database')
    print('Performing initial XML structuring')
    ComicDatabase = ET.Element ('ComicDatabase')
    Books = ET.SubElement(ComicDatabase, 'Books')
    Book = ET.SubElement(Books, 'Book')
    tags = ["Title","Series","Number","Count","Volume","AlternateSeries / AlternateNumber / AlternateCount","Summary","Notes","Year / Month / Day","Creator fields","Publisher","Imprint","Genre","Tags","Web","PageCount","LanguageISO","BlackAndWhite","Manga","Characters","Teams","Locations","MainCharacterOrTeam","ScanInformation","StoryArc","StoryArcNumber","SeriesGroup","AgeRating","CommunityRating","Review","GTIN","Pages / ComicPageInfo"]
    for tag in tags:
        subelement = ET.SubElement(Book, tag)

    
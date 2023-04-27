import os
import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from main import dblocationcr, dblocationor

#def MakeDB(directory):
 #   print('Performing initial XML structuring')
  #  ComicDatabase = ET.Element ('ComicDatabase')
   ##Book = ET.SubElement(Books, 'Book')
   # ET.write(directory+"ComicDB.xml")
    




#tags = ["Title","Series","Number","Count","Volume","AlternateSeries / AlternateNumber / AlternateCount","Summary","Notes","Year / Month / Day","Creator fields","Publisher","Imprint","Genre","Tags","Web","PageCount","LanguageISO","BlackAndWhite","Manga","Characters","Teams","Locations","MainCharacterOrTeam","ScanInformation","StoryArc","StoryArcNumber","SeriesGroup","AgeRating","CommunityRating","Review","GTIN","Pages / ComicPageInfo"]
#    for tag in tags:
#        ET.SubElement(Book, tag)
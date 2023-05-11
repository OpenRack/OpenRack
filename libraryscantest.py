import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
import xml.etree
from bs4 import BeautifulSoup
import sys
import zipfile

librarydir = "C:\\Users\\cmathews\\OneDrive - Midnight Monsters\\Desktop\\Test Directory\\"


def ReadFiles(library):
    file_list = []
    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(library):
        # Print the name of each file
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

ReadFiles(librarydir)
files = ReadFiles(librarydir)

for cbfile in files:
    if zipfile.is_zipfile(cbfile):
        cbzip = zipfile.ZipFile(cbfile, 'r')
        comicinfo = cbzip.read('ComicInfo.xml')
        print(comicinfo)
    else:
        print("ooga")
        




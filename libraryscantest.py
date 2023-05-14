import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
import xml.etree
from bs4 import BeautifulSoup
import sys
import zipfile

librarydir = "C:\\Users\\cmathews\\OneDrive - Midnight Monsters\\Desktop\\Test Directory\\"
platform = sys.platform
if "linux" in platform:
    appdata = os.getenv('HOME')
if "win" in platform:    
    appdata = os.getenv('APPDATA')
dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )
def ReadFiles(library):
    file_list = []
    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(library):
        # Print the name of each file
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def xml_data_transfer(source_xml, target_file):
    # Parse the source XML file
    root = ET.fromstring(source_xml)

    # Create the target XML file with the root element
    target_tree = ET.ElementTree(ET.Element(root.tag))
    target_root = target_tree.getroot()

    # Loop through the child elements of the source root
    for child in root:
        # Copy the child element to the target root
        target_root.append(child)

    # Write the target XML file
    target_tree.write(target_file)

ReadFiles(librarydir)
files = ReadFiles(librarydir)

for cbfile in files:
    print(cbfile)
    if zipfile.is_zipfile(cbfile):
        cbzip = zipfile.ZipFile(cbfile, 'r')
        comicinfo = cbzip.read('ComicInfo.xml')
        print(comicinfo)
        xml_data_transfer(comicinfo,dblocationor)
#
#        print(comicinfo)
#    else:
#        print("ooga")
        


#xml_data_transfer(,dblocationor)



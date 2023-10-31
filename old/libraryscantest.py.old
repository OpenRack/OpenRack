import os, re, fnmatch, zipfile
import xml.etree.ElementTree as ET
import xml.etree
from bs4 import BeautifulSoup
import sys
import zipfile
import uuid

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
    
    if zipfile.is_zipfile(cbfile):
        idgen = uuid.uuid4()
        cbzip = zipfile.ZipFile(cbfile, 'r')
        comicinfo = cbzip.read('ComicInfo.xml')
        bookinfo=ET.fromstring(comicinfo)
        destination_tree = ET.parse(dblocationor)
        ET.indent(destination_tree, space="\t", level=0)
        destination_root = destination_tree.find('Books')
        book = ET.SubElement(destination_root,'Book')
        book.set('ID',idgen)
        book.set('File',cbfile)
        for element in bookinfo:
            book.append(element)
        destination_tree.write(dblocationor)
        print(comicinfo)
#    else:
#        print("ooga")
        


'''# Parse the source XML strings into ElementTree objects
source_tree_1 = ET.fromstring(source_xml_1)
source_tree_2 = ET.fromstring(source_xml_2)

# Create an empty destination ElementTree object
destination_tree = ET.parse(dblocationor)
destination_root = destination_tree.getroot()

# Loop through each element in source_tree_1 and add it to the destination root
for element in source_tree_1:
    destination_root.append(element)

# Loop through each element in source_tree_2 and add it to the destination root
for element in source_tree_2:
    destination_root.append(element)

# Write the destination tree to a file
destination_tree.write(dblocationor)

#xml_data_transfer(,dblocationor)
'''



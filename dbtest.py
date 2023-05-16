# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import mysql.connector as db
import os, sys
from xml.etree import ElementTree
import zipfile, uuid


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

'''def xml_data_transfer(source_xml, target_file):
    # Parse the source XML file
    root = ElementTree.fromstring(source_xml)

    # Create the target XML file with the root element
    target_tree = ET.ElementTree(ET.Element(root.tag))
    target_root = target_tree.getroot()

    # Loop through the child elements of the source root
    for child in root:
        # Copy the child element to the target root
        target_root.append(child)

    # Write the target XML file
    target_tree.write(target_file)
'''
ReadFiles(librarydir)
files = ReadFiles(librarydir)

Host = 'localhost'
User = 'openrack'
Password = 'password'
Database = 'Openrack'
addbook = ("INSERT INTO openrack "
           "(id, comicinfo, filepath) "
           "VALUES (null, %s, %s)")
conn = db.connect(host=Host,user=User,password=Password,database=Database)
cursor = conn.cursor()

#cursor.execute("CREATE TABLE openrack (id MEDIUMINT NOT NULL AUTO_INCREMENT,comicinfo TEXT,filepath TEXT, PRIMARY KEY (id))")
for cbfile in files:
    
    if zipfile.is_zipfile(cbfile):
        #idgen = uuid.uuid4()
        cbzip = zipfile.ZipFile(cbfile, 'r')
        comicinfo = cbzip.read('ComicInfo.xml')
        #bookinfo = ElementTree.tostring(comicxml, encoding='unicode', method='xml')
        id = cursor.lastrowid
        bookdata = (comicinfo,cbfile)
        cursor.execute (addbook, bookdata)
        conn.commit()
cursor.close()
conn.close()












'''
conn = db.connect(host=Host,user=User,password=Password)

cur = conn.cursor()

cur.execute("CREATE DATABASE OPENRACK")

cur.execute("SHOW DATABASES")
dblist = cur.fetchall()

for database in dblist:
    print(database)


conn.close()
'''
import os, zipfile
#import mysql.connector as db
import sqlite3 as db
import sys




platform = sys.platform
if "linux" in platform:
    appdata = os.getenv('HOME')
if "win" in platform:    
    appdata = os.getenv('APPDATA')
    
dblocationor = os.path.join(appdata, "OpenRack")


librarydir = "E:\\Comics"

def ReadFiles(library):
    file_list = []
    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(library):
        # Print the name of each file
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list



# def dbconnecttest():
#     print(dblocationor)
#     conn = db.connect(dblocationor+"\\openrack.db")

# def dbmake():

#     conn = db.connect(dblocationor+"\\openrack.db")
#     cursor = conn.cursor()
#     cursor.execute("CREATE TABLE openrack (id INTEGER NOT NULL,comicinfo TEXT,filepath TEXT, PRIMARY KEY (id))")
#     cursor.close()
#     conn.close()
    
def libscan(files):
    try:
        conn = db.connect(dblocationor+"\\openrack.db")
        cursor = conn.cursor()

        for cbfile in files:
            if zipfile.is_zipfile(cbfile):
                cbzip = zipfile.ZipFile(cbfile, 'r')
                try:
                    comicinfo = cbzip.read('ComicInfo.xml')
                except:
                    print("fuck")
                # Check if the file exists in the database
                query = "SELECT id, comicinfo FROM openrack WHERE filepath = ?"
                cursor.execute(query, (cbfile,))
                existing_entry = cursor.fetchone()
                
                if existing_entry:
                    existing_id, existing_comicinfo = existing_entry
                    update_query = "UPDATE openrack SET comicinfo = ? WHERE id = ?"
                    cursor.execute(update_query, (comicinfo, existing_id))
                    conn.commit()
                    print("ComicInfo updated for entry:", existing_id)
                else:
                    # Insert new entry into the database
                    addbook = "INSERT INTO openrack (id, comicinfo, filepath) VALUES (null, ?, ?)"
                    bookdata = (comicinfo, cbfile)
                    cursor.execute(addbook, bookdata)
                    conn.commit()
                    print("New entry created:", cursor.lastrowid)
        
    except db.Error as err:
        print("Error:", err)
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    
libfiles = ReadFiles(librarydir)

libscan(libfiles)

#dbmake()
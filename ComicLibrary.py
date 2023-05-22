import os, zipfile
import mysql.connector as db


librarydir = "C:\\Users\\cmathews\\OneDrive - Midnight Monsters\\Desktop\\Test Directory"

def ReadFiles(library):
    file_list = []
    # Iterate through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(library):
        # Print the name of each file
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

'''def UpdateDB(host, user, password, database, files):
    addbook = ("INSERT INTO openrack "
           "(id, comicinfo, filepath) "
           "VALUES (null, %s, %s)")
    conn = db.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor
    for cbfile in files:
        
        if zipfile.is_zipfile(cbfile):
            cbzip = zipfile.ZipFile(cbfile, 'r')
            comicinfo = cbzip.read('ComicInfo.xml')
            check if file exists in zip
                file = id
                id = filename OR lastrowid
            if exists == False:
                id = cursor.lastrowid
            bookdata = (comicinfo,cbfile)
            cursor.execute (addbook, bookdata)
            conn.commit()
    cursor.close()
    conn.close()
'''    
    
def libscan(host, user, password, database, files):
    try:
        conn = db.connect(host=host, user=user, password=password, database=database)
        cursor = conn.cursor()

        for cbfile in files:
            if zipfile.is_zipfile(cbfile):
                cbzip = zipfile.ZipFile(cbfile, 'r')
                comicinfo = cbzip.read('ComicInfo.xml')
                
                # Check if the file exists in the database
                query = "SELECT id, comicinfo FROM openrack WHERE filepath = %s"
                cursor.execute(query, (cbfile,))
                existing_entry = cursor.fetchone()
                
                if existing_entry:
                    existing_id, existing_comicinfo = existing_entry
                    update_query = "UPDATE openrack SET comicinfo = %s WHERE id = %s"
                    cursor.execute(update_query, (comicinfo, existing_id))
                    conn.commit()
                    print("ComicInfo updated for entry:", existing_id)
                else:
                    # Insert new entry into the database
                    addbook = "INSERT INTO openrack (id, comicinfo, filepath) VALUES (null, %s, %s)"
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
    
#libfiles = ReadFiles(librarydir)

#libscan('localhost','openrack','password','openrack',libfiles)
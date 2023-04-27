import sys, os


platform = sys.platform
if "linux" in platform:
    appdata = os.getenv('HOME')
if "win" in platform:    
    appdata = os.getenv('APPDATA')
print (appdata)

dblocationor = os.path.join(appdata, "OpenRack", "ComicDb.xml" )
print(dblocationor)
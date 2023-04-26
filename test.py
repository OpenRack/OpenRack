comicdbexists = True
opendbexists = True

while comicdbexists == True & opendbexists == True:
    print("Do you want to proceed with the OpenRack DB(1) or the ComicRack DB(2)?")
    whichdb = input()
    if whichdb != 1 or 2:
        print(whichdb + " is not an acceptable answer.")
        continue
    else:
        if whichdb == 1:
            legacy = 0
        if whichdb == 2:
            legacy = 1
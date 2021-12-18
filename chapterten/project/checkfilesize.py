#! python3
# checkfilesize.py - walks through a folder, checks files above 100mb

import os

filesize = 100000000   #100,000,000 Bytes

for folderName, subfolders, filenames in os.walk('chapterten/Chapter project/delicious'):

    for subfolder in subfolders:
        size = os.path.getsize(folderName + '/' + subfolder)
        if size > filesize:
            print(folderName + '/' + subfolder)
            

    for filename in filenames:
        size = os.path.getsize(folderName + '/'+ filename)
        if size > filesize:
            print(folderName + '/' + filename)
            

        

#! python3
# filefindpaste.py - walks through a folder, finds file with .pdf and .jpg extension
# and paste it to a new folder

import shutil, os


for folderName, subfolders, filenames in os.walk('chapterten/Chapter project/delicious'):

    for filename in filenames:
        split = filename.split('.')
        if split[1] =='txt' or split[1]=='pdf':
            filepath = folderName+'/'+filename
            folderpath = 'chapterten/project/txtandpdf/'
            shutil.copy(filepath,folderpath)

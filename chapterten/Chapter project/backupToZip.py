#! python3
# backupToZip.py  - Copies an entire folder and its contents into a zipfile whose filename increments.

import zipfile,os

def backupToZiip(folder):
    folder = os.path.abspath(folder)
    number =1
    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not  os.path.exists(zipFilename):
            break
        number+=1
    
    print('Done')
backupToZiip('./delicious')
#! python3
# fillinggaps.py - finds gap between file name

import re, shutil,os

def getfilelist(folderpath):
    list = []
    list2 = []
    fileRegex = re.compile(r'(spam)((\d)(\d)(\d))\.txt')
    files = os.listdir(folderpath)
    for file in files:
        list.append(file)
    for filename in list:
        mo = fileRegex.search(filename)
        if mo != None:
            list2.append(mo.group(0))
    list = list2
    return(list)

def fillgap(list):
    for i in range(len(list)):
        if i+1<10:
            shutil.move(folderpath+'/'+list[i],folderpath+'/'+"spam00{}.txt".format(i+1))
        if i+1<100 and i>9:
            shutil.move(folderpath+'/'+list[i],folderpath+'/'+"spam0{}.txt".format(i+1))
        if i+1>99 and i<1000:
            shutil.move(folderpath+'/'+list[i],folderpath+'/'+"spam{}.txt".format(i+1)) 

# def addgap(number,list):
#     open("myfile.txt", "x")
#     list.append("spam009.txt")
#     for i in range(len(list)):
#         if i+1<10:
#             list[i]="spam00{}.txt".format(i+1)
#         if i+1<100 and i>9:
#             list[i]="spam0{}.txt".format(i+1)
#         if i+1>99 and i<1000:
#             list[i]="spam{}.txt".format(i+1)
#     return list
        

    

folderpath = 'chapterten/project/files'
list = getfilelist(folderpath)
fillgap(list)
list = getfilelist(folderpath)
# list = addgap(2,list)
# fillgap(list)







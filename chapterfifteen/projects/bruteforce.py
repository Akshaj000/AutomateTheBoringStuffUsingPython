import os,PyPDF2,sys
from pathlib import Path

if len(sys.argv)>1:
    filepath = sys.argv[1]

names = open(filepath)
names = names.read()
names = names.split(sep='\n')

pdfReader = PyPDF2.PdfFileReader(open('bftest.pdf', 'rb'))
for i in names:
    print("Checking if ",i," ---------> False")
    l = pdfReader.decrypt(i.lower()) 
    u = pdfReader.decrypt(i)
    if l == 1 or u == 1:
        print("Password is : ",i)
        break

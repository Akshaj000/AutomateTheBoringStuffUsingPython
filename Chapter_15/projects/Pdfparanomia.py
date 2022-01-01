#! python3
# Pdfparanomia.py - walk through folders and subfolders, encrypts and decrypts all the pdffile

import os,PyPDF2,sys
from pathlib import Path

filepath = "AutomateTheBoringStuffUsingPython/chapterfifteen"
password = "petterpan"
if len(sys.argv) > 1:
    filepath = sys.argv[1]
    password = sys.argv[2]

pdfs = []

def walk(path):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".pdf"):
                pdfs.append(folderName + '/'+ filename)

def encrypt(filepath, code):
    pdfReader = PyPDF2.PdfFileReader(open(filepath, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()
    if not pdfReader.isEncrypted:
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt(code)
        p = Path(filepath)
        newPath = str(p.stem)+"_encrypted"+str(p.suffix)
        resultPdf = open(newPath, 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        
def decrypt(filepath,code):
    pdfReader = PyPDF2.PdfFileReader(open(filepath, 'rb'))
    pdfWriter = PyPDF2.PdfFileWriter()
    if  pdfReader.isEncrypted:
        a = pdfReader.decrypt(code)
        if a == 0:
            return
        print(a)
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        pdfWriter.encrypt(code)
        p = Path(filepath)
        newPath = str(p.stem)+"_decrypted"+str(p.suffix)
        resultPdf = open(newPath, 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()


cur = Path.cwd()
try:
    os.mkdir(str(cur)+'/Encryptedpdfs')
    os.mkdir(str(cur)+'/Decryptedpdfs')
except FileExistsError:
    pass
os.chdir(str(cur)+'/Encryptedpdfs')
walk(filepath)
for i in pdfs:
    encrypt(i,password)
os.chdir(str(cur)+'/Decryptedpdfs')
for i in pdfs:
    decrypt(i,password)
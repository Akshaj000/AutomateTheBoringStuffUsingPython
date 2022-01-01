import os,sys
import openpyxl,sys
from openpyxl.styles import Font

if len(sys.argv) > 1:
    path = sys.argv[1]
    row,column = 1,1;
    wb = openpyxl.Workbook()
    sheet = wb.active
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            file = open(path+"/"+filename)
            read = file.readlines()
            for i in read:
                sheet.cell(row=row,column=column).value = i
                row+=1
            row=1
            column+=1
            file.close()
    wb.save('textfiletoexcel000.xlsx')
    

else:
    print("Enter arguement n!")

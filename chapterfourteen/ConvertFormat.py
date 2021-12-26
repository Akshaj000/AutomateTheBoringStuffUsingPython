#! python3
# Converts format of File to Required Format

import ezsheets
import pyinputplus as pyip

print('Enter filepath to convert : ')
path = pyip.inputStr()
print('''
Enter 1 to convert to .xlsx 
Enter 2 to convert to .ods
Enter 3 to convert to .csv
Enter 4 to convert to .tsv
Enter 5 to convert to .pdf
Enter 6 to convert to .zip
''')
opt = pyip.inputInt()
ss = ezsheets.upload(path)
if opt == 1:
    ss.downloadAsExcel()
elif opt == 2:
     ss.downloadAsODS()
elif opt == 3:
    ss.downloadAsCSV()
elif opt == 4:
    ss.downloadAsTSV()
elif opt == 5:
    ss.downloadAsPDF()
elif opt == 6:
    ss.downloadAsHTML()
else:
    print("Invalid Entry")





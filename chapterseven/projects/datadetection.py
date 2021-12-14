#! python3
# datedetection.py - Finds dates on the clipboard.

import pyperclip, re, sys

dateRegex = re.compile(r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([1-9][0-9]{3})')

day,month,year=[],[],[]


text = str(pyperclip.paste())


for groups in dateRegex.findall(text):
    day.append(groups[0])
    month.append(groups[1])
    year.append(groups[2])

A=True
if len(month)==0:
    A=False
    print("No date found")
    sys.exit()
while A:
    minm = len(month)
    for i in range(len(month)):
        if  int(day[i])>30 and (month[i] =='04' or month[i] == '06' or month[i] =='09' or month[i] =='11') :
            del day[i]
            del month[i]
            del year[i]
            break
        elif int(day[i]) > 31:
            del day[i]
            del month[i]
            del year[i]
            break
     
        if (month[i] == '02' and int(year[i])%4==0) or (month[i] == '02' and int(year[i])%100==0 and int(year[i])%400==0):
            if int(day[i])>28:
                del day[i]
                del month[i]
                del year[i]
                break
    if minm == len(month):
        A=False
    else:
        minm = min(minm,len(month))

if len(day)==0:
    print("No date found")
else:
    string=""
    print("--dates--")
    for i in range(len(day)):
        string=day[i]+"-"+month[i]+"-"+year[i]
        pyperclip.copy(string)
        print(string)
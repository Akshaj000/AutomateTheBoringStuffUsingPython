#INCOMPLETE

#! python3
# passworddetection.py - check whether password is strong or not.

import pyperclip, re
text = str(pyperclip.paste())

text='akshaaaA0AAA'

checklengthRegex = re.compile(r'^([(a-z)(A-z)(0-9)]{8,})$')
checknumberRegex = re.compile(r'\d')
a,b = checklengthRegex.search(text),checknumberRegex.search(text)
a,b = a!=None,b!=None
print(a and b)

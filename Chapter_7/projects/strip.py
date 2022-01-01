
#! python3
# strip.py - strips the string from left and right.

import pyperclip, re
text = pyperclip.paste()
strip = re.sub(r'^\s+|\s+$', '', text)
pyperclip.copy(strip)    
print(strip)

from os import read
import re
from pathlib import Path

usr_input = input()
p = Path('chapternine/chapterprojects/randomquizgenerator')
for i in p.glob('*.txt'):
    file = open(i)
    read = file.read()
    haRegex = re.compile(usr_input)
    mo1 = haRegex.search(read)
    if mo1 != None:
        print(i)
    file.close()
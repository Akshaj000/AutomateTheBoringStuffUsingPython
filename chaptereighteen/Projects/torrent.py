import ezgmail
import re
import subprocess
import time

ezgmail.init()
file = open("Email_collected.txt","w")
resultThreads = ezgmail.search('label:unread asrvlogs000@gmail.com')
regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

while True:
    try:
        i=0
        while True:
            a = resultThreads[i].messages[0].body
            if a != None:
                url = re.findall(regex,a)
                for j in url:
                    x = re.search('.torrent$', j[0])
                    if x != None:
                        link = j[0]
                        subprocess.Popen(['/usr/bin/qbittorrent',str(link)])
                        
            i+=1
                
    except IndexError:
        print("No links found")
    
    time.sleep(900)
#opens only few links
import webbrowser
import ezgmail
import re

ezgmail.init()
unreadThreads = ezgmail.unread() # List of GmailThread objects.
regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

try:
    i=0
    while True:
        a = unreadThreads[i].messages[0].body
        if a != None:
            if "unsubscribe" in a or "Unsubscribe" in a:
                url = re.findall(regex,a)
                for j in url:
                    if "unsubscribe" in j[0] or "Unsubscribe" in j[0]: 
                        webbrowser.open(j[0])
                    
        i+=1
        
except IndexError:
    pass

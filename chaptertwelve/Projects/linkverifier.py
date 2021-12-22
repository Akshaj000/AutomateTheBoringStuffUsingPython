#! python3
# linkverifier.py - prints  pages that have 404 "not found" code
# give url as arguement to parse through it

import sys,bs4,requests

url = "https://blog.fluidui.com/top-404-error-page-examples/"
file = open('links.txt','a')

if len(sys.argv) == 2:
    url = sys.argv[1]

response = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text,'html.parser')
links = soup.select("a")
for i in links:
    i = i.get("href")
    if i!= None:
        if "https" not in i:
            i = url+i
        res  = requests.get(i)
        status = res.status_code
        if status == 404:
            print(i+"- page not found 404")
        else:
            file.write(i+' - Working  \n')
            file.flush()
file.close()



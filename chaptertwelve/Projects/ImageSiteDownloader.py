#! python3
# ImageSiteDownloader.py - Goes to Imagewebsite searches for a category of photos and then downloads top 10  images.
# Arguement 1 -> link (default imagur) , arguement 2 -> keyword

import requests,sys,bs4,os


os.makedirs("images", exist_ok=True)

def downloadimage(link):
    response = requests.get(link)
    response.raise_for_status()
    imgFile = open(os.path.join("images", os.path.basename(link)), 'wb')
    for chunk in response.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()


url= ''
if len(sys.argv) > 2:
    url = sys.argv[1]
    keyword = ''.join(sys.argv[2:])
    url += 'search?q='+str(keyword)
elif len(sys.argv) == 2:
    keyword = ''.join(sys.argv[1:])
    url = 'https://imgur.com/search?q='+keyword
else:
    print("Enter arguements properly. 1st argument -> url , 2nd arguement -> keyword")
    url = 'https://imgur.com/search?q=dogs'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
imageElem = soup.select('.image-list-link img')
if imageElem == []:
    print('Counldnt find any')
else:
    for i in imageElem:
        link = 'https:'+ i.get('src')
        downloadimage(link)

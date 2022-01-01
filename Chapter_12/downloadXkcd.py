#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Counldnt find any')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

    
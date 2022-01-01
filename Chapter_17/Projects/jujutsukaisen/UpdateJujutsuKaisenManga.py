#! python3
# UpdateJujutsuKaisenManga.py update jujutsi kaisen manga images every day to JK directory if new chapter is released.
# type this in crontab - 30 17 * * * <python3path> <filepath>
# cron format - minute hour day_of_month month day_of_week command_to_run
# reference  - https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804


import bs4,requests,os

def downloadimage(url,imageno):
    res = requests.get(url)
    res.raise_for_status()
    imageFile = open(os.path.join('JK', os.path.basename("Page-"+str(imageno))),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    print("Image - {} Downloaded".format(imageno))

file = open("chapterseventeen/Projects/jujutsukaisen/currentChapter")
read = file.read()
Lchapter = int(read)+1
file.close()

os.makedirs('JK', exist_ok=True)
url = "https://jujustukaisen.com/manga/jujutsu-kaisen-chapter-{}/".format(Lchapter)
response = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text,'html.parser')
links = soup.select('.article_ed__img')
Numimg = len(links)

if Numimg>1:
    imageno = 1
    for i in links:
        i = i.get("src")
        if i != None:
            downloadimage(i,imageno)
            imageno+=1
    file = open("chapterseventeen/Projects/jujutsukaisen/currentChapter",'w')
    file.write(str(Lchapter))
    print("New chapter Updated")
    file.close()
else:
    print("New chapter not available")


file = open("chapterseventeen/Projects/jujutsukaisen/currentChapter",'r')
read = file.read()
print("Current chapter is ",read)


# TODO-> ADD IMAGES TO WORLD DOCUMENT AND CREATE A PDF 

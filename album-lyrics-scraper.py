import requests
from bs4 import BeautifulSoup

#copy albums from the genuis.com artist page and paste in a text file, enter
#the name of the file in ".txt"

def replaceMultiple(mainString, toBeReplaces, newString):
    for elem in toBeReplaces :
        if elem in mainString :
            mainString = mainString.replace(elem, newString)
    return  mainString

songs = []
aes = ""

#place file name here

with open(".txt", encoding='utf-8') as file_in:
    lines = []
    for line in file_in:
        lines.append(replaceMultiple((replaceMultiple(line.strip(),['#','.',',','\'','?','!','/','’','(',')',':','|','-'],"")),' ',"-"))
    file_in.close()
for line in lines:
#change ARTIST-NAME with artist's name as typed in their genius artist page URL
    url = "https://genius.com/albums/ARTIST-NAME/"+line
    text = requests.get(url)
    soup = BeautifulSoup(text.content, 'lxml')
    data = soup.findAll('div',attrs={'class':'column_layout-column_span column_layout-column_span--primary'})
    for div in data:
        links = div.findAll('a')
        for a in links:
            songs.append(a['href'])

for song in songs:
    try:
        result = requests.get(song)
        soup = BeautifulSoup(result.content, 'lxml')
        aes+=soup.find("div", {"class": "lyrics"}).get_text()
        print(aes)
    except AttributeError:
        continue

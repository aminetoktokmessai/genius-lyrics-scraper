import requests
from bs4 import BeautifulSoup

#copy songs from the genuis.com artist page and paste in a text file, enter
#the name of the file in ".txt"

def replaceMultiple(mainString, toBeReplaces, newString):
    for elem in toBeReplaces :
        if elem in mainString :
            mainString = mainString.replace(elem, newString)
    return  mainString

lines2 = []
aes = ""

#place file name here

with open(".txt", encoding='utf-8') as file_in:
    lines = []
    for line in file_in:
        lines.append(line.strip())
file_in.close()
for line in lines:
    lines2.append(replaceMultiple((replaceMultiple(line,['.',',','\'','?','!','/','’','(',')',':','|','-'],"")),' ',"-"))
for line in lines2:
    try:
#change ARTIST-NAME with artist's name as typed in their genius artist page URL
        result = requests.get("https://genius.com/ARTIST-NAME-"+line+"-lyrics")
        soup = BeautifulSoup(result.content, 'lxml')
        aes+=soup.find("div", {"class": "lyrics"}).get_text()
        print(aes)
    except AttributeError:
        continue

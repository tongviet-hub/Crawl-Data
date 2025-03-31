import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text


soup = BeautifulSoup(content,'lxml') 

box = soup.find('article', class_= 'main-article')
title = box.find('h1').get_text()


transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
 
with open(f'Beautiful_Soup_Test/{title}.txt', 'w') as file: #title + '.txt'
    file.write(transcript)

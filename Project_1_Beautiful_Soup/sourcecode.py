
# Vì Quá Dài nên tôi Sẽ Chỉ Crawl 2 Trang thôi (Line 18)
import requests
from bs4 import BeautifulSoup

root = 'https://subslikescript.com'
website = f'{root}/movies'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content,'lxml') 

# Pagination
pagination = soup.find('ul', class_= 'pagination')
pages = pagination.find_all('li',class_ = 'page-item')
last_page = pages[-2].text

for page in range(1, int(last_page)+1)[:2]:
    #https://subslikescript.com/movies?page=1
    website = f'{root}/movies?page={page}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content,'lxml') 


    box = soup.find('article', class_= 'main-article')
    links = []
    for link in box.find_all('a', href =True):
        links.append(link['href'])
    for link in links:
        try:
            print(link)
            website = f'{root}/{link}'
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content,'lxml') 

            box = soup.find('article', class_= 'main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
            with open(f'Project_1_Beautiful_Soup/{title}.txt', 'w', encoding='utf-8') as file: 
                file.write(transcript)
        
        except:
            print("-----Link not working---------")
            print(link)
            pass
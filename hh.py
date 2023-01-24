import requests
from bs4 import BeautifulSoup 

def hh_scraper(text):
    data=[]
    for page in range(100):
        params = {'text': text, 'area':'113','per_page':'10', 'page':page}
        req = requests.get('https://api.hh.ru/vacancies', params=params)
        data = req.json(
        )
        for i in data['items']:
            with open('Отчет.txt', 'a+', encoding='utf-8') as f:
                f.write(f"Название: {i['name']}\nОжидаения работодателя: {i['snippet']['requirement']}\nОбязанности: {i['snippet']['responsibility']}\n\n\n")
            
        



hh_scraper('Информационаая безопастность')
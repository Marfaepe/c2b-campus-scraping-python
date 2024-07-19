import requests
import feedparser
from bs4 import BeautifulSoup

while True:
    feed = feedparser.parse('https://www.jotdown.es/feed/')

    link_list = []
    for i, entry in enumerate(feed.entries):
        href = entry.link
        title = entry.title
        link_list.append(href)
        print(f'{i}. {title}')
    while True:
        art_num = input('Puedes elegir un artículo para leer: ')
        try:
            art_num = int(art_num)
            url = link_list[art_num]
            break
        except:
            print('Introduce un número de la lista')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select_one('.entry-content')
    print(content.get_text())
    cont = input('Continuar (Y/n)>')

    if cont == 'n':
        break         
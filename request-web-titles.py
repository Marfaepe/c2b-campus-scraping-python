import requests
from bs4 import BeautifulSoup

url = 'https://www.jotdown.es/'

response = requests.get(url)

if response.status_code !=200:
    print(f'Error al obtener los títulos {response.status_code}')
    exit(1)

soup = BeautifulSoup(response.content, 'html.parser')
title_tags = soup.find_all('h3', class_ = 'entry-title')
    
    
titulos = []
       
for i, title_tag in enumerate(title_tags, start=1):
    titulo_texto = title_tag.get_text().strip()# strip = Elimina los espacio del inicio y del final
    enlace = title_tag.find('a')['href'] #busca la primera etiqueta <a> (enlace) dentro de la etiqueta <h3>.
                                             #obtiene el valor del atributo href de la etiqueta <a>, que es la URL a la que apunta el enlace.   
    titulos.append((i, titulo_texto, enlace))#append mete el elemento al final de la tupla
   

while True:

    for titulo in titulos:
            
        print(titulo)

    option = input('Introduce el número del artículo que quieres leer: ') 

    url_articulo = titulos[int(option)-1][2] 

    response = requests.get(url_articulo)

    if response.status_code !=200:
       print(f'Error al obtener los títulos {response.status_code}')
       exit(1)

    soup = BeautifulSoup(response.content, 'html.parser')

    noticia = soup.find(class_ = 'entry-content')

    print(noticia.get_text())
        




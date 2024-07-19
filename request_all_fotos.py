import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.jotdown.es/'
response = requests.get(url)

if response.status_code == 200:
    soup =  BeautifulSoup(response.content , 'html.parser')


    try:
        os.mkdir('downloads')

    except FileExistsError:
        print('El directorio ya existe,pero da igual')


    img_tags = soup.find_all('img')

    for i, img_tag in enumerate(img_tags, start=1):
        
        img_url = img_tag.get('src')

        if img_url:  # Asegurarse de que img_url no es None
            image_name = img_url.split('/')[-1]  # separa un string en partes dodne yo le diga
            img_response = requests.get(img_url)

            if img_response.status_code == 200:
                with open(f'downloads/{image_name}', 'wb') as file:
                    file.write(img_response.content)
                print(f'La foto {i} descargada')
            else:
                print(f'Error al descargar la foto {img_url}')
        else:
            print(f'La imagen {i} no tiene una URL válida')
else:
    print(f'Error al obtener la página {response.status_code}')
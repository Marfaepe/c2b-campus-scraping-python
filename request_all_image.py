import requests
from bs4 import BeautifulSoup

# URL de la página web que queremos analizar y descargar imágenes
url = 'https://www.jotdown.es/'

# Realizar la solicitud HTTP GET a la URL
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Crear un objeto BeautifulSoup con el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todas las etiquetas 'img' en el HTML
    img_tags = soup.find_all('img')
    
    # Carpeta donde se guardarán las imágenes descargadas
    carpeta_destino = 'todas_las_imagenes'
    
    # Descargar cada imagen encontrada
    for idx, img_tag in enumerate(img_tags, start=1):
        # Obtener la URL de la imagen
        img_url = img_tag.get('src')
            
        # Realizar la solicitud GET para descargar la imagen
        img_response = requests.get(img_url)
        
        # Verificar si la solicitud de la imagen fue exitosa
        if img_response.status_code == 200:
            # Guardar la imagen en un archivo local dentro de la carpeta destino
            with open(f'{carpeta_destino}/imagen{idx}.jpg', 'wb') as archivo:
                archivo.write(img_response.content)
            print(f'Imagen {idx} descargada')
        else:
            print(f'Error al descargar la imagen {img_url}')
else:
    print(f'Error al obtener la página {url}')

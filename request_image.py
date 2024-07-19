#Hacemos una petición a una web para descargar una imagen 
import requests


#Url de la imagen que queresmos descargar
url_imagen = 'https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png'


#nombre del archivo con el que queremos guardar la imagen
nombre_archivo = 'popopo.png'


#Realizar la solicitus GET para obtener la imagen
response = requests.get(url_imagen)


#verifica si la solicitud fue exitosa

if response.status_code == 200:
    with open(nombre_archivo, 'wb')as file:
        file.write(response.content)
    print(f'Imagen descargada y guardada como {nombre_archivo}')
else:
    print(f'Error al descargar la imagen: {response.status_code }')        



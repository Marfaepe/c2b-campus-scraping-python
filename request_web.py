import requests

# Definimos la URL de la página web
url = 'https://elenq.tech/es/'

# Realizamos la solicitud HTTP GET a la URL
response = requests.get(url)

# Verificamos si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Obtenemos el contenido HTML de la respuesta
    contenido_html = response.text
    
    # Imprimimos una porción del contenido HTML (en este caso, los primeros 500 caracteres)
    print(contenido_html)
else:
    # Si la solicitud no fue exitosa, mostramos un mensaje de error
    print(f'Error al obtener la página: {response.status_code}')


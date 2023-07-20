import requests
from bs4 import BeautifulSoup

# Definir la URL de la página web
url = "https://www.example.com"

# Enviar una solicitud GET a la URL
response = requests.get(url)

# Crear un objeto BeautifulSoup con el contenido de la respuesta
soup = BeautifulSoup(response.content, "html.parser")

# Imprimir el HTML completo de la página
print(soup.prettify())

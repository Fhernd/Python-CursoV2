import requests
from bs4 import BeautifulSoup


def consultar_url(url):
    """
    Función que consulta una URL y devuelve el contenido de la respuesta.

    :param url: URL a consultar.
    :return: Contenido de la respuesta.
    """
    response = requests.get(url)
    
    return response.content

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


def crear_objeto_beautifulsoup(html):
    """
    Función que crea un objeto BeautifulSoup a partir de un HTML.

    :param html: HTML.
    :return: Objeto BeautifulSoup.
    """
    return BeautifulSoup(html, "html.parser")


def tiene_tablas_html(soup):
    """
    Función que verifica si un objeto BeautifulSoup tiene tablas HTML.

    :param soup: Objeto BeautifulSoup.
    :return: True si tiene tablas HTML, False en caso contrario.
    """
    return len(soup.find_all("table")) > 0


def contar_tablas_html(soup):
    """
    Función que cuenta las tablas HTML de un objeto BeautifulSoup.

    :param soup: Objeto BeautifulSoup.
    :return: Número de tablas HTML.
    """
    return len(soup.find_all("table"))

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


def extraer_tabla(soup, indice_tabla):
    """
    Función que extrae el contenido de una tabla HTML de un objeto BeautifulSoup.

    :param soup: Objeto BeautifulSoup.
    :param indice_tabla: Índice de la tabla HTML.
    :return: Contenido de la tabla HTML.
    """
    return soup.find_all("table")[indice_tabla]


def extraer_contenido_tabla(tabla):
    """
    Función que extrae el contenido de una tabla HTML.

    :param tabla: Tabla HTML.
    :return: Contenido de la tabla HTML.
    """
    contenido = []

    for fila in tabla.find_all("tr"):
        fila_contenido = []

        for columna in fila.find_all(["th", "td"]):
            fila_contenido.append(columna.text.strip())

        contenido.append(fila_contenido)

    return contenido


def prueba():
    url = 'https://www.htmlquick.com/es/tutorials/tables.html'

    html = consultar_url(url)

    soup = crear_objeto_beautifulsoup(html)

    # print(soup.prettify())

    print(tiene_tablas_html(soup))

    print(contar_tablas_html(soup))

    indice = 0

    tabla = extraer_tabla(soup, indice)

    print(type(tabla))


if __name__ == '__main__':
    prueba()

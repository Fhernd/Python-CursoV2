import csv
import re

from bs4 import BeautifulSoup
import requests

import flet as ft


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


def crear_csv(contenido, nombre_archivo):
    """
    Función que crea un archivo CSV a partir de un contenido.

    :param contenido: Contenido.
    :param nombre_archivo: Nombre del archivo.
    """
    with open(nombre_archivo, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contenido)


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

    contenido = extraer_contenido_tabla(tabla)
    print(contenido)

    nombre_archivo = 'tabla.csv'

    crear_csv(contenido, nombre_archivo)


def validate_url(url):
    """
    Esta función valida si la cadena de entrada es una URL válida.

    :param url: URL a validar.
    :return: True si es una URL válida, False en caso contrario.
    """
    regex = re.compile(
        r'http[s]?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, url) is not None


def main(page: ft.Page):
    page.title = "Extractor de CSV desde HTML"
    # Tamaño de la ventana:
    page.size = (400, 600)

    soup = None

    def on_click_extraer_datos(event):
        opcion_tabla = cbx_tablas.value

        if opcion_tabla is None:
            dlg_modal.content = ft.Text('Debe seleccionar una tabla')
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return

        indice_tabla = int(cbx_tablas.value)

        tabla = extraer_tabla(soup, indice_tabla)

        # contenido = extraer_contenido_tabla(tabla)

        # nombre_archivo = 'tabla.csv'

        # crear_csv(contenido, nombre_archivo)

        # dlg_modal.content = ft.Text('Se ha creado el archivo CSV')
        # page.dialog = dlg_modal
        # dlg_modal.open = True
        # page.update()

    btn_extraer_datos = ft.FilledButton("Extraer datos...", on_click=on_click_extraer_datos, disabled=True)

    def close_dialog(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Mensaje"),
        content=ft.Text(''),
        actions=[
            ft.TextButton("OK", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def on_click_consultar(event):
        url = txt_url.value

        btn_extraer_datos.disabled = True
        cbx_tablas.disabled = True
        
        if url == '':
            dlg_modal.content = ft.Text('Debe ingresar una URL. El campo no puede quedar vacío')
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return
        
        if not validate_url(url):
            dlg_modal.content = ft.Text('Debe ingresar una URL válida. Por ejemplo: https://ortizol.blogspot.com')
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return
        
        html = consultar_url(url)

        soup = crear_objeto_beautifulsoup(html)

        if not tiene_tablas_html(soup):
            dlg_modal.content = ft.Text('La URL no tiene tablas HTML')
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
            return
        
        contador_tablas = contar_tablas_html(soup)

        opciones_tablas = [ft.dropdown.Option(str(i)) for i in range(1, contador_tablas + 1)]

        cbx_tablas.options = opciones_tablas

        cbx_tablas.disabled = False
        btn_extraer_datos.disabled = False

        page.update()

    txt_url = ft.TextField()

    contenedor_1 = ft.ResponsiveRow([
        ft.Container(
            ft.Text("URL:", size=25),
            padding=15,
            col={"sm": 2, "md": 1, "xl": 1},
        ),
        ft.Container(
            txt_url,
            padding=5,
            col={"sm": 8, "md": 9, "xl": 8},
        ),
        ft.Container(
            ft.FilledButton("Consultar...", on_click=on_click_consultar),
            padding=12,
            col={"sm": 2, "md": 2, "xl": 2},
        )
        ],
    )

    cbx_tablas = ft.Dropdown(
        width=100,
        options=[],
        disabled=True,
    )

    contenedor_2 = ft.ResponsiveRow([
        ft.Container(
            ft.Text("Tabla:", size=25),
            padding=15,
            col={"sm": 2, "md": 1, "xl": 1},
        ),
        ft.Container(
            cbx_tablas,
            padding=5,
            col={"sm": 8, "md": 9, "xl": 8},
        ),
        ft.Container(
            btn_extraer_datos,
            padding=12,
            col={"sm": 2, "md": 2, "xl": 2},
        )
        ],
    )

    page.add(
        contenedor_1
    )
    page.add(
        contenedor_2
    )


if __name__ == '__main__':
    ft.app(target=main)

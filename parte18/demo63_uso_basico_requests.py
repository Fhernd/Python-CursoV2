import requests

url = 'https://randomuser.me/api?format=json'

try:
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print('Código de respuesta:', respuesta.status_code)
        
        print()

        print('Contenido como cadena de bytes:')
        print(type(respuesta.content))
        print(respuesta.content)

        print()
        print('Contenido en formato texto (str):')
        print(type(respuesta.text))
        print(respuesta.text)

        print()

        print('Contenido en formato JSON:')
        contenido_json = respuesta.json()
        print(type(contenido_json))
        print(contenido_json)

        print()

        print('Contenido de results:')
        print(type(contenido_json['results'])) # <class 'list'>
        print(contenido_json['results'])
        print(contenido_json['results'][0]['gender']) # ~
        print(contenido_json['results'][0]['name']['first']) # ~

        print()
    else:
        print('No se ha encontrado el recurso.')
except:
    print('La URL no existe')

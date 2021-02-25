import requests

url = 'https://randomuser.me/api?format=docx'

try:
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        print('Código de respuesta:', respuesta.status_code)
        
        print()

        print('Contenido:')
        print(type(respuesta.content))
        print(respuesta.content)

        print()
        print('Contenido:')
        print(type(respuesta.text))
        print(respuesta.text)
    else:
        print('No se ha encontrado el recurso.')
except:
    print('La URL no existe')

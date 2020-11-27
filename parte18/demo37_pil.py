from PIL import Image

img_logo_python = Image.open('parte18/demo35_python_logo.png')
print(img_logo_python.format, img_logo_python.size, img_logo_python.mode)

print()

img_logo_python = Image.open('parte18/demo35_python_logo.jpg')
print(img_logo_python.format, img_logo_python.size, img_logo_python.mode)

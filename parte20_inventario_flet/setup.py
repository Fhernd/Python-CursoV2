from setuptools import setup

setup(name='inventario', version='1.0.0', packages=['inventario'],
entry_points= {
    'console_scripts': ['inventario = inventario.__main__:main']
})

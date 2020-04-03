from setuptools import setup

setup(name='calculadora', version='1.0.0', packages=['calculadora'], 
entry_points= {
    'console_scripts': ['calculadora = calculadora.__main__:main']
})

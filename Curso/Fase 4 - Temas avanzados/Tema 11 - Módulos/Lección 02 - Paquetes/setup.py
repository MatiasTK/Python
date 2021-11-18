#Este archivo sirve para crear UN PAQUETE DISTRIBUIBLE -> esta instalado para usarlo cuando quieras
from setuptools import setup

setup(
    name = "paquete",
    version = "0.1",
    description = "Este es un paquete de ejemplo",
    author = "Matias Vallejos",
    author_email = "matiavallejo@gmail.com",
    url = "http://google.com",
    # scripts = ["script.py"]
    packages = ["paquete","paquete.adios","paquete.hola"] # Se introduce el paquete y los subpaquetes
)
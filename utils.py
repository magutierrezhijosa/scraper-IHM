# Importamos libreria de Python para crear y escribir ficheros CSV
import csv

# Importamos la funciones :
# 1."urljoin" para combinar URLs (Convierte enlaces relativos en  absolutos)
# 2. "urlparse" funcion para desmontar un URL en sus partes:  dominio,ruta,protocolo
from urllib.parse import urljoin, urlparse

# Importamos la constantes del archivo config.py
from config import OUTPUT_CSV,CSV_FIELDNAMES

# Declaramos la funcion que se va a encargar de asegurarnos que todos lo enlaces sean absolutos 
# 1. Si el enlace es absoluto -> lo devuelve tal cual
# 2. Si el enlace es relativo -> lo combina con la base_url para construir la URL completa
def  build_absolute_url(href: str, base_url: str) -> str:
    return urljoin(base_url,href)


# Declaramos la funcion que se  encarga de desmontar la URL  y nos quedamos solo con la ruta 
def is_direct_pdf(url: str) -> bool:
    path = urlparse(url).path
    return path.lower().endswith('.pdf')


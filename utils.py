# Importamos libreria de Python para crear y escribir ficheros CSV
import csv

# Importamos la funciones :
# 1."urljoin" para combinar URLs (Convierte enlaces relativos en  absolutos)
# 2. "urlparse" funcion para desmontar un URL een sus partes:  dominio,ruta,protocolo
from urllib.parse import urljoin, urlparse

# Importamos la constantes del archivo config.py
from config import OUTPUT_CSV,CSV_FIELDNAMES



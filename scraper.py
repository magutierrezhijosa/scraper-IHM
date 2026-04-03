# Importamos libreria de Python para manejar tiempos
import time
# Libreria que importamos parta hacer peticiones HTTP
import requests
# Libreria para parsear el HTML que nos devuelva el requests
from bs4 import BeautifulSoup
# Importamos CONSTANTES del confi..py
from config import HEADERS,REQUEST_DELAY, REQUEST_TIMEOUT



# Definimos la funcion que recibe una url que debe ser string
def fetch_page(url:str) -> BeautifulSoup | None:

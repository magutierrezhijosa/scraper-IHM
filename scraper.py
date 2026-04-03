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

    # Iniciamos un try para que si falla el codigo vaya al except
    try:
        # Realizamos la peticion de HTTP real 
        response  = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)

        # Comprobamos si el servidor respondio y si hay unn error lo manda al except
        response.raise_for_status()

        # Pasamos a BeautifulSoup el response.txt y lo parseamos para interpretar ese HTML
        return BeautifulSoup(response.text, "html.parser")

    # EXCEPCIONES

    # Si el servidor tardo mas de 15 segundos en responder
    except requests.exceptions.Timeout:
        # Mostramos un aviso y devolvemos None
        print(f"  [!] Timeout al obtener: {url}")
        return None
    
    # Si el servidor respondio con un error HTTP 
    except requests.exceptions.HTTPError as e:
        print(f"  [!] Error HTTP {e.response.status_code} en: {url}")
        return None
    
    # Capturamos cualquier otro error que no hayamos previsto antes
    except requests.exceptions.RequestException as e : 
        print(f"  [!] Error de conexión en {url}: {e}")
        return None
    

# Funcion para pausar la ejecucion del programa 
def polite_delay() -> None:
    # Es la funcion de Python para "Dormir" el programa durante los segunndos que le indiques
    time.sleep(REQUEST_DELAY)
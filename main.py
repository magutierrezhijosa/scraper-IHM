# IMPORTS

from urllib.parse import urlparse
from scraper import fetch_page, polite_delay
from parser import extract_publications, extract_pdf_from_secondary_page
from utils import save_to_csv
from config  import PUBLICATIONS_URL, OUTPUT_CSV


# Defiinimos la funcion principal del programa que se encarga de coordinar todo el proceso de scraping y extracción de datos
def main():

    # Imprime un mensaje indicando que el proceso de scraping ha comenzado
    print("=" * 60)
    print(" IHM Publicaciones Scraper ")
    print(f" URL de origen: {PUBLICATIONS_URL}")
    print("=" * 60)

    # Paso 1: Obtener el contenido HTML de la página de publicaciones utilizando la función fetch_page
    print("\n[1/3] Descargando página principal...")

    # Llama a la funcion del scraper.py para obtener el contenido HTML de la página de publicaciones y lo almacena en la variable main_soup
    main_soup = fetch_page(PUBLICATIONS_URL)

    # Si no se pudo obtener el contenido HTML de la página principal, imprime un mensaje de error y termina la ejecución del programa
    if not main_soup:
        print("[✗] No se pudo obtener la página principal. Abortando.")
        return
    
    print("  → Página descargada correctamente.")
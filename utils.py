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

# Declaramos la funcion extrae el dominio de una URL dada y lo compara con la lista de dominios externos permitidos
def is_external_link(url: str, external_domains: list) -> bool:
    # Extrae el dominio de la URL si es None devuelve una cadena vacia
    hostname = urlparse(url).hostname or ""
    # Compara el dominio extraido con la lista de dominios externos permitidos
    return any(domain in hostname for domain in external_domains)

# Declaramos la funcion que se encarga de guardar los datos extraidos en un archivo CSV
# Recibe una lista de diccionarios (cada diccionario sera una fila en el CSV con las claves titulo, pdf_url)
# Recibe el nombre del fichero CSV donde se guardaran los datos
def save_to_csv(records: list[dict], filename: str = OUTPUT_CSV) -> None:
    # Abre el archivo CSV en modo escritura y crea un objeto writer para escribir en el archivo
    with open(filename, mode = 'w', newline='', encoding='utf-8') as f:
        # Escritor de CSV que utiliza las claves del diccionario como nombres de columna en el archivo CSV
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDNAMES)
        # Escribe la fila de encabezado en el archivo CSV
        writer.writeheader()
        # Escribe cada registro (diccionario) como una fila en el archivo CSV
        writer.writerows(records)
    print(f"\n[✓] Guardados {len(records)} registros en '{filename}'")

    
    
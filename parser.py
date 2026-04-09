# IMPORTS 
from bs4 import BeautifulSoup
from utils import build_absolute_url, is_direct_pdf, is_external_link
from config import EXTERNAL_DOMAINS, BASE_URL

# Definimos la funcion qque se encarga de analizar el contenido HTML de la pagina web y extrae los datos relevantes (titulo y URL del PDF)
def extract_publications(soup: BeautifulSoup) -> list[dict]:
    # Lista vacio donde iremos acumulando los datos extraidos
    publications = []

    # Buscamos todos los elementos <a> que tengan un href
    cards = soup.find_all('a', href=True)

    # Iteramos sobre cada elemento encontrado
    for card in cards:

        # Dentro de cada elemento <a>, buscamos un elemento <h3 class="title"> para extraer el titulo de la publicacion     
        title_tag = card.find('h3', class_='title')
        
        # Si no se encuentra el elemento <h3 class="title">, se omite esta iteracion y se pasa al siguiente elemento <a>    
        if not title_tag:
            continue

        # Extraemos el texto del titulo y eliminamos espacios en blanco al inicio y al final
        titulo = title_tag.get_text(strip=True)

        # Obtenemos el valor del atributo href del elemento <a> y lo convertimos en una URL absoluta utilizando la función build_absolute_url
        href = card['href']
        absolute_url = build_absolute_url(href, BASE_URL)

        # Agregamos un diccionario con el titulo, la URL absoluta, y las banderas que indican si es un enlace directo a un PDF o si es un enlace externo a la lista de publicaciones
        publications.append({
            "titulo": titulo,
            "link": absolute_url,
            "is_pdf": is_direct_pdf(absolute_url),
            "is_external": is_external_link(absolute_url, EXTERNAL_DOMAINS),
        })

    return publications

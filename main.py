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

    # ------------------------------------------------------------------
    # PASO 1: Descargar la página principal
    #   Obtener el contenido HTML de la página de publicaciones utilizando la función         #   fetch_page
    # ------------------------------------------------------------------
    
    print("\n[1/3] Descargando página principal...")

    # Llama a la funcion del scraper.py para obtener el contenido HTML de la página de publicaciones y lo almacena en la variable main_soup
    main_soup = fetch_page(PUBLICATIONS_URL)

    # Si no se pudo obtener el contenido HTML de la página principal, imprime un mensaje de error y termina la ejecución del programa
    if not main_soup:
        print("[✗] No se pudo obtener la página principal. Abortando.")
        return
    
    print("  → Página descargada correctamente.")

    # ------------------------------------------------------------------
    # PASO 2: Extraer las tarjetas de publicaciones
    # ------------------------------------------------------------------

    print("\n[2/3] Extrayendo publicaciones...")

    # Llama a la función extract_publications del parser.py para analizar el contenido HTML de la página principal y extraer los datos relevantes (titulo, URL del PDF, etc.) de cada publicación. Almacena los resultados en la variable publications
    publications = extract_publications(main_soup)

    if not publications:
        print("[✗] No se encontraron publicaciones. Abortando.")
        return
    
    direct_count = sum(1 for pub in publications if pub['is_pdf'])
    external_count = sum(1 for pub in publications if pub['is_external'])

    print(f"  → {len(publications)} publicaciones encontradas:")
    print(f"     • {direct_count} con enlace directo a PDF")
    print(f"     • {external_count} con página secundaria externa")

    # ------------------------------------------------------------------
    # PASO 3: Manejar enlaces a páginas secundarias y extraer PDFs        
    # ------------------------------------------------------------------

    # PASO 3: Resolver las URLs de los PDFs
    print("\n[3/3] Resolviendo URLs de PDFs...")
    records = []

    for i, pub in enumerate(publications, start=1):
        titulo = pub["titulo"]
        link = pub["link"]

        print(f"\n  [{i}/{len(publications)}] {titulo[:70]}{'...' if len(titulo) > 70 else ''}")

        if pub["is_pdf"]:
            print(f"    → PDF directo: {link}")
            records.append({"titulo": titulo, "pdf_url": link})

        elif pub["is_external"]:
            print(f"    → Página externa, navegando a: {link}")
            polite_delay()

            secondary_soup = fetch_page(link)

            if secondary_soup:
                parsed = urlparse(link)
                external_base = f"{parsed.scheme}://{parsed.netloc}"

                pdf_url = extract_pdf_from_secondary_page(secondary_soup, external_base)

                if pdf_url:
                    print(f"    → PDF encontrado: {pdf_url}")
                    records.append({"titulo": titulo, "pdf_url": pdf_url})
                else:
                    print(f"    → ⚠ PDF no encontrado. Guardando URL de la página.")
                    records.append({"titulo": titulo, "pdf_url": link})
            else:
                print(f"    → ✗ Error al acceder a la página secundaria.")
                records.append({"titulo": titulo, "pdf_url": "ERROR_AL_ACCEDER"})

        else:
            print(f"    → ⚠ Tipo desconocido, guardando URL tal cual.")
            records.append({"titulo": titulo, "pdf_url": link})


    # PASO 4: Guardar los datos en el CSV
    save_to_csv(records, OUTPUT_CSV)
    print("\n✅ ¡Proceso completado con éxito!")
    print(f"   Revisa el fichero: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()    
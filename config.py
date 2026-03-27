
# Declaracion de las constantes que vamos a usar en el proyecto

# --- URLs que vamos a usar ---
BASE_URL = "https://www.ihm.pt"

PUBLICATIONS_URL = "https://www.ihm.pt/pt/atualidade/publicacoes"

# --- Dominios externos ---
EXTERNAL_DOMAINS = ["madeira.gov.pt"]

# --- Salida ---
OUTPUT_CSV = "publicacoes.csv"
CSV_FIELDNAMES = ["titulo", "pdf_url"]

# --- Comportamiento HTTP ---
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-PT,pt;q=0.9,en;q=0.8",
}


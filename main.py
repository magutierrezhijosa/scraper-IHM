# IMPORTS

from urllib.parse import urlparse
from scraper import fetch_page, polite_delay
from parser import extract_publications, extract_pdf_from_secondary_page
from utils import save_to_csv
from config  import PUBLICATIONS_URL, OUTPUT_CSV



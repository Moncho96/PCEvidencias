import argparse
from scrapingAndMeta import Scraping

parser = argparse.ArgumentParser(description='Extrae imagenes y muestra sus metadatos')
parser.add_argument('-link', '--url',type=str, help='URL del sitio web donde se extraeran las imagenes')
args = parser.parse_args()

if __name__ == "__main__":
    scraping = Scraping()
    scraping.scrapingImages(args.url)


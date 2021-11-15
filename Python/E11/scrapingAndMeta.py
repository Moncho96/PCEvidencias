# -*- encoding: utf-8 -*-

import os
from typing import get_origin

import requests
from lxml import html
from bs4 import BeautifulSoup

from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image

def decode_gps_info(exif):
        gpsinfo = {}
        if 'GPSInfo' in exif:
            #Parse geo references.
            Nsec = exif['GPSInfo'][2][2] 
            Nmin = exif['GPSInfo'][2][1]
            Ndeg = exif['GPSInfo'][2][0]
            Wsec = exif['GPSInfo'][4][2]
            Wmin = exif['GPSInfo'][4][1]
            Wdeg = exif['GPSInfo'][4][0]
            if exif['GPSInfo'][1] == 'N':
                Nmult = 1
            else:
                Nmult = -1
            if exif['GPSInfo'][3] == 'E':
                Wmult = 1
            else:
                Wmult = -1
            Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
            Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
            exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
            input()
    
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
        
def printMeta():
    ruta = input("Ruta de imágenes: ")
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("[+] Metadata for file: %s " %(name))
            input()
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    archivo = open(name + ".txt","w") #A;adido
                    archivo.write (str(exif)) #a;adido
                    archivo.close() #A;adido
                    #print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                print ("\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

class Scraping:

    def scrapingImages(self,url):
            print("\nObteniendo imagenes de la url:"+ url)
        
            try:
                response = requests.get(url)  
                parsed_body = html.fromstring(response.text)

                # expresion regular para obtener imagenes
                images = parsed_body.xpath('//img/@src')

                print ('Imagenes %s encontradas' % len(images))
        
                #create directory for save images
                os.system("mkdir images")
        
                for image in images:
                    if image.startswith("http") == False:
                        download = url + image
                    else:
                        download = image
                    print(download)
                    # download images in images directory
                    r = requests.get(download)
                    f = open('images/%s' % download.split('/')[-1], 'wb')
                    f.write(r.content)
                    f.close()
                printMeta()
                    
            except Exception as e:
                    print(e)
                    print ("Error conexion con " + url)
                    pass
    
import argparse

parser = argparse.ArgumentParser(description='Extrae imagenes y muestra sus metadatos')
parser.add_argument('-link', '--url',type=str, help='URL del sitio web donde se extraeran las imagenes')
args = parser.parse_args()

if __name__ == "__main__":
    scraping = Scraping()
    scraping.scrapingImages(args.url)
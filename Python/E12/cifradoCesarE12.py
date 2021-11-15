# -*- encoding: utf-8 -*-

import argparse
import detectSpanish

parser = argparse.ArgumentParser(description='Encripta, desencripta y crackea mensajes')
parser.add_argument('-e',dest="encode",type=str, help='Encripta un mensaje dada una clave')
parser.add_argument('-d',dest="decode",type=str, help='Desencripta un mensaje dada una clave')
parser.add_argument('-c',dest="crack",type=str, help='Crackear un mensaje cifrado, analizando si es o no un mensaje valido en español')
args = parser.parse_args()

def encriptar(clave):
    message = args.encode
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key

            print(translatedIndex)
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("Se ha encriptado con exito: ",translated)

def desencriptar(clave):
    message = args.decode
    espacios = 1
    while espacios > 0:
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            print(translatedIndex)
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol

    print("Se ha desencriptado con exito: ",translated)

def crack():
    message = args.crack
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        claves = []
        translated = ''

        # The rest of the program is almost the same as the original program:

        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol
        claves.append(translated)
        for clave in claves:
            if detectSpanish.isSpanish(clave):
                print('Traduccion:',clave)

if __name__ == '__main__':
    if args.encode != None:
        encriptar(args.encode)
    if args.decode != None:    
        desencriptar(args.decode)
    if args.crack != None:
        crack()
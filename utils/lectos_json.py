import json

def leer_json(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return json.load(archivo) # Esto devolverá la lista de diccionarios
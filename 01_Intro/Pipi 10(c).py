import csv

# Diccionario para contar los árboles por nombre común y guardar sus coordenadas
conteo_arboles = {}
coordenadas = {}

with open('arbolado-en-espacios-verdes.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Contamos los árboles y guardamos sus coordenadas
    for row in reader:
        nombre = row['nombre_com']
        latitud = row['lat']
        longitud = row['long']
        
        if nombre in conteo_arboles:
            conteo_arboles[nombre] += 1
        else:
            conteo_arboles[nombre] = 1
            coordenadas[nombre] = (latitud, longitud)

# Filtramos los árboles únicos
arboles_unicos = {nombre: coordenadas[nombre] for nombre, cantidad in conteo_arboles.items() if cantidad == 1}

# Mostramos los resultados
if arboles_unicos:
    print("Los árboles únicos encontrados en CABA son:")
    for nombre, (lat, long) in arboles_unicos.items():
        link = f"https://www.google.com/maps?q={lat},{long}"
        print(f"- {nombre}: {link}")
else:
    print("No se encontraron árboles únicos.")
import csv

archivo_csv = 'arbolado-en-espacios-verdes.csv'

suma_diametros = 0
cantidad_ceibos = 0

with open(archivo_csv, newline='', encoding='utf-8') as csvfile: #encoding='utf-8' se usa para caracteres especiales en el archivo
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['nombre_com'] == 'Ceibo':  # Verificamos si el árbol es un "Ceibo"
            suma_diametros += float(row['diametro'])  # Sumamos el diámetro
            cantidad_ceibos += 1  

# Calculamos el promedio
if cantidad_ceibos > 0:
    promedio_diametro = suma_diametros / cantidad_ceibos
    print(f"El promedio de diámetro de los árboles Ceibo es: {promedio_diametro:.2f}")
else:
    print("No se encontraron árboles con el nombre Ceibo.")

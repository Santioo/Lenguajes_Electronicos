import csv

origen = {}

with open ('arbolado-en-espacios-verdes.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader, None)

    for row in spamreader:
        nombre = row[7]
        if nombre in origen:
            origen[nombre] = origen[nombre] + 1
        else:
            origen[nombre] = 1
    #print(origen) 
    
ordenado = sorted(origen.items(), key=lambda x:x[1], reverse=True)

print(ordenado)
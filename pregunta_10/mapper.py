#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

# Guardar el contenido del archivo en una variable.
infile = sys.stdin

# Itera sobre cada linea del archivo recibido a través del flujo de entrada.
for row in infile:

    # Generar una lista de cada una de las columnas de la fila.
    columns = row.split('\t')
    
    # Seleccionar la primera columna como valor.
    value = columns[0]
    
    # Seleccionar los elementos de la segunda columna como claves.
    for key in columns[1].split('\r')[0].split(','):
        
        # Imprimir la "clave,valor" por cada elemento de la segunda columna.
        sys.stdout.write(key + ',' + value + '\n')

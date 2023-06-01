#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

# Guardar el contenido del archivo en una variable.
infile = sys.stdin

# Itera sobre cada linea del archivo recibido a través del flujo de entrada.
for row in infile:

    # Generar una lista de cada una de las columnas de la fila.
    columns = row.split(',')
    
    # Seleccionar la primera columna como clave.
    key = columns[0]
    # Seleccionar la segunda columna como valor.
    value = columns[1].split('\n')[0]

    # Imprimir la "clave,valor".
    sys.stdout.write(key + "," + value + "\n")

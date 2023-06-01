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
    
    # Seleccionar la columna "purpose" como clave.
    key = columns[3]
    # Seleccionar la columna "amount" como valor.
    value = columns[4]

    # Imprimir la "clave,valor".
    sys.stdout.write(key + "," + value + "\n")

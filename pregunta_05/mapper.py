#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

# Guardar el contenido del archivo en una variable.
infile = sys.stdin

# Itera sobre cada linea del archivo recibido a través del flujo de entrada.
for row in infile:

    # Generar una lista de cada una de las columnas de la fila.
    columns = row.split('   ')
    
    # Seleccionar el mes de los valores de la segunda columna como clave.
    key = columns[1].split('-')[1]

    # Imprimir la "clave,valor".
    sys.stdout.write(key + ',1' + '\n')

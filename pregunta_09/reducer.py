#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

# Guardar el contenido del archivo en una variable.
infile = sys.stdin

# Guardar todas las claves y sus coincidencias en una lista.
keys_list = []

# Iterar sobre cada clave.
for row in infile:

    key, value = row.split(',')
    value = int(value)
    
    # Actualizar la lista con la clave y el valor.
    keys_list.append([key, value])

# Ordenar la lista por clave de menor a mayor.
keys_list.sort(key=lambda x: x[1])
# Obtener sólo los seis primeros elementos de la lista.
keys_list = keys_list[:6]

# Obtener el resultado.
for key_ans, value_ans in keys_list:
    sys.stdout.write(key_ans + '   ' + str(value_ans) + '\n')

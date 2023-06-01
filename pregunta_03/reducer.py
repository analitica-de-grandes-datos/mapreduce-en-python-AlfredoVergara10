#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

# Guardar el contenido del archivo en una variable.
infile = sys.stdin

# Guardar todas las claves y sus coincidencias en un diccionario.
keys_dict = {}

# Iterar sobre cada clave.
for row in infile:

    key, value = row.split(',')
    value = int(value)
    
    # Actualizar el diccionario con la "clave,valor" recibida.
    keys_dict.update({key: value})

# Iterar sobre el diccionario y obtener el resultado ordenado por claves de mayor a menor.
for key_ans, value_ans in sorted(keys_dict.items(), key=lambda item: item[1]):
    sys.stdout.write(key_ans + ',' + str(value_ans) + '\n')

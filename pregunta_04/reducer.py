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
    
    # Si la clave ya ha sido reconocida, sumar el valor, sino, actualizar el diccionario.
    if key in keys_dict:
        keys_dict[key] = keys_dict[key] + value
    else:
        keys_dict.update({key: value})

# Iterar sobre el diccionario y obtener el resultado.
for key_ans, value_ans in sorted(keys_dict.items()):
    sys.stdout.write(key_ans + ',' + str(value_ans) + '\n')

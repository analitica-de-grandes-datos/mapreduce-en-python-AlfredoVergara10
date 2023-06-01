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
    value = float(value)
    
    # Si la clave ya ha sido reconocida, sumar el valor y el número de coincidencias, sino, actualizar el diccionario.
    if key in keys_dict:
        keys_dict[key] = [keys_dict[key][0] + value, keys_dict[key][1] + 1]
    else:
        keys_dict.update({key: [value, 1]})

# Iterar sobre el diccionario y obtener el resultado.
for key_ans, value_ans in sorted(keys_dict.items()):
    sys.stdout.write(key_ans + '\t' + str(value_ans[0]) + '\t' + str(value_ans[0]/value_ans[1]) + '\n')

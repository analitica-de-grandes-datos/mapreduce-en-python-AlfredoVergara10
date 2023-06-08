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

    key, value = row.split('\t')
    value = int(value)
    
    # Si la clave ya ha sido reconocida, añadir la clave a la lista de claves, sino, actualizar el diccionario.
    if key in keys_dict:
        keys_dict[key].append(value)
    else:
        keys_dict.update({key: [value]})

# Iterar sobre el diccionario y obtener el resultado.
for key_ans, value_ans in sorted(keys_dict.items()):
    
    # Ordenar las claves de mayor a menor.
    value_ans.sort()
    # Obtener una cadena de caracteres a partir de la lista de claves.
    value_ans = ','.join(map(str, value_ans))

    # Imprimir el resultado.
    sys.stdout.write(key_ans + '\t' + value_ans + '\n')

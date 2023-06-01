#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

# Guardar el contenido del archivo en una variable.
infile = sys.stdin
# Guardar todas las claves únicas (letra de la primera columna).
unique = []
# Guardar todas las claves y valores en un diccionario.
keys_dict = {}

# Iterar sobre cada clave.
for row in infile:
    
    key, value = row.split(',')
    value = int(value)
    
    # Si la clave única no existe en la lista, añadirla.
    if key.split('   ')[0] not in unique:
        unique.append(key.split('   ')[0])
    
    # Añadir la clave y valor al diccionario.
    keys_dict.update({key: value})

# Ordenar la lista única de claves.
unique.sort()

# Iterar sobre el diccionario y obtener el resultado.
for letter in unique:

    # Guardar todas las claves por agrupar en un diccionario a parte.
    keys_dict_group = {}
    
    # Recorrer el diccionario general de claves y valores
    for key_value in keys_dict:
        
        # Obtener la clave y el valor específico.
        key = key_value
        value = keys_dict[key_value]
        value = int(value)
        
        # Si la clave coincide con la clave por la que se agrupa, añadir la clave y valor al grupo
        if key.split('   ')[0] == letter:
            keys_dict_group.update({key: value})

    # Imprimir el resultado por grupos ordenando por valores.
    for key_ans, value_ans in sorted(keys_dict_group.items(), key=lambda item: item[1]):

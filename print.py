# Ejemplos de la fucnión print()

print('Hola mundo')
print('Hola mundo', 'otra vez')
print('Son las', 9, 'de la mañana')

print('El resultado de 3 * 4 es:', 3*4)

# Ejemplos de cadenas formateadas
print('El número 15 en sistema decimal es %d, en sistema octal es %o, en sistema hexadecimal es %x' % (15, 15, 15))

pi = 3.141592
r = 5
print(f'El radio de un círculo es {r} y el área de ese círculo es {pi * r ** 2 : .2f}')

# Impresión de caracteres espaciales
print('la letra beta es: \n\t \u03b2')

# Caracteres de escape
print('Hola mundo', end = ' ')
print('otra vez', end = '\t')
print('y otra vez')
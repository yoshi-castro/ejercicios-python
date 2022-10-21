numHuevos = 12
# print('Tengo ' + numHuevos  + ' huevos.')

# Opción 1
print('Tengo ' + str(numHuevos) + ' huevos.')

# Opción 2
print('Tengo %s huevos.' %(numHuevos))

# Calcular la superficie o área de un cuadrado
lado = int(input('Ingrese la medida del lado del cuadrado: '))
superficie = lado * lado
print('La superficie del cuadrado es: ' + str(superficie))

# Formulario 
nombre = input('Introduce tu nombre: ') 
apellido = input('Introduce tu apellido: ')
edad = int(input('Introduce tu edad: '))
correo = input('Introduce tu correo electrónico: ')
telefono = input('Introduce tu teléfono: ')

print('Nombre: ' + nombre)
print('Apellido: ' + apellido)
print('Tengo ' + str(edad) + 'años')
print('Correo: ' + correo)
print('Teléfono: ' + telefono)

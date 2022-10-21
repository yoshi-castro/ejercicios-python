# Sentencia if

from re import X


animal = input('Dime un animal: ')
if animal == 'perro':
    print('-guau')
print('conozco pocos animales.')

num = int(input('Ingrese un entero: '))
if num < 0:
    num = -num
print('Su valor absoluto es', num)

# Sentencia if else

animal = input('Dime un animal: ')
if animal == 'perro':
    print('-guau')
else:
    print('no conozco su sonido.')
print('conozco pocos animales.')

# Sentencia elif

animal = input('Dime un animal: ')
if animal == 'perro':
    print('-guau')
elif animal == 'gato':
    print('-miau')
elif animal == 'vaca':
    print('-muu')
else:
    print('no conozco su sonido.')
print('conozco pocos animales.')

# Sentencia do while

print('Impares menores a 10')
x=1
while x<=10:
    print(x)
    x+=2

factorial = 5
contador = factorial - 1
while contador > 0:
    factorial *= contador 
    contador -= 1

# Sentencia for

for i in 1,2,3:
    print(i)

for i in range(5):
    print(i)

for i in ['Ale','Ivan','Monse','Luis','Rafa','Luca']:
    print(i)

for i in 'Hola Mundo':
    if i == 'M':
        pass
    else
    print(i,end='')

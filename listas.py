# mix = [0, 1.0, 'dos', 3 + 4j]

# # Que tipo es cada elemento
# # for i in mix :
# #     print(f'{i:6} - Tipo: {type(i)}')

# # Imprime cual es la longitud de la lista
# # print(len(mix))

# # Imprime la lista sin lo que hay en el lugar dos
# # sin_dos = mix[:2] + mix[3:]
# # print(mix, sin_dos)

# # duplicado = mix * 2
# # print(duplicado)

# # 
# # cuadrados = [0, 1, 4, 9, 16, 25]
# # for i in range(len(cuadrados)) :
# #     print(f'{i}**2 = {cuadrados[i]}')

# cuadrados = [0, 1, 4, 9, 16, 25]
# for i in range(len(cuadrados)) :
#     cuadrados[i] = cuadrados[i] * i
#     print(f'Ahora están al cubo {cuadrados[i]}')

# cuadrados.append(7 **3)

# cuadrados.insert(6, 6 ** 3)

# cuadrados.extend([27, 1000, -1])

# cuadrados.extend(range(-1, -4, -1))

# del cuadrados[9:]

# cuadrados.remove(27)

# valor_removido = cuadrados.pop(2)

# cuadrados.clear

# print(cuadrados)

# print(valor_removido)


# vocales = ['a', 'e', 'i', 'o', 'u']

# vocales[1:4] = ['E', 'I', 'O']

# print(vocales, len(vocales))

# vocales[1:4] = []

# print(vocales, len(vocales))

# vocales[1:2] = ['e', 'i', 'o', 'u']

# print(vocales, len(vocales))

# vocales.extend(['i', 'i'])

# print(vocales.index('i'))
# print(vocales.count('i'))

# print(vocales.index('i', 4))

# vocales.reverse()

# print(vocales, len(vocales))

# vocales.sort()

# print(vocales, len(vocales))

# Carros
# carros = ['Audi', 'Ford', 'BMW', 'VW']

# carros.sort(key=len)

# print(carros)

# # Listas
# listas = [[0, 1], [2, 3, 4], [5, 6]]

# print(listas[0], listas[1:3])

# print(listas[2][1])

# x = [3, 2.5, 6, 6.3]

# Vocales

vocales1 = ['a', 'e', 'i', 'o', 'u']

vocales2 = vocales1

print(id(vocales1), id(vocales2))

vocales3 = vocales1.copy()

print(vocales1, vocales3)

print(id(vocales1), id(vocales3))

print(id(vocales1[2])), id(vocales2[2])

print(id(vocales1[2])), id(vocales3[2])

del vocales1[2]
print(vocales2, vocales3)

print(id(vocales1[2])), id(vocales3[3])

emoji_dicionario = {'feliz': 'ð', 'amo': 'ð', 'risa': 'ð¤£', 'sonrisa': 'ð', 'llorar':'ð­', \
    'beso': 'ð', 'aplauso': 'ðð¼', 'reir': 'ð', 'fuego': 'ð¥', 'roto': 'ð', 'pensando': 'ð¤', \
        'maravillado': 'ð', 'aburrido': 'ð', 'guiÃ±o': 'ð', 'ok': 'ðð¼', 'abrazo': 'ð¤', \
            'cool': 'ð', 'enojado': 'ð ', 'python': 'ð'}

frase = input('Escribe una frase: ')
frase = frase.lower()
palabras = frase.split()

respuesta = ''

for palabra in palabras:
    if palabra in emoji_dicionario:
        respuesta = respuesta + emoji_dicionario[palabra] + ' '
    else:
        respuesta = respuesta + palabra + ' '
        
print(respuesta)

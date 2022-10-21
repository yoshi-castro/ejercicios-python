emoji_dicionario = {'feliz': '😀', 'amo': '😍', 'risa': '🤣', 'sonrisa': '😊', 'llorar':'😭', \
    'beso': '😘', 'aplauso': '👏🏼', 'reir': '😁', 'fuego': '🔥', 'roto': '💔', 'pensando': '🤔', \
        'maravillado': '😍', 'aburrido': '🙄', 'guiño': '😉', 'ok': '👌🏼', 'abrazo': '🤗', \
            'cool': '😎', 'enojado': '😠', 'python': '🐍'}

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

""" Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro dessa tupla as vogais de cada palavra.
 Faça um print na tela com o nome da palavra e suas respectivas vogais"""

import unicodedata

palavras = ("gato", "livro", "computador", "café", "futebol", "praia", "viagem", "música", "filme", "jardim", "Abóbora")
vogais = ('a', 'e', 'i', 'o', 'u')
vogal = []

for palavra in palavras:
    for letra in palavra:
        letra_normalizada = (unicodedata.normalize('NFD', letra).encode('ascii', 'ignore').
                             decode('utf-8'))
        if letra_normalizada.lower() in vogais and letra_normalizada.lower() not in vogal:
            vogal.append(letra_normalizada.lower())

    print(f"A palavra {palavra} tem as vogais: {vogal}")
    vogal.clear()

# Modo sem biblioteca

palavras = ("gato", "livro", "computador", "café", "futebol", "praia", "viagem", "música", "filme", "jardim", "Abóbora")
vogais = ('a', 'e', 'i', 'o', 'u')
vogais_acentuadas = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                     'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
                     'ã': 'a', 'õ': 'o', 'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u'}

for palavra in palavras:
    vogal = []
    for letra in palavra:
        # Substitui a vogal acentuada pela não acentuada
        letra_normalizada = vogais_acentuadas.get(letra.lower(), letra.lower())
        if letra_normalizada in vogais and letra_normalizada not in vogal:
            vogal.append(letra_normalizada)

    print(f"A palavra {palavra} tem as vogais: {vogal}")




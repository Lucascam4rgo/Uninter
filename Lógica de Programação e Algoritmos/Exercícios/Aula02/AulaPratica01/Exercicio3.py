""" Crie uma variável de string que receba uma frase qualquer. Crie a segunda variável, agora contendo a metade
da string digitada. Imprima na tela somente os dois últimos caracteres da segunda variável do tipo string"""

palavra = input("Digite uma palavra qualquer: ")
metade_palavra = palavra[:int(len(palavra)/2)]

print(metade_palavra)
print(metade_palavra[-2:])


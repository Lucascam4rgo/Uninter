""" Condicional Composta """

# Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um ano
# bissexto"

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print(f"{ano} é um ano bissexto")
else:
    print("Definitivamente não é um ano bissexto")

# Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Decida-se!", caso contrário, escreva: "Você
# escolheu um caminho!"

cima = True
baixo = True

if cima and baixo == True:
    print("Decida-se!")
else:
    print("Você escolheu um caminho!")

# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar:
# adição (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da operação desejada

print("Seja bem vindo a calculadora do Python!")
print("-" * 50)
print("Escolha a operação desejada: \n")
print("1 - Adição\n")
print("2 - Subtração\n")
print("3 - Multiplicação\n")
print("4 - Divisão\n\n")

escolha = int(input("Escolha: "))

print(escolha)

if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
    print("Escolha inválida. Saindo do programa...")
    exit()
else:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if escolha == 1:
        soma = num1 + num2
        print(f"A soma dos números é igual a: {soma}")
    elif escolha == 2:
        sub = num1 - num2
        print(f"A subtração dos números é igual a: {sub}")
    elif escolha == 3:
        mult = num1 * num2
        print(f"A multiplicação dos números é igual a: {mult}")
    elif escolha == 4:
        div = num1 / num2
        print(f"A divisão dos números é igual a: {div}")
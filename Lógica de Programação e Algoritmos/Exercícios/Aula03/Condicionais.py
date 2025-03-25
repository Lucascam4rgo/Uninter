""" Condicionais Simples """

# Lê dois valores inteiros e compara ambos

x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if x > y:
    print("O primeiro valor é maior que o segundo!")


# Lê dois valores inteiros e compara ambos

x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if x > y:
    print("O primeiro valor é maior que o segundo!")
if x < y:
    print("O segundo valor é maior que o primeiro")

""" Condição Composta """

# Lê dois valores inteiros e compara ambos

x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if x > y:
    print("O primeiro valor é maior que o segundo!")
else:
    print("O segundo valor é maior que o primeiro")

# Descubra se é par ou impar

par_impar = int(input('Digite um valor inteiro: '))

if par_impar % 2 == 0:
    print("O valor é par!")
else:
    print("O valor é impar")

""" Condição Aninhada e múltipla escolha(elif)"""

# Exercício 1

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Morango')

produto = int(input('Qual a sua escolha?: '))
qtd = int(input('Quantas unidades?: '))

if produto == 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total a Pagar: {pagar}')
elif produto == 2:
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} laranjas. Total a Pagar: {pagar}')
elif produto == 3:
    pagar = qtd * 4.7
    print(f'Você comprou {qtd} morangos. Total a Pagar: {pagar}')
else:
    print("Produto inexistente")


# Exercicio 2

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Morango')

produto = int(input('Qual a sua escolha?: '))
qtd = int(input('Quantas unidades?: '))

if produto == 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} maçãs. Total a Pagar: {pagar}')
else:
    if produto == 2:
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} laranjas. Total a Pagar: {pagar}')
    else:
        if produto == 3:
            pagar = qtd * 4.7
            print(f'Você comprou {qtd} morangos. Total a Pagar: {pagar}')
        else:
            print("Produto inexistente")

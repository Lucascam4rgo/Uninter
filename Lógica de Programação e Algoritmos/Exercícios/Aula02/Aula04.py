""" Entrada """

idade = input('Qual a sua idade?: ')
print(idade)

nome = input('Qual o seu nome?: ')
print(f'Olá, {nome}, seja bem-vindo!')

""" Casting """

nota = float(input('Qual a nota que você recebeu na disciplina?: '))
print(f'Sua nota é {nota}')

""" Fluxo de execução de programa (teste de mesa) """

x = 1
y = 1
z = x + y

x = x + 2
y = y - 1
z = x + y

x = y + 1
y = x - 1
z = x + y

print(z)

""" Exercício 1 """

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = (num1 + num2)

print(f"A soma dos números {num1} e {num2} é: {soma}")

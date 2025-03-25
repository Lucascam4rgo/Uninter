# Escreva um algoritmo onde o usuário escolhe se quer comprar maçãs, laranjas e bananas. Deverá ser mostrado na tela um
# menu com a opção 1 para maçã, 2 para laranja e 3 para banana

# Depois de escolhida a fruta, deve-se digitar quantas unidades se quer comprar. O algoritmo deve calcular o preço total
# a pagar pelo produto escolhido e mostrá-lo na tela

# Maçã = 2,30 laranja = 3,60 e banana = 1,85

print('Escolha o que deseja comprar: ')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual a sua escolha?: '))
qtd = int(input('Quantas unidades?: '))

match produto:
    case 1:
        pagar = qtd * 2.3
        print(f"Você comprou {qtd} maçãs. Total à pagar: {pagar:.2f}")
    case 2:
        pagar = qtd * 3.6
        print(f"Você comprou {qtd} laranjas. Total à pagar: {pagar:.2f}")
    case 3:
        pagar = qtd * 1.85
        print(f"Você comprou {qtd} bananas. Total à pagar: {pagar:.2f}")
    case _:
        print('Produto inexistente')


def checagem_tipo(dado):
    match dado:
        case str(dado):
            print(f"String: {dado}")
        case int(dado):
            print(f"Inteiro: {dado}")
        case float(dado):
            print("Float:", dado)
        case _:
            print("Tipo desconhecido de dado.")


dados = ['Python', 42, 3.14, 23, 'C']

for dado in dados:
    checagem_tipo(dado)

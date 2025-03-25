""" Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado pelo usuário, assim
como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa r$ 60
por dia e R$ 0,15 por km rodado"""

km_rodados = float(input("Quantos Km o carro rodou?: "))
dias_rodados = float(input("Por quantos dias o carro foi alugado?: "))

preco_pagamento = (km_rodados * 0.15) + (dias_rodados * 60)

print(f"O preço a ser pago é: R${preco_pagamento:.2f}")


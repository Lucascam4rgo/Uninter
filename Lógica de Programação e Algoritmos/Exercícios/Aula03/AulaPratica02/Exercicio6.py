# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh
# consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios
# calcule o preço de acordo com a tabela a seguir: Residencial: até 500 kwh o preço é 0,40, acima disso é 0,65
# Comercial: até 1000 é 0,55, acima 0,60
# Industrial: até 5000 é 0,55 e acima de 5000 é 0,60

quantidade_kwh = float(input("Qual a quantidade de kWh consumida?: "))
tipo_instalacao = input("Qual o tipo de instalação? Digite R para residencial, C para comercial e I para Industrial: ")

if tipo_instalacao.upper() == "R":
    if quantidade_kwh <= 500:
        preco_pagar = quantidade_kwh * 0.40
        print(f"O preço a ser pago é: {preco_pagar:.2f}")
    else:
        preco_pagar = quantidade_kwh * 0.65
        print(f"O preço a ser pago é: {preco_pagar:.2f}")

elif tipo_instalacao.upper() == "C":
    if quantidade_kwh <= 1000:
        preco_pagar = quantidade_kwh * 0.55
        print(f"O preço a ser pago é: {preco_pagar:.2f}")
    else:
        preco_pagar = quantidade_kwh * 0.60
        print(f"O preço a ser pago é: {preco_pagar:.2f}")

elif tipo_instalacao.upper() == "I":
    if quantidade_kwh <= 5000:
        preco_pagar = quantidade_kwh * 0.55
        print(f"O preço a ser pago é: {preco_pagar:.2f}")
    else:
        preco_pagar = quantidade_kwh * 0.60
        print(f"O preço a ser pago é: {preco_pagar:.2f}")

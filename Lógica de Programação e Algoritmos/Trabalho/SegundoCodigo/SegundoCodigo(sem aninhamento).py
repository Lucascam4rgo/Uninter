# Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende
# Marmitas de Bife Acebolado ou Filé de Frango. Você ficou com a parte de desenvolver a interface do cliente
# para retirada do produto.

# A Loja possui seguinte relação:
# •	Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;
# •	Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;
# •	Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;

# Elabore um programa em Python que:
# A.	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
# Por exemplo: print (“Bem vindos a loja de Marmitas do Bruno Kostiuk”)
# Além do seu nome completo, deve-se implementar um print com um Menu para o cliente. [EXIGÊNCIA DE CÓDIGO 1 de 8];
# B.	Deve-se implementar o input do sabor (BA/FF) e o print “Sabor inválido. Tente novamente" se o usuário entra com
# valor diferente de BA e FF [EXIGÊNCIA DE CÓDIGO 2 de 8];
# C.	Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com
# entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
# D.	Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das
# combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];
# E.	Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
# F.	Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do
# item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
# G.	Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
# H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
# I.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo e o menu para o cliente conhecer
# as opções  [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
# J.	Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
# K.	Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
# L.	Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];

def mostrar_menu():
    print("-" * 5 + " Bem-vindos a Loja de Marmitas do Lucas Camargo" + "-" * 13)
    print("-" * 25 + " Cardápio " + "-" * 30)
    print("-" * 65)
    print("-" * 3 + "|  TAMANHO  |  BIFE ACEBOLADO(BA)  |  FILÉ DE FRANGO(FF)  |" + "-" * 3)
    print("-" * 3 + "|     P     |       R$ 16.00       |      R$ 15.00        |" + "-" * 3)
    print("-" * 3 + "|     M     |       R$ 18.00       |      R$ 17.00        |" + "-" * 3)
    print("-" * 3 + "|     G     |       R$ 22.00       |      R$ 21.00        |" + "-" * 3)
    print("-" * 65)


precos = {
    "P": {"BA": 16.00, "FF": 15.00},
    "M": {"BA": 18.00, "FF": 17.00},
    "G": {"BA": 22.00, "FF": 21.00}
}
sabores = ["Bife Acebolado", "Filé de Frango"]
acumulador_preco = 0

mostrar_menu()

while True:
    sabor = input("Entre com o sabor desejado (BA/FF): ")

    if sabor.upper() not in ["BA", "FF"]:
        print("Sabor inválido. Tente novamente")
        continue

    tamanho = input("Entre com o tamanho desejado(P/M/G): ")

    if tamanho.upper() not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente")
        continue

    acumulador_preco += precos[tamanho.upper()][sabor.upper()]
    if sabor.upper() == "BA":
        print(f"Você pediu um {sabores[0]} no tamanho {tamanho.upper()}: R$ {precos[tamanho.upper()][sabor.upper()]:.2f}")
    else:
        if sabor.upper() == "FF":
            print(f"Você pediu um {sabores[1]} no tamanho {tamanho.upper()}: R$ {precos[tamanho.upper()][sabor.upper()]:.2f}")

    mais_alguma_coisa = input("Deseja continuar?(S/N): ")
    if mais_alguma_coisa.upper() not in ["S", "N"]:
        print("Comando inválido. Tente novamente!")
        mais_alguma_coisa = input("Deseja continuar?(S/N): ")
    elif mais_alguma_coisa in "Ss":
        continue
    else:
        print(f"O valor total a ser pago: {acumulador_preco:.2f}")
        print("Até mais, volte sempre!")
        break






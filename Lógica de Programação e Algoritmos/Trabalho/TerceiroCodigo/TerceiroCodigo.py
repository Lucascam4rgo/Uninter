# Você foi contratado para desenvolver um sistema de cobrança de serviços de uma fábrica que vende Camisetas em atacado.
# Você ficou com a parte de desenvolver a interface com o funcionário.
# A Fábrica opera as vendas da seguinte maneira:
#
# •	Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos;
# •	Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos;
# •	Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos;
# •	Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos;
#
# •	Se número de camisetas for menor que 20 não há desconto na venda;
# •	Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%;
# •	Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%;
# •	Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%;
# •	Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas;
#
# ♦	Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais;
# ♦	Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais;
# ♦	Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais;
#
# O valor final da conta é calculado da seguinte maneira:
#
# total = (modelo * num_camisetas) + frete
#
# Elabore um programa em Python que:
# A.	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
# Por exemplo: print(“Bem vindos a Fábrica de Camisetas do Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 7];
# B.	Deve-se implementar a função escolha_modelo() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
# a.	Pergunta o modelo desejado;
# b.	Retorna o valor do modelo com base na escolha do usuário (use return);
# c.	Repete a pergunta do item B.a se digitar uma opção diferente de: MCS/MLS/MCE/MLE;
# C.	Deve-se implementar a função num_camisetas() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
# a.	Pergunta o número de camisetas;
# b.	Retorna (use return) o número de camisetas com desconto seguindo a regra do enunciado (desconto calculado
# em cima do número de camisetas);
# c.	Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico
# (use try/except para não numérico)
# D.	Deve-se implementar a função frete() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
# a.	Pergunta pelo serviço adicional de frete;
# b.	Retorna (use return) o valor de apenas uma das opções de frete
# c.	Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
# E.	Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função,
# conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
# F.	Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
# G.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
# H.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
# I.	Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de modelo
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
# J.	Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de camisetas
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
# K.	Deve-se apresentar na saída de console um pedido com opção de modelo, número de camisetas e frete válidos
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];

def escolha_modelo():
    #Usar o try para coletar qualquer exceção que ocorra no código
    try:
        #Enquanto verdadeiro, a compra continuará
        while True:
            # Escolha do modelo
            modelo = input("Entre com o modelo desejado (Digite a sigla): "
                           "MCS - Manga Curta Simples\n"
                           "MCE - Manga Curta com Estampa\n"
                           "MLS - Manga Longa Simples\n"
                           "MLE - Manga Longa Com Estampa\n"
                           ">>").upper()

            # Condições para que o valor unitário de cada modelo seja retornado
            if modelo not in ['MCS', 'MLS', 'MCE', 'MLE']:
                print("Escolha inválida, entre com o modelo novamente")
                continue
            elif modelo == "MCS":
                valor_unitario = 1.8
                return valor_unitario
            elif modelo == "MCE":
                valor_unitario = 2.1
                return valor_unitario
            elif modelo == "MLS":
                valor_unitario = 2.9
                return valor_unitario
            elif modelo == "MLE":
                valor_unitario = 3.2
                return valor_unitario
    # Exceção para um erro genérico
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")


def num_camisetas():
    try:
        while True:
            num_camiseta = int(input("Entre com o número de camisetas: "))

            # Condições para que o desconto a partir do número de camisetas aconteça
            if num_camiseta > 20000 or not isinstance(num_camiseta, int):
                print("Não aceitamos tantas camisetas de uma vez")
                print("Entre com o número de camisetas novamente.")
                continue
            elif num_camiseta < 0:
                print("Nenhuma camiseta foi comprada.")
                exit()
            elif 0 < num_camiseta < 20:
                return num_camiseta
            elif 20 <= num_camiseta < 200:
                valor_desconto = num_camiseta * 5 / 100
                desconto = num_camiseta - valor_desconto
                return desconto
            elif 200 <= num_camiseta < 2000:
                valor_desconto = num_camiseta * 7/100
                desconto = num_camiseta - valor_desconto
                return desconto
            elif 2000 <= num_camiseta <= 20000:
                valor_desconto = num_camiseta * 12/100
                desconto = num_camiseta - valor_desconto
                return desconto
    #Exceção de erro no valor, caso um número inválido seja digitado
    except ValueError:
        print("Por favor, insira um número valido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")


def frete():
    try:
        while True:
            tipo_frete = int(input("Escolha o tipo de frete: "
                               "1 - Frete por transportadora - R$ 100.00\n"
                               "2 - Frete por Sedex - R$ 200.00\n"
                               "0 - Retirar o pedido na fábrica - Grátis\n"
                               ">>"))
            # Outra condição para que o valor do frete seja calculado
            if tipo_frete not in [1, 2, 0]:
                print("Opção inválida. Tente novamente")
                continue
            elif tipo_frete == 1:
                valor_frete = 100
                return valor_frete
            elif tipo_frete == 2:
                valor_frete = 200
                return valor_frete
            elif tipo_frete == 0:
                valor_frete = 0
                return valor_frete
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {str(e)}")








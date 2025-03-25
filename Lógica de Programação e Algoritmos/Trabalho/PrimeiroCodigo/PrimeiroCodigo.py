# Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa
# X que aceita cartões de crédito. Uma das estratégias de vendas dessa empresa X é cobrar um Juros maior
# conforme a quantidade de parcelas que o cliente desejar, conforme a listagem abaixo:
#
# 	Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
# 	Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);
# 	Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
# 	Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
# 	Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);
#
# O valor da parcela é calculado da seguinte maneira:
# valorDaParcela = (valorDoPedido*(1+juros))/quantidadeParcelas
# O valor total parcelado é calculado da seguinte maneira:
# valorTotalParcelado=valorDaParcela*quantidadeParcelas
#
# Elabore um programa em Python que:
# 	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
# Por exemplo: print(“Bem-vindos a loja do Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6];
# 	Deve-se implementar o input do valorDoPedido e da quantidadeParcelas [EXIGÊNCIA DE CÓDIGO 2 de 6];
# 	Deve-se implementar o Juros conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior)
# 	[EXIGÊNCIA DE CÓDIGO 3 de 6];
# 	Deve-se implementar o valorDaParcela e valorTotalParcelado [EXIGÊNCIA DE CÓDIGO 4 de 6];
# 	Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
# 	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
# 	Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
# 	Deve-se apresentar na saída de console um parcelamento com Juros (quantidadeParcelas maior ou igual a 4)
# 	apresentando o valor da Parcela e o valor Total Parcelado [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];


print("Bem vindos a Loja do Lucas Camargo")

valordopedido = float(input("Entre com o valor do pedido: "))
qtdparcelas = int(input("Entre com a quantidade de parcelas: "))

# Verifica a quantidade de parcelas e aplica a taxa de juros correspondente
if qtdparcelas < 4:
    # Sem juros para menos de 4 parcelas
    valorparcela = valordopedido * (1 + 0)/qtdparcelas
    valortotalparcelado = valorparcela * qtdparcelas
    print(f"O valor das parcelas é de:R$ {valorparcela:.2f}")
    print(f"O valor total parcelado é de:R$ {valortotalparcelado:.2f}")
elif 4 >= qtdparcelas < 6:
    # Aplica 4% de juros para 4 e 5 parcelas
    valorparcela = valordopedido * (1 + 4 / 100) / qtdparcelas
    valortotalparcelado = valorparcela * qtdparcelas
    print(f"O valor das parcelas é de:R$ {valorparcela:.2f}")
    print(f"O valor total parcelado é de:R$ {valortotalparcelado:.2f}")
elif 6 >= qtdparcelas < 9:
    # Aplica 8% de juros para 6 a 8 parcelas
    valorparcela = valordopedido * (1 + 8 / 100) / qtdparcelas
    valortotalparcelado = valorparcela * qtdparcelas
    print(f"O valor das parcelas é de:R$ {valorparcela:.2f}")
    print(f"O valor total parcelado é de:R$ {valortotalparcelado:.2f}")
elif 9 >= qtdparcelas < 13:
    # Aplica 16% de juros para 9 a 12 parcelas
    valorparcela = valordopedido * (1 + 16 / 100) / qtdparcelas
    valortotalparcelado = valorparcela * qtdparcelas
    print(f"O valor das parcelas é de:R$ {valorparcela:.2f}")
    print(f"O valor total parcelado é de:R$ {valortotalparcelado:.2f}")
else:
    # Aplica 32% de juros para 13 parcelas ou mais
    valorparcela = valordopedido * (1 + 32 / 100) / qtdparcelas
    valortotalparcelado = valorparcela * qtdparcelas
    print(f"O valor das parcelas é de:R$ {valorparcela:.2f}")
    print(f"O valor total parcelado é de:R$ {valortotalparcelado:.2f}")

# Fim do programa: o valor total parcelado é calculado e armazenado na variável 'valortotalparcelado'



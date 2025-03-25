""" Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado
a ele. Calcule e exiba o valor do desconto e o preço final do produto """

preco_prod = float(input("Digite o preço do produto: "))
percentual_desc = float(input("Digite o percentual de desconto: "))

valor_desc = preco_prod * (percentual_desc/100)
preco_prod_final = preco_prod - valor_desc

print(f"O preço do produto final é: {preco_prod_final}R$")
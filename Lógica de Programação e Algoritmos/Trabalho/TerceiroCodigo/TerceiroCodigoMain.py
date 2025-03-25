# Importa o código com as funções
import TerceiroCodigo as t

print("Bem vindo a Fábrica de Camisetas do Lucas Camargo")

#Cria as variáveis a partir das funções do TerceiroCodigo
modelo = t.escolha_modelo()

num_camisetas = t.num_camisetas()

frete = t.frete()

#Conta final para calcular o total
total = (modelo * num_camisetas) + frete
print(f"Total: R$ {total:.2f} (Modelo: {modelo:.2f} * Quantidade(com desconto): {num_camisetas} + Frete: {frete}")
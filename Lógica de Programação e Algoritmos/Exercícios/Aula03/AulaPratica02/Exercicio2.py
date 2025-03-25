import random

""" Condicionais Simples """

# Se idade é maior que 60, escreva "Você tem direitos aos benefícios"

idade = int(input("Digite sua idade: "))

if idade > 60:
    print("Você tem direitos aos benefícios")

# Se dano é maior que 10 e escudo é igual a 0, escreva: "Você está morto!

print("Prepare-se para a batalha!")
print("Inimigo atacou!")
dano = random.randint(0, 15)
escudo = random.randint(0, 15)

if dano > 10 and escudo == 0:
    print(f"Você está morto. Dano: {dano}, Escudo: {escudo}")

# Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resultarem em True, escreve: "Você escapou"

norte = False
sul = True
leste = False
oeste = False

if norte or sul or leste or oeste == True:
    print("Você escapou")

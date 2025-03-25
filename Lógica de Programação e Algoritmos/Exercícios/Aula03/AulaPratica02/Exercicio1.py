""" Expressões Booleanas """

# O somatório de 2 com 2 é menor que 4

print(2 + 2 < 4)  # False

# O valor 7 // 3 é igual a 1 + 1

print(7 // 3 == 1 + 1)  # True

# A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25

print(3 ** 2 + 4 ** 2 == 25)  # True

# A soma de 2, 4 e 6 é maior que 12

print(2 + 4 + 6 > 12)  # False

# 1387 é divisível por 19
if 1387 % 19 == 0:
    print("Verdadeiro")
else:
    print("Falso")

print(1387 % 19 == 0)

# 31 é par
if 31 % 2 == 0:
    print("31 é par")
else:
    print("Não, 31 é ímpar")

print(31 % 2 == 0)

# O menor valor entre 34, 29 e 31 é menor que 30
print(min(34, 29, 31) < 30)


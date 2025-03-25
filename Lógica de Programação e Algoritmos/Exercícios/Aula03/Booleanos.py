""" Booleanos """

# not

x = True
y = False

print(not x)
print(not y)

# and

x = True
y = False

print(x and y)

# or

x = False
y = False

print(x or y)

# Expressões Lógicas/Booleanas

x = 10
y = 1
res = not x > y  # False
print(res)

x = 10
y = 1
z = 5.5

res = x > y and z == y  # True and False = False
print(res)

x = 10
y = 1
z = 5.5

res = x > y or not z == y and y != y + z / x  # True or True and True = True
print(res)


# Exercício

m1 = float(input('Digite a nota da 1ª Matéria: '))
m2 = float(input('Digite a nota da 2ª Matéria: '))
m3 = float(input('Digite a nota da 3ª Matéria: '))

if m1 >= 7 and m2 >= 7 and m3 >= 7:
    print("O aluno está aprovado de ano!")
else:
    print('O aluno não passou de ano!')





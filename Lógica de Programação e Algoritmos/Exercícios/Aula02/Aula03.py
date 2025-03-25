""" Manipulação de Strings """

""" Concatenação """

s1 = "Lógica de Programação"
s1 = s1 + ' e Algoritmos'

print(s1)

""" Repetindo Strings """

s1 = 'A' + '-' * 10 + 'B'
print(s1)

s1 = 'A' + ' ' * 10 + 'B'
print(s1)

""" Composição por marcador de posição """

nota = 8.5
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)

""" Várias variáveis """

nota = 8.5
s1 = 'Você tirou %.1f na disciplina de Algoritmos' % nota
print(s1)

""" Várias variáveis """

nota = 8.5
disciplina = "Algoritmos"

s1 = 'Você tirou %.1f na disciplina de %s' % (nota, disciplina)
print(s1)

""" Composição Moderna """

nota = 8.5
disciplina = "Algoritmos"

s1 = "Você tirou {} na disciplina de {}".format(nota, disciplina)
print(s1)

""" Composição por f-string """

nota = 8.5
disciplina = "Algoritmos"

s1 = f"Você tirou {nota} na disciplina de {disciplina}"
print(s1)

""" Fatiamento """

s1 = "Lógica de Programação e Algoritmos"
print(s1[0:6])

s1 = "Lógica de Programação e Algoritmos"
print(s1[24:34])

s1 = "Lógica de Programação e Algoritmos"
print(s1[:6])

""" Tamanho(Length) """

s1 = 'Lógica de Programação e Algoritmos'
print(len(s1))
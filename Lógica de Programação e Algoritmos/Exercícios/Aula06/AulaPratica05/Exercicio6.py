""" Programa pra ler nome, ano de nascimento e sexo de diferentes pessoas """

from datetime import datetime

dicionario_pessoas = {'nome': [], 'idade': [], 'sexo': []}
cadastros = 0
soma_media = 0
mulheres_menos_30 = []
homens_acima_media = []

print("CADASTRO DE PESSOAS")
print('-' * 20)

while True:
    nome = input("Digite seu nome: ")
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    sexo = input("Digite seu sexo, Feminino(F) ou Masculino(M): ")

    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    print(idade)

    dicionario_pessoas['nome'].append(nome)
    dicionario_pessoas['idade'].append(idade)
    dicionario_pessoas['sexo'].append(sexo.upper())

    cadastros += 1

    soma_media += idade

    sair = input("Deseja sair? (Digite sim ou não): ")

    if sair.upper() in ["N", "NÃO"]:
        continue
    if sair.upper() in ["S", "SIM"]:
        media = soma_media/cadastros

        for i in range(cadastros):
            if dicionario_pessoas['sexo'][i] == "M" and dicionario_pessoas['idade'][i] > media:
                homens_acima_media.append([dicionario_pessoas['nome'][i], dicionario_pessoas['idade'][i]])
            if dicionario_pessoas['sexo'][i] == "F" and dicionario_pessoas['idade'][i] < 30:
                mulheres_menos_30.append([dicionario_pessoas['nome'][i], dicionario_pessoas['sexo'][i], dicionario_pessoas['idade'][i]])

        print(f"CADASTROS REALIZADOS: {cadastros}")
        print(f"MÉDIA DAS IDADES: {media:.2f}")
        print(f"LISTA DE MULHERES COM MENOS DE 30 ANOS: {mulheres_menos_30}")
        print(f"HOMENS COM IDADE ACIMA DA MÉDIA: {homens_acima_media}")

        #print(f"HOMENS COM IDADE ACIMA DA MÉDIA: {}")







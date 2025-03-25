# Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento
# de funcionários. Este software deve ter o seguinte menu e opções:
#
# 1)	Cadastrar Funcionário
# 2)	Consultar Funcionário
# 1.	Consultar Todos
# 2.	Consultar por Id
# 3.	Consultar por setor
# 4.	Retornar ao menu
# 3)	Remover Funcionário
# 4)	Encerrar Programa
#
# Elabore um programa em Python que:
# A.	Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
# Por exemplo: print(“Bem vindos a empresa do Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 8];
# B.	Deve-se implementar uma lista com o nome de lista_funcionarios e a variável id_global com valor inicial igual
# ao número de seu RU [EXIGÊNCIA DE CÓDIGO 2 de 8];
# C.	Deve-se implementar uma função chamada cadastrar_funcionario(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
# a.	Pergunta nome, setor, salario do funcionário;
# b.	Armazena o id (este é fornecido via parâmetro da função), nome, setor, salario dentro de um dicionário;
# c.	Copiar o dicionário para dentro da lista_funcionarios (utilizar o copy);
# D.	Deve-se implementar uma função chamada consultar_funcionarios() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
# a.	Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor
# / 4. Retornar ao menu):
# i.	Se Consultar Todos, apresentar todos os funcionários com todos os seus dados cadastrados;
# ii.	Se Consultar por Id, solicitar ao usuário que informe um id, e apresentar o funcionário específico com todos
# os seus dados cadastrados;
# iii.	Se Consultar por Setor, solicitar ao usuário que informe o setor, e apresentar o(s) funcionário(s) do setor com
# todos os seus dados cadastrados;
# iv.	Se Retornar ao menu, deve-se retornar ao menu principal (return);
# v.	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
# vi.	Enquanto o usuário não escolher a opção 4, o menu consultar funcionários deve se repetir.
# E.	Deve-se implementar uma função chamada remover_funcionario() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
# a.	Deve-se pergunta pelo id do funcionário a ser removido;
# b.	Remover o funcionário da lista_funcionarios;
# c.	Se o id fornecido não for de um funcionário da lista, printar “Id inválido” e repetir a pergunta E.a.
# F.	Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de função,
# em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
# a.	Deve-se pergunta qual opção deseja (1. Cadastrar Funcionário / 2. Consultar Funcionário
# / 3. Remover Funcionário / 4. Encerrar Programa):
# i.	Se Cadastrar Funcionário, incrementar em um id_ global e chamar a função cadastrar_funcionario(id_ global);
# ii.	Se Consultar Funcionário, chamar função consultar_funcionario ();
# iii.	Se Remover Funcionário, chamar função remover_funcionario();
# iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
# v.	Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a.
# vi.	Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
# G.	Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro)
# [EXIGÊNCIA DE CÓDIGO 7 de 8];
# H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
# I.	Deve-se apresentar na saída de console uma mensagem com o seu nome completo
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
# J.	Deve-se apresentar na saída de console um cadastro de 3 funcionários (sendo 2 deles no mesmo setor)
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
# K.	Deve-se apresentar na saída de console uma consulta de todos os funcionários
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
# L.	Deve-se apresentar na saída de console uma consulta por código (id) de um dos funcionários
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
# M.	Deve-se apresentar na saída de console uma consulta por setor em que 2 funcionários sejam do mesmo setor
# [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
# N.Deve-se apresentar na saída de console uma remoção de um dos funcionários seguida de uma consulta de todos os
# funcionários [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];

print("Bem vindos a empresa do [Seu Nome Completo]")  # EXIGÊNCIA DE CÓDIGO 1 de 8

# Lista para armazenar todos os funcionários e uma variável para o id_global inicializada com o RU
lista_funcionarios = []  # EXIGÊNCIA DE CÓDIGO 7 de 8
id_global = 4916567  # EXIGÊNCIA DE CÓDIGO 2 de 8


def cadastrar_funcionario(id_func):
    """
    Função para cadastrar um novo funcionário.
    :param id_func: int - Identificador único do funcionário.
    """
    try:
        print("-" * 40)
        print("-" * 9, "MENU CADASTRAR FUNCIONÁRIO", "-" * 11)
        # Coletando informações do funcionário
        print("Id do Funcionário: ", id_func)
        funcionario = {
            'id': id_func,
            'nome': input("Entre com o nome do funcionário: "),
            'setor': input("Qual é o setor do funcionário?: ").upper(),
            'salario': float(input("Qual o salário do funcionário?: "))
        }
        # Adicionando o dicionário do funcionário na lista usando cópia
        lista_funcionarios.append(funcionario.copy())  # Copia do dicionário é adicionada na lista
        print("-" * 40)
    except Exception as e:
        # Tratamento de exceção genérica
        print("Um erro inesperado aconteceu e não foi possível cadastrar o funcionário: ", str(e))


def consultar_funcionarios():
    """
    Função para consultar funcionários cadastrados.
    """
    try:
        while True:
            print("-" * 40)
            print("-" * 9, "MENU CONSULTAR FUNCIONÁRIO", "-" * 11)
            # Menu de consulta de funcionários
            escolha_consulta = int(input("Escolha a opção desejada: \n"
                                         "1 - Consultar todos os Funcionários\n"
                                         "2 - Consultar Funcionário por Id\n"
                                         "3 - Consultar Funcionário(s) por Setor\n"
                                         "4 - Retornar\n"
                                         ">>"))

            match escolha_consulta:
                case 1:
                    # Exibindo todos os funcionários
                    for funcionario in lista_funcionarios:
                        print(f"id: {funcionario['id']}")
                        print(f"nome: {funcionario['nome']}")
                        print(f"setor: {funcionario['setor']}")
                        print(f"salário: {funcionario['salario']}\n")
                case 2:
                    # Consultando funcionário por ID
                    func_id_busca = int(input("Digite o ID do funcionário: "))
                    funcionario_encontrado = False  # Flag para verificar se o funcionário foi encontrado
                    for funcionario in lista_funcionarios:
                        if func_id_busca == funcionario['id']:
                            print(f"id: {funcionario['id']}")
                            print(f"nome: {funcionario['nome']}")
                            print(f"setor: {funcionario['setor']}")
                            print(f"salário: {funcionario['salario']}\n")
                            funcionario_encontrado = True
                            break
                    if not funcionario_encontrado:
                        print("Funcionário com ID especificado não encontrado.")
                case 3:
                    # Consultando funcionários por setor
                    func_setor_busca = input("Digite o setor do(s) funcionário(s): ").upper()
                    funcionarios_encontrados = False  # Flag para verificar se algum funcionário foi encontrado
                    for funcionario in lista_funcionarios:
                        if func_setor_busca == funcionario['setor']:
                            print(f"id: {funcionario['id']}")
                            print(f"nome: {funcionario['nome']}")
                            print(f"setor: {funcionario['setor']}")
                            print(f"salário: {funcionario['salario']}\n")
                            funcionarios_encontrados = True
                    if not funcionarios_encontrados:
                        print("Nenhum funcionário encontrado no setor especificado.")
                case 4:
                    # Retornando ao menu principal
                    return
                case _:
                    # Opção inválida
                    print("Opção inválida. Tente novamente")
                    continue
            print("-" * 40)
    except Exception as e:
        # Tratamento de exceção genérica
        print("Um erro inesperado aconteceu e não foi possível consultar o(s) funcionário(s): ", str(e))


def remover_funcionario():
    try:
        while True:
            id_remover = int(input("Digite o id a ser removido: "))
            for funcionario in lista_funcionarios:
                if id_remover == funcionario['id']:
                    lista_funcionarios.remove(funcionario)
                    print(f"O funcionário {funcionario['nome']} com id {id_remover} "
                          f"foi removido da lista de funcionários.")
                    return
                elif id_remover not in lista_funcionarios:
                    print("Esse ID não existe na nossa lista de funcionários")
                    continue
    except Exception as e:
        print("Um erro inesperado aconteceu e não foi possível remover o funcionário: ", str(e))




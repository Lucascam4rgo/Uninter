import QuartoCodigo as q

# Menu principal do programa
while True:
    print("-" * 40)
    print("-" * 9, "MENU PRINCIPAL", "-" * 11)
    # Menu principal com as opções
    escolha = int(input("Escolha a opção desejada: \n"
                        "1 - Cadastrar Funcionário\n"
                        "2 - Consultar Funcionário\n"
                        "3 - Remover Funcionário\n"
                        "4 - Encerrar Programa\n"
                        ">>"))

    match escolha:
        case 1:
            # Cadastra novo funcionário
            q.cadastrar_funcionario(q.id_global)
            q.id_global += 1  # Incrementa o id_global
        case 2:
            # Consulta funcionários
            q.consultar_funcionarios()
        case 3:
            # Remove funcionário
            q.remover_funcionario()
        case 4:
            # Encerra o programa
            print("Encerrando o programa...")
            break
        case _:
            # Opção inválida
            print("Opção inválida. Tente novamente")


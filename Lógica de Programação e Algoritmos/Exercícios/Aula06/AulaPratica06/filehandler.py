def existearquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def abrirarquivoleitura(nomearquivo):
    try:
        a = open(nomearquivo, 'r')
    except:
        print("Não foi possível abrir para leitura.")
    else:
        print(f"Arquivo {nomearquivo} aberto com sucesso.")
        return a


def criararquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'wt+')
        a.close()
    except:
        print("Erro na criação do arquivo.")
    else:
        print(f"Arquivo {nomearquivo} criado com sucesso.")


def listararquivo(nomearquivo):
    try:
        a = open(nomearquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        dados = a.readlines()
    finally:
        a.close()
        return dados


def inserir_score(nomearquivo, nomejogador, score):
    try:
        a = open(nomearquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogador, score))
    finally:
        a.close()
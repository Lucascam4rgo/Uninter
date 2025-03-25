""" Jokenpô """

import random
import time


def validaint(msg, minimo, maximo):
    while True:
        x = int(input(msg))
        if minimo <= x <= maximo:
            return x
        else:
            print(f"Por favor, insira um valor entre {minimo} e {maximo}.")


resultados = {
    (1, 1): "Empate: Ambos escolheram Pedra",
    (1, 2): "Computador venceu: Papel cobre Pedra",
    (1, 3): "Você venceu: Pedra quebra Tesoura",
    (2, 1): "Você venceu: Papel cobre Pedra",
    (2, 2): "Empate: Ambos escolheram Papel",
    (2, 3): "Computador venceu: Tesoura corta Papel",
    (3, 1): "Computador venceu: Pedra quebra Tesoura",
    (3, 2): "Você venceu: Tesoura corta Papel",
    (3, 3): "Empate: Ambos escolheram Tesoura",
}

vitorias_jogador = []
vitorias_pc = []
empate = []

print("BEM-VINDO AO JOKENPÔ ONLINE")
print("-" * 30)
print("SERÁ QUE VOCÊ CONSEGUE ME VENCER?")

while True:
    escolha = validaint("Escolha entre 1 - Pedra, 2 - Papel e 3 - Tesoura "
                        "(Digite 0 pra sair se quiser, prometo que não vou saber sua escolha!!): ", 1, 3)

    if escolha == 0:
        if len(vitorias_jogador) > len(vitorias_pc):
            print(f"O jogador venceu com {len(vitorias_jogador)} vitória(s) contra o PC que ganhou {len(vitorias_pc)} "
                  f"vez(es). Parabéns!")
        elif len(vitorias_jogador) < len(vitorias_pc):
            print(f"O jogador perdeu com {len(vitorias_jogador)} vitória(s) contra o PC que ganhou {len(vitorias_pc)} "
                  f"vez(es). Boa sorte da próxima vez!")
        else:
            print(f"Deu empate: Os dois jogadores ficaram com {len(vitorias_jogador)} vitórias")
        print("Obrigado por jogar!")
        exit()

    escolha_pc = random.randint(1, 3)

    print("VAMOS LÁ, NO 3!")

    time.sleep(0.5)

    print("1")

    time.sleep(0.5)

    print("2")

    time.sleep(0.5)

    print("3!!!")

    time.sleep(0.5)

    resultado = resultados.get((escolha, escolha_pc))
    print(resultado)
    if escolha == escolha_pc:
        empate.append(resultado)
    elif escolha == 1 and escolha_pc == 3 or escolha == 2 and escolha_pc == 1 or escolha == 3 and escolha_pc == 2:
        vitorias_jogador.append(resultado)
    else:
        vitorias_pc.append(resultado)

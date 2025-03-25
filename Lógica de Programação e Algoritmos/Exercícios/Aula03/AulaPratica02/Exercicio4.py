# Faça um algoritmo que recebe três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique
# se os valores formam um triângulo e classifique como equilátero (três lados iguais), isósceles (dois lados iguais) ou
# Escaleno (Três lados diferentes)

primeiro_lado = int(input("Digite o tamanho do primeiro lado: "))
segundo_lado = int(input("Digite o tamanho do segundo lado: "))
terceiro_lado = int(input("Digite o tamanho do terceiro lado: "))

if (primeiro_lado > 0 and segundo_lado > 0 and terceiro_lado > 0) and (primeiro_lado + segundo_lado > terceiro_lado and
                                                                    primeiro_lado + terceiro_lado > segundo_lado and
                                                                       segundo_lado + terceiro_lado > primeiro_lado):
    if primeiro_lado == segundo_lado == terceiro_lado:
        print("É um triângulo equilátero")
    elif (primeiro_lado == segundo_lado) or (primeiro_lado == terceiro_lado) or (segundo_lado == terceiro_lado):
        print("É um triângulo isósceles")
    elif primeiro_lado != segundo_lado != terceiro_lado:
        print("É um triângulo escaleno")
else:
    print("Os valores não correspondem a um triângulo válido")

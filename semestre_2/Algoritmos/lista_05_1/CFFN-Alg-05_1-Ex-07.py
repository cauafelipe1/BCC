# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 07

'''Usando a função da questão anterior, crie um novo programa que lance o dado 1 milhão de
vezes. Conte e imprima quantas vezes cada número saiu. A probabilidade deu certo? Ou seja,
a porcentagem dos números sorteados foi parecida?'''

from random import randint

def sorteia_dado():
    x = randint(1,6)
    return x

def um_milhao_de_tentativas():
    i = 0
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    cinco = 0
    seis = 0
    milhao = 1000000
    while i < milhao:
        y = sorteia_dado()
        if y == 1:
            um += 1
        elif y == 2:
            dois += 1
        elif y == 3:
            tres += 1
        elif y == 4:
            quatro += 1
        elif y == 5:
            cinco += 1
        elif y == 6:
            seis += 1
        i += 1
    um_porcentagem = (um/milhao) * 100
    dois_porcentagem = (dois/milhao) * 100
    tres_porcentagem = (tres/milhao) * 100
    quatro_porcentagem = (quatro/milhao) * 100
    cinco_porcentagem = (cinco/milhao) * 100
    seis_porcentagem = (seis/milhao) * 100
    print("Porcentagens em relação ao sorteio:")
    print(f"1: {um} sorteios de {milhao}: {um_porcentagem}%")
    print(f"2: {dois} sorteios de {milhao}: {dois_porcentagem}%")
    print(f"3: {tres} sorteios de {milhao}: {tres_porcentagem}%")
    print(f"4: {quatro} sorteios de {milhao}: {quatro_porcentagem}%")
    print(f"5: {cinco} sorteios de {milhao}: {cinco_porcentagem}%")
    print(f"6: {seis} sorteios de {milhao}: {seis_porcentagem}%")

um_milhao_de_tentativas()
# Como pode-se notar, proximo à casa de 1 milhão de tentativas
# as porcentagens vão ficando cada vez mais semelhantes
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 01

'''Escreva um programa Python que leia números inteiros (do usuário) e os
armazena em uma lista. Seu programa deve continuar lendo inteiros até que o usuário entre
com o valor 0 (zero). Então, o programa deve exibir em ordem crescente todos os números
digitados pelo usuário sem incluir o valor 0, com um valor em cada linha impressa. Obs.: você
pode implementar o algoritmo de ordenação BubbleSort ou usar o método sort ou a função
sorted para ordenar a lista.'''

def crescente(inteiros):
    inteiros.sort()
    print("\nNúmeros ordenados (ordem crescente): ")
    for i in inteiros:
        print(i)


def main():

    inteiros = []
    while True:
        try:
            x = int(input("Insira o valor inteiro (0 para encerrar):"))
            if x == 0:
                break
            else:
                inteiros.append(x)
        except ValueError:
            print("Insira um valor inteiro!!")
            continue
    return crescente(inteiros)

if __name__ == "__main__":
    main()
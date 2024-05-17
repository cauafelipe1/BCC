# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 02

'''Escreva um programa Python que leia números inteiros (do usuário) e
os armazena em uma lista. Seu programa deve continuar lendo inteiros até que o usuário
entre com o valor 0 (zero). Então, o programa deve exibir em ordem decrescente todos os
números digitados pelo usuário sem incluir o valor 0, com um valor em cada linha impressa.'''

def decrescente(inteiros):
    inteiros.sort(reverse = True)
    print("\nNúmeros ordenados (ordem decrescente): ")
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
    return decrescente(inteiros)

if __name__ == "__main__":
    main()
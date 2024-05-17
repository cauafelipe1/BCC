# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 06

'''Um divisor de um numero inteiro n é um número inteiro positivo menor
que n, tal que divida n em partes inteiras (divisão exata, sem resto). Escreva uma função
Python que calcula todos os divisores de um número inteiro positivo. A função deve retornar
uma lista contendo todos os divisores. Escreva uma função main para demonstrar o
funcionamento da sua solução, a função main deve ler um número do usuário e imprimir todos
os seus divisores.'''


def encontrar_divisores(n):
    divisores = []
    n_divisores = 0
    for i in range(1, n+1):
        if n % i == 0:
            n_divisores += 1
            divisores.append(i)
    print(f"O número {n} possui {n_divisores} divisores, são eles: ")
    for i in divisores:
        print(i)

def main():
    while True:
        try:
            n = int(input("Insira um valor inteiro positivo:"))
            break
        except ValueError:
            print("Insira um valor inteiro!!")
            continue
    return encontrar_divisores(n)


if __name__ == "__main__":
    main()
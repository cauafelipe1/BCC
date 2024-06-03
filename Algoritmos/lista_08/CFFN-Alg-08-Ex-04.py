# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 04

'''Escreva uma nova versão da sua função
recursiva do exercício 2 (Fibonacci) utilizando a técnica de memorização de resultado para
melhorar desempenho e consumo de memória.'''

def fibonacci(n, memorizados={}):
    if n in memorizados:
        return memorizados[n]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    memorizados[n] = fibonacci(n - 1, memorizados) + fibonacci(n - 2, memorizados)
    return memorizados[n]

def main():
    n = int(input("Insira um valor inteiro positivo: "))
    return print(f"Fibonacci({n}) = {fibonacci(n)}")

if __name__ == "__main__":
    main()
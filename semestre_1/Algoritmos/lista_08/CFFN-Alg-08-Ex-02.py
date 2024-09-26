# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 02

'''A série de Fibonacci é uma sequencia de Fn números inteiros no
qual um termo é definido pela soma dos dois termos anteriores. Os primeiros termos Fi da
sequencia são 0, 1, 1, 2, 3, 5, 8, 13, etc. Portanto, o enésimo termo da sequencia é definido
por Fn = Fn-1 + Fn-2, sendo F0 = 0 e F1 = 1. Escreva uma função Python recursiva que
recebe como parâmetro um valor inteiro n, e retorna o enésimo termo da sequencia de
Fibonacci.'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = int(input("Insira um valor inteiro positivo: "))
    return print(f"Fibonacci({n}) = {fibonacci(n)}")

if __name__ == "__main__":
    main()
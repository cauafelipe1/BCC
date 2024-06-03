# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 01

'''Implementa uma função recursiva para calcular o fatorial de um número inteiro
positivo. O fatorial é denotado pelo símbolo de exclamação “!” e é definido da seguinte forma:
1! = 1 e n! = n * (n - 1)!, para n > 1.'''

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n-1)

def main():
    n = int(input("Insira um valor inteiro: "))
    return print(f"{n}! = {fatorial(n)}")

if __name__ == "__main__":
    main()
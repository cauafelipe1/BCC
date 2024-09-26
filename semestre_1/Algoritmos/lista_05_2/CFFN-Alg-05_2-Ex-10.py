# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 10

'''Um número inteiro positivo é primo se e somente se ele for divisível apenas
por 1 e por ele mesmo. Escreva uma função que recebe um valor inteiro positivo e retorna
True se ele for primo ou False se ele não for. Escreva um programa principal que leia um
número inteiro do usuário e exiba uma mensagem indicando se ele é ou não primo.'''
from math import sqrt

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def main():
    n = int(input("Insira um número inteiro positivo: "))
    if isPrime(n):
        x = print("É primo!")
    else:
        x = print("Não é primo!")
    return x

if __name__ == "__main__":
    main()
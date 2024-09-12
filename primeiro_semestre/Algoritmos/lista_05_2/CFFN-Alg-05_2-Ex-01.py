# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 01

'''Hipotenusa. Escreva uma função que recebe como parâmetros os comprimentos dos dois
lados menores de um triângulo retângulo. A função deve retornar como resultado o
comprimento da hipotenusa, calculado com o Teorema de Pitágoras. Inclua um programa
principal (função main) que solicite ao usuário os comprimentos dos lados, utilize sua função
para calcular a hipotenusa e imprima o resultado.'''
from math import sqrt

def hipotenusa(lado_1, lado_2):
    hip = lado_1**2 + lado_2**2
    hip = sqrt(hip)
    return hip

def main():
    lado_1 = int(input("Insira o valor do primeiro lado: "))
    lado_2 = int(input("Insira o valor do segundo lado: "))
    x = print(f"Dado os valores {lado_1} e {lado_2}, temos:\nhipotenusa² = {lado_1}² + {lado_2}²\nhipotenusa = {hipotenusa(lado_1, lado_2)}")
    return x

if __name__ == "__main__":
    main()
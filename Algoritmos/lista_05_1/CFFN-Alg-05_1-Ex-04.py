# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 04

'''Escreva uma função Python chamada quadrado(x), que vai receber receber um número real
x, e vai retornar o valor de x ao quadrado.'''

x = float(input("Insira o valor de x: "))

def quadrado(x):
    print(f"{x}² = {x} * {x} =", x**2)

quadrado(x)
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 08

'''Faça uma função que recebe um número inteiro n>0 e devolve o número de dígitos de n.'''

n = int(input("Insira um valor inteiro de n (sendo n > 0): "))

def digitos(n):
    print(f"O número {n} possui {len(str(n))} digitos!")

digitos(n)
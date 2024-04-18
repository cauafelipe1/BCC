# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 11

'''Usando a função do item anterior, faça um programa que lê dois inteiros positivos a e b e
responda se a é permutação de b.
Um número a é dito permutação de um número b se os dígitos de a formam uma permutação
dos dígitos de b.
Exemplo: 5412434 é uma permutação de 4321445, mas não é uma permutação de 4312455.
Obs.: Considere que o dígito 0 (zero) não aparece nos números.'''

print("(Considere a e b desprovidos do digito 0)")
a = int(input("Insira um valor para a: "))
b = int(input("Insira um valor para b: "))



def conta_digitos(a, b):
    i = 0

    for digito in str(a):
        if int(digito) == b:
            i += 1
    return i

def verifica_permutacao(a, b):
    
    if len(str(a)) != len(str(b)):
        return False
    
    for digito in range(1, 10):  
        vezes_em_a = conta_digitos(a, digito)
        vezes_em_b = conta_digitos(b, digito)

        if vezes_em_a != vezes_em_b:
            return False
    
    return True

if verifica_permutacao(a, b):
    print(f"{a} é permutação de {b}")
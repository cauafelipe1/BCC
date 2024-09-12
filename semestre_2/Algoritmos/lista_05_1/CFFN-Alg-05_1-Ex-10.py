# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 10

'''Faça uma função chamada conta_digitos(n, d) que dados um inteiro n e um inteiro d, 0 < d
<= 9, devolve quantas vezes o dígito d aparece em n.'''

n = int(input("Insira um valor para n: "))
d = int(input("Insira um valor para d (sendo 0 < d <=9): "))
def conta_digitos(n, d):
    i = 0

    for digito in str(n):
        if int(digito) == d:
            i += 1
    return i

print(f"O digito {d} aparece {conta_digitos(n, d)} vezes em {n}!")
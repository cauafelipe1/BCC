# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 11

'''Proposta: Parte 2 - Comando WHILE - faça todos os exercícios desta parte com "while":
11. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.
A = 1 - 1/2 + 1/3 - 1/4 + 1/5 ... ± 1/n'''

print("=-"*30, "\n[Valor de A em relação à fórmula da proposta]")

n = int(input("Insira o valor de n: "))
i = 2
A = 1

while i <= n:
    if i % 2 == 0:
        A -= 1/i
    else:
        A += 1/i
    i += 1

print(f"\nPela fórmula indicada na proposta, temos que: \nA = {A}")
print("=-"*30)
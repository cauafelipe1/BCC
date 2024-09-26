# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 10

'''Proposta: Parte 2 - Comando WHILE - faça todos os exercícios desta parte com "while":
10. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.
A = 1 + 1/3 + 1/5 + ... 1/(2*N-1)'''

print("=-"*30, "\n[Valor de A em relação à fórmula da proposta]")

n = int(input("Insira o valor de n: "))
i = 3
A = 1

while i <= (2 * n - 1):
    A += 1/i
    i += 2

print(f"\nPela fórmula indicada na proposta, temos que: \nA = {A}")
print("=-"*30)
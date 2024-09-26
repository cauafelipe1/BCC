# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 05

'''Proposta: Parte 1 - Comando FOR - faça todos os exercícios desta parte com comando “for" e função
“range":
Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.
A = N + (N-1)/2 + (N-2)/3 ... 1/N'''

print("=-"*30, "\n[Valor de A em relação à fórmula da proposta]")

n = int(input("Insira um valor inteiro: "))
A = n

for i in range(1, n):
    A += (n-i)/(i+1)

print(f"\nPela fórmula indicada na proposta, temos que: \nA = {A}")
print("=-"*30)
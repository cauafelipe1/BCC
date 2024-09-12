# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 04

'''Proposta: Parte 1 - Comando FOR - faça todos os exercícios desta parte com comando “for" e função
“range":
Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um
número inteiro positivo fornecido pelo usuário.
A = 1 + 1/2 + 1/3 + ... 1/n'''

print("=-"*30, "\n[Valor de A em relação à fórmula da proposta]")

n = int(input("Insira um valor inteiro: "))

A = 1
for i in range(2, n+1):
    A += 1/i
    
print(f"\nPela fórmula indicada na proposta, temos que: \nA = {A}")
print("=-"*30)
    

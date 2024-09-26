# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 07

'''Proposta: Escreva um programa Python que receba do
usuário um número inteiro positivo n e então exiba a soma de todos os números inteiros de 1 a
n. Tal soma pode ser computada usando a seguinte fórmula:
soma = (n)(n+1)/2'''

n = int(input("Digite um número inteiro positivo: "))

# método utilizando laço de repetição (fiz porque não tinha entendido direito a fórmula)
'''soma = 0
for i in range(0, n+1):
    soma += i

print(f"O resultado da soma de todos os números positivos do 1 ao {n} é igual a: {soma}")'''

# método utilizando a fórmula
soma = (n*(n+1)/2)

print(f"O resultado da soma de todos os números positivos do 1 ao {n} é igual a: {int(soma)}")
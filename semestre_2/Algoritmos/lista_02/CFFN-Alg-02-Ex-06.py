# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 06

'''Proposta: Desenvolva um programa que obtenha do usuário um
número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1).'''

print("=-"*30, "\nSoma dos algarismos de um número de 4 digitos")

n = int(input("Insira um número inteiro de 4 digitos: "))

digito_1 = n//1000
resto = n%1000

digito_2 = resto//100
resto = n%100

digito_3 = resto//10
resto = n%10

digito_4 = resto
soma = digito_1 + digito_2 + digito_3 + digito_4
print(f"A soma dos 4 digitos do número {n} é igual a {soma}!")
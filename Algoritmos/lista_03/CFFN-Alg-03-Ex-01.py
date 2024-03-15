# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 01

'''Proposta: Escreva um programa Python que recebe do usuário um número inteiro. Seu
programa deve então exibir uma mensagem indicando se o número fornecido é par ou ímpar.'''

print("=-"*30, "\n[Par ou impar?]")
x = int(input("\nDigite um valor inteiro: "))

if x % 2 == 0:
    print(f"O valor de {x} fornecido pelo usuário é um número par!")

else:
    print(f"O valor de {x} fornecido pelo usuário é um número impar!")

print("=-"*30)
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 10

'''Proposta: 10. Aritmética. Escreva um programa Python que leia do usuário dois inteiros a e b. Seu
programa deve computar e exibir o seguinte:
• A soma de a e b
• A diferença quando b é subtraído de a
• O produto de a por b
• O quociente quando a é dividido por b
• O resto quando a é dividido por b
• O resultado de log₁₀a
• O resultado de aᵇ'''

from math import log10

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

soma = a + b
diferenca = a - b
produto = a * b
quociente_divisao = a / b
resto_divisao = a % b
logaritmo_10 = (log10(a))
potenciacao = a**b

print("=-"*30)
print(f"Resultados aritméticos envolvendo os valores {a} e {b}:\n")
print(f"soma: {a} + {b} = {soma}")
print(f"subtração: {a} - {b} = {diferenca}")
print(f"multiplicação: {a} * {b} = {produto}")
print(f"quociente de divisão: {a} / {b} = {quociente_divisao}")
print(f"log₁₀{a}: {logaritmo_10}")
print(f"potenciação: {a} ** {b} = {potenciacao}")
print("=-"*30)

# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 13

'''Proposta: A área de um triângulo pode ser calculada pela fórmula abaixo, onde b
é o comprimento de sua base e h é o comprimento de sua altura.
area = (b * h)/2
Escreva um programa Python que permita que o usuário forneça os dados de b e h de um
triângulo, e calcule e exiba o valor de sua área.'''

print("=-"*30, "\nCálculo da área de um triângulo")

b = float(input("Insira o valor da base do triângulo (em metros): "))
h = float(input("Insira o valor da base do triângulo (em metros): "))

area = (b*h)/2

print(f"\nA área do triângulo cujos valores foram inseridos é de {area}m²!")
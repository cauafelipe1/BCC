# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 14

'''Proposta: No exercício anterior você criou um programa para
calcular a área de um triângulo dados sua base e sua altura. Entretanto, também é possível
calcular a área de um triângulo se forem conhecidos os comprimentos de seus 3 lados. Seja
, , e os comprimentos dos três lados.
seja l = (l1 + l2 + l3)/2
Então, a área do triângulo pode ser calculada com a seguinte fórmula:
area = √(l * (l - l1) * (l - l2) * (l - l3))
Escreva um programa Python que leia os comprimentos de 3 lados de um triângulo, calcule e
exiba sua área.'''

from math import sqrt
print("=-"*30, "\nCálculo da área de um triângulo (novamente)")
print("Dessa vez, iremos calcular a área de uma maneira diferente!")
print("Vamos calcular utilizando o comprimento de seus três lados!")

l1 = float(input("Insira o valor do primeiro lado do triângulo (em metros): "))
l2 = float(input("Insira o valor do segundo lado do triângulo (em metros): "))
l3 = float(input("Insira o valor do terceiro lado do triângulo (em metros): "))

l = (l1+l2+l3)/2

area = sqrt(l * (l - l1) * (l - l2) * (l - l3))
print(l, area)
print(f"\nA área do triângulo cujos valores foram inseridos é de {area}m²!")
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 15

'''Proposta: Um polígono é regular se seus lados são todos do mesmo
tamanho e os ângulos entre lados adjacentes são todos iguais. A área de um polígono regular
pode ser calculada pela fórmula abaixo onde l é o comprimento de um lado e n é o número de
lados:
area = (n * l²)/(4 * tan(𝞹/n))
Escreva um programa Python que obtenha do usuário os valores de l e n, e então calcule e
exiba a área do polígono regular correspondente.'''

from math import tan, pi

print("=-"*30, "\nCálculo da área de um polígono regular")

l = float(input("Insira o valor do comprimento de um lado do polígono (em metros): "))
n = int(input("Insira o número de lados do polígono: "))

area = (n * l ** 2)/ 4 * tan(pi/n)

print(f"\nA área do polígono regular é de {area}m².")
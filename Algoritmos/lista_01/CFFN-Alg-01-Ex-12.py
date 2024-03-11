# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 12

'''Proposta: Escreva um programa Python que começa lendo o valor de um raio r,
fornecido pelo usuário. O programa deve continuar calculando e exibindo a área de um círculo
de raio r, e o volume de uma esfera de raio r. Utilize a constante pi do módulo math nos seus
cálculos.
Observação: a área e o volume são dados por:
area = 𝞹r²
volume = 4/3𝞹r³'''

from math import pi 
r = float(input("Digite o valor de raio para r (em metros): "))

area = pi * (r**2)
volume = 4/3 * pi * r**3

print(f"A área de um circulo de raio r é de {area}m²")
print(f"O volume de uma esfera de raio r é de {volume}m³")
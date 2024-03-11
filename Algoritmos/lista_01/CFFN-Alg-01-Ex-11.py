# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 11

'''Proposta: A terra é curva (a não ser para os terraplanistas!) e
a distância entre graus de longitude (leste-oeste) varia conforme a latitude (norte-sul). Com
isso, encontrar a distância entre dois pontos na superfície da terra é mais complicado do
simplesmente usar o Teorema de Pitágoras no plano. Seja (t1, g1) as latitudes e
(t2, g2) as longitudes de dois pontos na superfície da terra. A distância em quilômetros entre estes dois
pontos ao longo da superfície da terra é dada por:
distancia = 6371.01 * arccos(sen(t1) * sen(t2) + cos(t1) * cos(t2) * cos(g1-g2))
Crie um programa Python que receba a latitude e a longitude de dois pontos na Terra em
graus, calcule e exiba a distância entre eles em quilômetros ao longo da superfície.'''

from math import acos, sin, cos, radians

print("=-"*30, "\nEntão você quer saber a distância entre dois pontos na terra?")
print("Ótimo! apenas me passe algumas informações...")
print("\nInforme (em graus):")

t1 = (float(input("a latitude do primeiro ponto: ")))
g1 = (float(input("a longitude do primeiro ponto: ")))

t2 = (float(input("Informe a latitude do segundo ponto: ")))
g2 = (float(input("Informe a longitude do segundo ponto: ")))

# verificacao dos valores inseridos
if (-90 <= t1 <= 90) and (-90 <= t2 <= 90) and (-180 <= g1 <= 180) and (-180 <= g2 <= 180):
    t1, g1, t2, g2 = radians(t1), radians(g1), radians(t2), radians(g2)
    distancia = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))
    print(f"\nA distância entre os dois pontos registrado é de aproximadamente {round(distancia, 3)}km!")

else:
    print("\nParece que você inseriu valores inválidos...")
    print("Lembre-se, latitude varia de -90° a 90° e longitude de -180° a 180°!")

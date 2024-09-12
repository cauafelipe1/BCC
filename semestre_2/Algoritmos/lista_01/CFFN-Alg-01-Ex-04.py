# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 04

'''Proposta: Crie um programa Python que leia as dimensões de um terreno em
metros (largura e profundidade), e exiba o resultado em hectares.'''

largura = int(input("digite quantos metros de largura tem o terreno: "))
profundidade = int(input("digite quantos metros profundidade tem o terreno: "))

area = largura * profundidade
area_para_hectares = area/10000

print(f"O terreno informado possui as dimensões de {area_para_hectares} hectares.")
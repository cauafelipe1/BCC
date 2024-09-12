# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 03

'''Proposta: Escreva um programa Python que peça para o usuário os comprimentos
da largura e profundidade de uma sala. Após a leitura dos valores, seu programa deve exibir a
área da sala. A largura e a profundidade devem ser números reais. Inclua as unidades nas
mensagens de entrada e saída (metros e metros quadrados).'''

largura = int(input("digite quantos metros de largura tem a sala: "))
profundidade = int(input("digite quantos metros profundidade tem a sala: "))

area = largura * profundidade

print(f"A área da sala é de {area}m².")
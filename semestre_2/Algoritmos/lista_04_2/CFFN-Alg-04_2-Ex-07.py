# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 07

'''Proposta: O valor aproximado de pode ser calculado pela série infinita
apresentada abaixo:
Escreva um programa Python que exiba 15 aproximações de . A primeira aproximação deve
π  ≈ 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) 
ter apenas o primeiro termo da série (ou seja, o valor resultante vai ser somente 3). Cada nova
aproximação de mostrada pelo seu programa deve incluir mais um termo da série, sendo
cada vez uma aproximação mais precisa do que a anterior.'''

pi = 3

i = 0

while i < 15:
    x = (i + 1) * 2
    formula = 4 / (x * (x + 1) * (x + 2))

    if i % 2 == 0:
        pi += formula
    else:
        pi -= formula
    i += 1

print(f"Após {i} aproximações: π  ≈ {pi}")
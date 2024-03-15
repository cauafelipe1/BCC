# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 04


'''Proposta: Crie um programa Python que determina e exibe o nome de um polígono
regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar
polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o
programa deve exibir uma mensagem de erro.'''

print("=-"*30, "\n[Polígono regular]")

lado = int(input("Insira a quantidade de lados de um polígono regular (3 a 10): "))


if lado == 3:
    print(f"O polígono regular que possui {lado} lados é um triângulo!")

elif lado == 4:
    print(f"O polígono regular que possui {lado} lados é um quadrado!")

elif lado == 5:
    print(f"O polígono regular que possui {lado} lados é um pentágono!")

elif lado == 6:
    print(f"O polígono regular que possui {lado} lados é um hexágono!")

elif lado == 7:
    print(f"O polígono regular que possui {lado} lados é um heptágono!")

elif lado == 8:
    print(f"O polígono regular que possui {lado} lados é um octógono!")    

elif lado == 9:
    print(f"O polígono regular que possui {lado} lados é um eneágono!")

elif lado == 10:
    print(f"O polígono regular que possui {lado} lados é um decágono!")

else:
    print(f"O valor de lados inserido não é válido para este programa... Por favor insira um valor de 3 a 10.")

print("=-"*30)

'''
Poderia também ser resolvido da seguinte forma:

nomes = ["triângulo", "quadrado", "pentágono", "hexágono", "heptágono", "octógono", "eneágono", "decágono"]
print(f"O polígono regular que possui {lado} lados é um {nomes[lado-3]}!")'''

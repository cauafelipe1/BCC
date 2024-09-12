# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 04

'''Proposta: Crie um programa Python para calcular o perímetro de um
polígono sendo fornecidas as coordenadas x e y de cada um de seus vértices. Inicie lendo x e
y do primeiro vértice. Depois disso continue lendo x e y dos próximos vértices até que o
usuário entre com uma linha em branco para o valor da coordenada x (ou seja, quando ele
digitar “Enter" ou “Return" sem fornecer um valor). Cada vez que você ler as coordenadas de
um novo vértice, você deve calcular a distância em relação ao vértice anterior e acrescentá-la
ao valor do perímetro. A figura abaixo ilustra como se calcula a distância entre dois pontos
sendo dadas suas coordenadas x e y.
Quando o usuário entrar com a linha em branco na coordenada x, seu programa deve
adicionar ao perímetro a distância do último ponto até o primeiro. Depois disso, deve exibir o
valor do perímetro.'''
from math import sqrt

lista_x = []
lista_y = []
d = 0

while True:
    try:
        x = input("Digite a coordenada x de um ponto (enter para sair): ")
        if x == "":
            break
        y = input("Digite a coordenada y de um ponto:")
        lista_x.append(float(x))
        lista_y.append(float(y))

        if len(lista_y) >= 2:
            x = float(x)
            y = float(y)

            d += sqrt((y - lista_y[-2])**2 + (x - lista_x[-2])**2)

    
    except ValueError:
        print("Digite um valor válido!!")
        continue


print(f"O perímetro deste polígono é igual a {d}")


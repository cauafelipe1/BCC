# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 02

'''Em uma determinada cidade, as tarifas de táxi consistem em um valor inicial de
R$ 4,00 mais R$ 0,25 a cada 140 metros percorridos. Escreva uma função que recebe como
seu único parâmetro a distância percorrida em quilômetros, e retorna como seu único
resultado o valor total da corrida. Escreva um programa principal que demonstre o
funcionamento de sua função.'''

def tarifa(distancia):
    tarifa = 4.00
    distancia = distancia*1000
    adicional = (distancia/140) * 0.25
    tarifa += adicional
    return round(tarifa, 2)

def main():
    distancia = float(input("Digite a distância percorrida (em km): "))
    x = print(f"A corrida na distância de {distancia}km, totalizou um valor de R${tarifa(distancia)}!")
    return x

if __name__ == "__main__":
    main()
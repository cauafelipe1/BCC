# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 09

'''Proposta: Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não
em uma variável do tipo data, crie um programa Python que leia uma data no formato
DDMMAA e imprima essa data no formato AAMMDD, onde:
• a letra D corresponde a dois algarismos representando o dia;
• a letra M corresponde a dois algarismos representando o mês;
• a letra A corresponde aos dois últimos algarismos representando o ano.
Por exemplo: a data 110618 (11 de junho de 2018), deve ser impressa como 180611'''

print("=-"*30, "\nData inversa")

dma = int(input("Insira uma data em um valor inteiro (utilize o formado DDMMAA): "))

dia = dma//10000
resto = dma%10000

mes = resto//100
resto = dma%100

ano = resto

amd = ano * 10000 + mes * 100 + dia 

print(f"A data no formato DDMMAA {dma} invertida é equivalente a {amd} no formato AAMMDD.")
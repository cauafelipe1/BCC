# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 04

'''Proposta: Crie um programa que obtém 3 números inteiros do usuário e os
exibe de forma ordenada do menor para o maior. Use as funções min e max para encontrar o
menor valor e o maior valor. Dica: o valor do meio pode ser obtido pela soma dos três valores,
subtraída do maior e do menor.'''

print("=-"*30, "\nOrdenando três números inteiros")

valor_1 = int(input("Insira o primeiro valor: "))
valor_2 = int(input("Insira o segundo valor: "))
valor_3 = int(input("Insira o terceiro valor: "))

valores = [valor_1, valor_2, valor_3]
valor_min = min(valores)
valor_max = max(valores)
valor_med = (valor_1 + valor_2 + valor_3)- valor_min - valor_max

print(f"Os valores {valor_1}, {valor_2} e {valor_3} podem ser ordenados da seguinte forma:")
print(f"Mínimo: {valor_min}\nMédio: {valor_med}\nMáximo: {valor_max}")
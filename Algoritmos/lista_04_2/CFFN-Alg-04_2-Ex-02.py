# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 02

'''Proposta: Uma loja está oferecendo uma liquidação com descontos de 60% em
uma variedade de produtos em final de estoque. O vendedor gostaria de ajudar seus clientes a
determinar o preço reduzido (com desconto) de seus produtos. Ele quer criar uma tabela que
mostra os preços originais e os preços após o desconto ser aplicado. Escreva um programa
Python usando laço de repetição que gere esta tabela mostrando o preço original, o valor de
desconto e o novo valor com desconto aplicado para produtos com os seguintes valores:
R$ 4.95, R$ 9.95, R$ 14.95, R$ 19.95 e R$ 24.95. Certifique-se que todos os valores são
mostrados com duas casas decimais.'''

print("[Tabela de preços]")
print("Confira abaixo a tabela contendo os produtos com DESCONTO de 60% aplicado!")

print("=-"*20)
print("Preço original\t\tPreço final")

for i in range(4, 24, 5):
    produto = i + 0.95
    desconto = produto * 0.4
    print(f"R${produto}\t\t\tR${round(desconto, 2)}")

print("=-"*20)
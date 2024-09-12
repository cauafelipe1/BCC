# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 05

'''Proposta: Alguns estabelecimentos retornam créditos em troca de reciclagem
de recipientes. Em um estabelecimento em particular, vasilhames de um litro ou menos geram
crédito de 10 centavos e vasilhames de mais de um litro geram créditos de 25 centavos.
Escreva um programa que leia do teclado a quantidade destes dois tipos de vasilhames a
serem reciclados. A seguir o programa deve calcular e exibir o valor total dos créditos
referentes ao retorno dos vasilhames. Pesquise sobre como formatar a saída para que a
resposta seja exibida com sinal de reais R$ e exatamente duas casas decimais.'''

abaixo_1_litro = int(input("Digite quantos vasilhames de 1 litro ou menos serão reciclados: "))
acima_1_litro = int(input("Digite quantos vasilhames de mais de 1 litro serão reciclados: "))

credito_1 = abaixo_1_litro * 0.10
credito_2 = acima_1_litro * 0.25

total = credito_1 + credito_2

print(f"O retorno dos vasilhames registrados rendeu um total de R${round(total, 2)}")

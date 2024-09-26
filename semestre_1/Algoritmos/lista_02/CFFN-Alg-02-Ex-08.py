# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 08

'''Proposta: Dado um número de três algarismos N = CDU
(onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das
unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é,
M=UDC. Faça um programa Python para gerar e imprimir M a partir de N (p.ex.:N=123
->M=321).'''

print("=-"*30, "\nCentena, dezena e unidade de forma inversa")

n = int(input("Insira um valor inteiro de três digitos: "))

c = n//100
resto = n%100 
d = resto//10
resto = n%10
u = resto

m = c + (d*10) + (resto*100)

print(f"O valor de {n} ao contrário será {m}!")
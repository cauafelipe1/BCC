# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 07

'''Proposta: Dado um número de três algarismos N = CDU (onde C é o
algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um
programa Python que receba do usuário o número inteiro N, e imprima separadamente a
centena, a dezena e a unidade.'''
print("=-"*30, "\nCentena, unidade e d")

n = int(input("Insira um valor inteiro de três digitos: "))

c = n//100
resto = n%100
d = resto//10
resto = n%10
u = resto

print(f"Podemos ler o valor {n} também como {c} centena(s), {d} dezena(s) e {u} unidade(s).")
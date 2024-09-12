# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 09

'''Proposta: Faça de conta que você acabou de abrir uma conta de investimento que
rende 12% de juros ao ano. Os juros que você ganha são pagos ao final do ano. Escreva um
programa que começa lendo do usuário o valor inicial depositado na conta. Em seguida, o
programa deve computar e exibir o saldo da conta de investimento após 1, 2 e 3 anos. Exiba
cada valor com exatamente 2 casas decimais.'''

saldo = float(input("Digite o valor inicial depositado em sua conta: "))

for i in range(1, 4):
    saldo += saldo*0.12
    print(f"Após o {i}° ano, o valor de sua conta será de R${round(saldo, 2)}")
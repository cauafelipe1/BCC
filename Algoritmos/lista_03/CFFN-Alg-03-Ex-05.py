# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 05

'''Proposta: A quantidade de dias de um mês pode variar de 28 a 31
dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de 
um mês (como uma string). Então seu programa deve exibir uma mensagem informando a
quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar
“28 ou 29 dias.'''

print("=-"*30, "\n[Nome do mês e número de dias]")

# meses com 30 dias
meses_30 = ["abril", "junho", "setembro", "novembro"]
# meses com 31 dias
meses_31 = ["janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"]

mes = input("Digite o nome de um mês: ")
mes = mes.lower()
if mes in meses_30:
    print(f"O mês de {mes} possui 30 dias.")

elif mes in meses_31:
    print(f"O mês de {mes} possui 31 dias.")

elif mes == "fevereiro":
    print(f"O mês de {mes} possui 28 ou 29 dias.")
else:
    print("O valor inserido não é o nome de um mês.")

print("=-"*30)

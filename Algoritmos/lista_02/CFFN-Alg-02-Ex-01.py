# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 01

'''Proposta: Crie um programa Python que leia do usuário um valor de intervalo de 
tempo expresso em número de dias, horas, minutos e segundos. O programa deve computar e
exibir a quantidade total de segundos deste intervalo de tempo informado.'''

print("=-"*30, "\nConversão de Unidades de tempo (conversão para segundos)")
data_final = []
tempo = ["dias", "horas", "minutos", "segundos"]

for i in range(len(tempo)):
    t = int(input(f"Digite o valor equivalente a quantidade de {tempo[i]}: "))
    data_final.append(t)

dias = int(data_final[0])
horas = int(data_final[1])
minutos = int(data_final[2])
segundos = int(data_final[3])

if (0 <= dias) and (0 <= horas <= 24) and (0 <= minutos <= 60) and (0 <= segundos <=60):
    segundos_totais = (dias*86400) + (horas*3600) + (minutos*60) + (segundos*60)
    print(f"\nA quantidade de segundos no intervalo de tempo de {dias} dia(s) {horas} hora(s) {minutos} minuto(s) e {segundos} segundo(s) equivale a {segundos_totais} segundos.")

else:
    print("Algum dos valores inseridos é inválido.")
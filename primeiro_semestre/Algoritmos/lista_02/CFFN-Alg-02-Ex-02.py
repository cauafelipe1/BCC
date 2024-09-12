# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 02

'''Proposta: Neste exercício você deve fazer o processo inverso do
exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de
tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na
forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos
respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com
dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10.'''

print("=-"*30, "\nConversão de Unidades de tempo (conversão para D:HH:MM:SS)")

segundos = int(input("Insira o valor do intervalo de tempo desejado expresso em segundos: "))

dias = segundos//86400
resto = segundos%86400
horas = resto//3600
resto = segundos%3600
minutos = resto//60
resto = segundos%60

if dias < 10:
    dias = "0" + str(dias)
if horas < 10:
    horas = "0" + str(horas)
if minutos < 10:
    minutos = "0" + str(minutos)
if resto < 10:
    resto = "0" + str(resto)
print(f"O valor de {segundos} segundos é equivalente a {dias} dias {horas} horas, {minutos} minutos e {resto} segundos.")


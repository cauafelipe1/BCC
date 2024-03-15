# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 09

'''Proposta: A tabela abaixo mostra os feriados nacionais brasileiros que caem sempre no
mesmo dia (em oposição aos feriados variáveis como carnaval e corpus christi).

[Feriado]                             [Data]
Confraternização universal            1o. de janeiro
Tiradentes                            21 de abril
Dia do trabalho                       1o. de maio
Independência do Brasil               7 de setembro
Nossa Senhora Aparecida               12 de outubro
Finados                               2 de novembro
Proclamação da República              15 de novembro
Natal                                 25 de dezembro

Escreva um programa Python que leia do usuário o mês e o dia de uma determinada data. Se
o mês e o dia corresponderem a uma das datas da tabela acima, seu programa deve exibir o
nome do feriado. Caso contrário o programa deve informar que o dia e o mês informados não
correspondem a um feriado nacional.'''

print("=-"*30, "\n[Data de Feriado]")

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
feriados = ["Confraternização universal", "Tiradentes", "Dia do trabalho", "Independência do Brasil", "Nossa Senhora Aparecida", "Finados", "Proclamação da República", "Natal"]

dia = int(input("Digite o dia da sua data: "))
mes = input("Digite o mês da sua data: ")

mes = mes.lower()

if (1 <= dia <= 31) and mes in meses:
    if (dia == 1) and (mes == "janeiro"):
        print(f"O dia {dia} de {mes} corresponde ao feriado de {feriados[0]}!")

    elif (dia == 21) and (mes == "abril"):
        print(f"O dia {dia} de {mes} corresponde ao feriado de {feriados[1]}!")

    elif (dia == 1) and (mes == "maio"):
        print(f"O dia {dia} de {mes} corresponde ao feriado do {feriados[2]}!")

    elif (dia == 7) and (mes == "setembro"):
        print(f"O dia {dia} de {mes} corresponde ao feriado da {feriados[3]}!")

    elif (dia == 12) and (mes == "outubro"):
        print(f"O dia {dia} de {mes} corresponde ao feriado de {feriados[4]}!")

    elif (dia == 2) and (mes == "novembro"):
        print(f"O dia {dia} de {mes} corresponde ao feriado de {feriados[5]}!")

    elif (dia == 15) and (mes == "novembro"):
        print(f"O dia {dia} de {mes} corresponde ao feriado da {feriados[6]}!")

    elif (dia == 25) and (mes == "dezembro"):
        print(f"O dia {dia} de {mes} corresponde ao feriado de {feriados[7]}!")
    
    else:
        print(f"O dia {dia} de {mes} não corresponde a um feriado!")

else:
    print(f"O dia {dia} e o {mes} não correspondem a uma data válida.")
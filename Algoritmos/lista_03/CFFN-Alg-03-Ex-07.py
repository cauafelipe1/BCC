# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 07

'''Proposta: A tabela abaixo mostra uma lista de volume sonoro em decibéis para
diferentes tipos comuns de barulhos.

[Barulho]               [Nível de decibéis (dB)]
Britadeira                        130
Cortador de grama                 106
Despertador                       70
Sala silenciosa                   40

Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o
usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve
exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado.
Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa
deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar
quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o
usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor.'''

print("=-"*30, "\n[Níveis de barulho.]")

tabela = ["britadeira (130dB)", "cortador de grama (106dB)", "despertado (70dB)", "sala silenciosa (40dB)"]

barulho = float(input("Informe em decibéis (dB) um nível de volume: "))


if barulho >= 0:
    if barulho < 40:
        print(f"O nível de barulho de {barulho} decibéis é menor que o de uma {tabela[3]}.")

    elif barulho == 40:
        print(f"O nível de barulho de {barulho} decibéis é igual ao de uma {tabela[3]}.")

    elif 40 < barulho < 70:
        print(f"O nível de barulho de {barulho} decibéis está entre o de uma {tabela[3]} e de um {tabela[2]}.")

    elif barulho == 70:
        print(f"O nível de barulho de {barulho} decibéis é igual ao de um {tabela[2]}.")

    elif 70 < barulho < 106:
        print(f"O nível de barulho de {barulho} decibéis está entre o de um {tabela[2]} e de um {tabela[1]}.")

    elif barulho == 106:
        print(f"O nível de barulho de {barulho} decibéis é igual ao de um {tabela[1]}.")

    elif 106 < barulho < 130:
        print(f"O nível de barulho de {barulho} decibéis está entre o de um {tabela[1]} e de uma {tabela[0]}.")

    elif barulho == 130:
        print(f"O nível de barulho de {barulho} decibéis é igual ao de uma {tabela[0]}.")

    elif barulho > 130:
        print(f"O nível de barulho de {barulho} decibéis é maior que o de uma {tabela[0]}.")
else:
    print("O valor de decibéis inserido não é válido.")

print("=-"*30)
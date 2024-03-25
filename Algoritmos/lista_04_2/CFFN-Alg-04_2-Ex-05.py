# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 05

'''Proposta: Um determinado zoológico estipula o valor da entrada baseado na idade
do visitante. Visitantes com até dois anos de idade não precisam pagar. Crianças entre 3 e 12
anos de idade pagam R$ 14.00. Idosos com 65 anos ou mais pagam R$ 18.00. Todos os
demais pagam R$ 23.00. Crie um programa que inicia lendo as idades, uma por uma, de um
grupo de pessoas. O usuário deve entrar uma linha em branco para indicar que não há mais
pessoas no grupo. Depois disso, seu programa deve exibir uma mensagem informando o
preço total de todas as entradas para o grupo. O valor deve ser exibido com duas casas
decimais.'''
entrada = 0
i = 1
while True:
    try:
        idade = input(f"Digite a idade da {i}ª pessoa: ")
        if idade == "":
            break
        else:
            idade = int(idade)

            if 0 < idade < 3:
                pass
            elif 3 <= idade <= 12:
                entrada += 14

            elif 13 <= idade < 65:
                entrada += 23

            elif idade >= 65:
                entrada += 18
            else:
                print("Insira uma idade válida!!")
                continue
            i += 1
    except ValueError:
        print("Insira um valor válido!!")
        continue

# não é necessário o uso do método round() pois todos os valores são redondos
print(f"O total a ser pago será R${entrada}.00")
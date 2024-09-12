# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 02

'''Proposta: É comum dizermos que um ano de um cachorro equivale a 7 anos de um
humano. Porém, essa conversão simples erra em não reconhecer que cachorros se tornam
adultos em cerca de 2 anos. Assim, algumas pessoas acreditam que é melhor contar os dois
primeiros anos como 10.5 anos caninos, e os anos restantes como 4 anos caninos cada.
Escreva um programa que implemente a conversão de anos cronológicos para anos caninos.
Certifique-se que seu programa funciona tanto para conversão de idades até 2 anos
cronológicos e também maiores que 2 anos cronológicos. Seu programa deve exibir uma
mensagem de erro se o usuário entrar com um número negativo.'''

print("=-"*30, "\n[Conversão de anos cronológicos para anos caninos]")

idade = int(input("Digite a idade cronológica que deseja converter para canina: "))

if idade >= 2:
    idade -= 2
    i = 10.5
    i += idade * 4
    idade += 2
    print(f"A idade cronológica de {idade} anos convertida para idade canina é de {i} anos!")
    print(f"Ou seja, tendo {idade} anos de idade, seu cachorro terá o equivalente a {i} anos de um humano.") 

elif (0 < idade < 2):
    i = 10.5/2
    print(f"A idade cronológica de {idade} ano convertida para idade canina é de {i} anos!")
    print(f"Ou seja, tendo {idade} ano de idade, seu cachorro terá o equivalente a {i} anos de um humano.")    

else:
    if idade < 0:
        print(f"É impossível calcular a idade canina, pois o valor inserido {idade} é negativo.")
    elif idade == 0:
        print(f"É impossível calcular a idade canina, pois o valor inserido {idade} é zero.")
    else: 
        print(f"É impossível calcular a idade canina, pois o valor inserido {idade} é inválido.")


# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 08

'''Proposta: Uma loja online oferece aos seus clientes dois tipos de
produto: bugigangas e quinquilharias. Cada bugiganga pesa 75 gramas e cada quinquilharia
pesa 112 gramas. Faça um programa Python que leia a quantidade de bugigangas e a
quantidade de quinquilharias de um pedido do usuário. A seguir, seu programa deve calcular e
exibir o peso total do pedido.'''

bugigangas = (int(input("Quantas bugigangas o usuário deseja? ")))*75
quinquilharias = (int(input("Quantas quinquilharias o usuário deseja? ")))*112

soma = bugigangas + quinquilharias

if soma >= 1000:
    print(f"O peso total do pedido é de {round(soma/1000, 3)}kg")
else:
    print(f"O peso total do pedido é de {soma} gramas")
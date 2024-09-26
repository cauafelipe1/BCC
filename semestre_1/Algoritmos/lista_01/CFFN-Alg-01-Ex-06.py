# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-01
# Exercício: 06

'''Proposta: Imagine que você foi almoçar num restaurante, e pediu uma refeição com
um suco, um prato principal e uma sobremesa. Cada um desses itens tem um preço unitário.
Ao final, o valor da conta deve ser a soma do valor dos itens consumidos, acrescida de 10%
de taxa de serviço. Faça um programa Python para receber estes dados do usuário e calcular
o valor total da conta deste tipo de refeição. Exiba a resposta com os mesmos critérios de
formatação da questão anterior (R$ e 2 casas decimais).'''

suco = float(input("Informe o valor do suco: "))
prato_principal = float(input("Informe o valor do prato principal: "))
sobremesa = float(input("Informe o valor da sobremesa: "))

total = suco + prato_principal + sobremesa
total += total*0.10

print(f"O valor total da conta incluindo os 10% de taxa de serviço é R${round(total, 2)}")
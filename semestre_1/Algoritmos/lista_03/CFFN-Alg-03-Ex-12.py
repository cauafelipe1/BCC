# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 12

'''Proposta: A maioria dos anos possui 365 dias. Porém, o tempo para a Terra dar uma volta
completa em torno do Sol é um pouco maior que isso. Como consequência, um dia extra (29
de fevereiro) é incluído em alguns anos para compensar essa diferença. Tais anos são
chamados de anos bissextos. As regras para determinar se um ano é ou não bissexto são as
seguintes:
• Qualquer ano divisível por 400 é bissexto
• Dos demais anos, qualquer ano divisível por 100 não é um ano bissexto
• Dos demais anos, qualquer ano divisível por 4 é um ano bissexto
• Todos os outros anos não são bissextos.

Escreva um programa Python que recebe do usuário um ano, e exibe uma mensagem
informando se o ano é ou não é bissexto.'''

print("=-"*30, "\n[Ano bissexto]")

ano = int(input("Informe um ano: "))

if ano % 400 == 0:
    print(f"O ano {ano} é bissexto!")

else:
    if ano % 100 == 0:
        print(f"O ano {ano} não é bissexto!")
    
    elif ano % 4 == 0:
        print(f"O ano {ano} é bissexto!")

    else:
        print(f"O ano {ano} não é bissexto!")

print("=-"*30)
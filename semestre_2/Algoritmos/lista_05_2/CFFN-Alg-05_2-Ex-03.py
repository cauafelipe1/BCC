# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 03

'''Uma loja online fornece envio de seus itens pelo preço
de R$ 10,95 para o primeiro item e R$ 2,95 para cada um dos demais itens. Escreva uma
função que receba a quantidade de ítens de um pedido e retorne o valor total do envio de
acordo com essas regras. Inclua um programa principal que leia do usuário o número de itens
adquiridos e mostre o custo do envio.'''

def frete(produtos):
    tarifa = 10.95
    if produtos > 1:
        tarifa += produtos * 2.95
    return round(tarifa, 2)

def main():
    produtos = int(input("Digite o número de itens adquiridos: "))
    x = print(f"O valor de entrega dos {produtos} produtos é de R${frete(produtos)}!")
    return x

if __name__ == "__main__":
    main()
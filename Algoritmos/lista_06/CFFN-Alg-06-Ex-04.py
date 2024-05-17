# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 04

'''Crie um programa Python que leia palavras do teclado até que o
usuário forneça uma palavra vazia (somente a tecla enter). Depois disso, seu programa deve
mostrar somente uma vez cada palavra digitada pelo usuário. Ou seja, se o usuário forneceu
mais de uma vez a mesma palavra, ela só poderá ser exibida uma vez. As palavras devem ser
exibidas na mesma ordem em que foram digitadas. Por exemplo, se o usuário digitar:
Primeira
Segunda
Primeira
Terceira
Segunda
Então seu programa deve exibir:
Primeira
Segunda
Terceira'''

def repetidos(dados):
    dados = list(dict.fromkeys(dados))
    for i in dados:
        print(i)


def main():

    dados = []
    while True:
        x = (input("Insira uma string (tecle enter para encerrar):"))
        if x == "":
            break
        else:
            dados.append(x)
    
    return repetidos(dados)



if __name__ == "__main__":
    main()
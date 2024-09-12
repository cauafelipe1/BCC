# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 05

'''Escreva um programa Python que leia números inteiros até
que uma linha em branco seja fornecida pelo usuário (se ele digitar somente enter). Depois
que todos os inteiros tiverem sido lidos, seu programa deve mostrar todos os números
negativos, seguidos por todos os zeros e depois todos os números positivos. Dentro de cada
grupo os números devem ser exibidos na ordem em que foram fornecidos pelo usuário. Por
exemplo, se o usuário forneceu os valores 3, -4, 1, 0, -1, 0 e -2, então seu programa deve
exibir os valores -4, -1, -2, 0, 0, 3 e 1, cada um em uma linha.'''


def ordenar(dados):
    dados_negativos = []
    dados_zerados = []
    dados_positivos = []
    for i in dados:
        if i < 0:
            dados_negativos.append(i)
        elif i == 0:
            dados_zerados.append(i)
        else:
            dados_positivos.append(i)
    dados = dados_negativos + dados_zerados + dados_positivos

    return dados



def main():

    dados = []
    while True:
        try:
            x = (input("Insira um valor inteiro (tecle enter para encerrar):"))
            if x == "":
                break
            else:
                x = int(x)
                dados.append(x)
        except ValueError:
            print("Insira um valor inteiro!!")
            continue
    
    return print(f"Dados ordenados: {ordenar(dados)}")
        
if __name__ == "__main__":
    main()
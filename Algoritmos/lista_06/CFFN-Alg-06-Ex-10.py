# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 10

'''Quando escrevemos uma lista em português, geralmente separamos
os itens por vírgula e colocamos a conjunção “e" entre os dois últimos itens, a não ser que a
lista só tenha um item. Considere as listas abaixo:
maçãs
maçãs e laranjas
maçãs, laranjas e bananas
maçãs, laranjas, bananas e limões
Escreva uma função que receba como parâmetro uma lista de strings e retorne uma única
string contendo todos os itens da lista formatados conforme mostrado acima. Apesar dos
exemplos acima terem no máximo 4 itens, sua função deve se comportar corretamente para
listas de qualquer tamanho. Escreva uma função main demonstrando o funcionamento de sua
função.'''

def formatar(dados):
    if len(dados) >= 2:
        for i in dados:
            if i == dados[-2]:
                print(i, end=" e ")
            elif i != dados[-1]:   
                print(i, end=", ")
            else:
                print(i)
    else:
        print(dados[0])

def main():

    dados = []
    while True:
        x = (input("Insira uma string (tecle enter para encerrar):"))
        if x == "":
            break
        else:
            dados.append(x)
    
    return formatar(dados)




if __name__ == "__main__":
    main()
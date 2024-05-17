# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 12

'''Escreva uma função que determina se uma lista de valores está ou
não em ordem de classificação (crescente ou decrescente). A função deve receber a lista
como parâmetro e retornar True se a lista já estiver classificada. Caso contrário, ele deve
retornar False. Escreva um programa principal que leia uma lista de números do usuário e use
sua função para relatar se a lista é classificada.
Observação: certifique-se de considerar estas questões ao concluir este exercício:
Uma lista vazia está em ordem? E uma lista contendo somente um elemento?'''

def verificador(dados):
    crescente = dados[:]
    decrescente = dados[:]

    crescente.sort()
    decrescente.sort(reverse = True)
    
    result = False
    if (crescente == dados) or (decrescente == dados):
        result = True
    return result

def main():

    dados = []
    while True:
        try:
            x = input("Insira valores inteiros para a lista (tecle enter para encerrar):")
            if x == "":
                break
            else:
                dados.append(int(x))
        except ValueError:
            print("Digite um valor inteiro!")
            continue
    
    if verificador(dados):
        return print("A lista está em ordem de classificação!")
    else:
        return print("A lista não está em ordem de classificação!")




if __name__ == "__main__":
    main()
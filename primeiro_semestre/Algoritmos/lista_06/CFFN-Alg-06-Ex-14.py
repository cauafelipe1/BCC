# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 14

'''Escreva uma função chamada precedencia que retorna um
inteiro representando a precedência de um operador matemático. Uma string contendo o
operador será passada para a função como seu único parâmetro. Sua função deve retornar 1
para + e -, 2 para * e / e 3 para ^. Se a string passada para a função não for um desses
operadores, a função deve retornar -1. Inclua um programa principal que lê um operador do
usuário e exibe a precedência do operador ou uma mensagem de erro indicando que a
entrada não era um operador.'''

def procedencia(operacao):
    result = -1
    if ("+" in operacao) or ("-" in operacao):
       result = 1
    elif  ("/" in operacao) or ("*" in operacao):
        result = 2
    elif "^" in operacao:
        result = 3
    return result
def main():
    operacao = input("Insira uma operação qualquer (utilize ^ para exponenciação): ")
    print("[Legenda]:\noperadores + e -: 1\noperadores * e /: 2\noperador ^: 3\noperdor não identificado: -1")
    return print(f"Procedência da operação inserida: {procedencia(operacao)}")

if __name__ == "__main__":
    main()
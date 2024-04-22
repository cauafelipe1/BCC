# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 06

'''Escreva uma função que recebe uma string como seu primeiro
parâmetro e a largura de uma linha do terminal em caracteres como seu segundo parâmetro.
Sua função deve retornar uma nova string que consiste na string original e no número correto
de espaços iniciais para que a string original apareça centralizada dentro da largura fornecida
quando for impressa. Não adicione nenhum caractere ao final da string. Inclui um programa
principal que demonstre sua função.'''

def centralizar(string, terminal_lenght):
    diferenca = terminal_lenght - len(string)
    prefixo = " "*(diferenca//2)
    return print(f"{prefixo}{string}")

def main():
    string = input("Insira uma string: ")
    terminal_lenght = int(input("Insira a largura do seu terminal: "))
    return centralizar(string, terminal_lenght)

if __name__ == "__main__":
    main()
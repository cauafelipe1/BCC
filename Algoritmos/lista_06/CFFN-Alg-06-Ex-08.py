# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 08

'''Neste exercício você deve criar uma função em Python que recebe um
texto em uma string e retorna uma lista somente com as palavras, sem espaços ou símbolos
de pontuação. Por exemplo, se a string for: “Beleza! Este é um ótimo exemplo, você
não acha?”, sua função deveria retornar a seguinte lista: [ “Beleza", “Este", “é",
“um", “ótimo", "exemplo", “você", “não", “acha”]. Escreva uma função main
que demonstre o funcionamento da sua solução.'''


def main():
    string = input("Insira uma string:")
    n = string.split()
    return print(n)
    


if __name__ == "__main__":
    main()
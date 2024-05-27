# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 07

'''Uma cartela de bingo é formada por 5 linhas e 5 colunas. As colunas são
rotuladas com as letras B, I, N, G e O. Existem 15 números diferentes que podem aparecer
abaixo de cada letra. Abaixo do B podem aparecer os números de 1 a 15; abaixo do I os
números de 16 a 30, abaixo do N os números de 31 a 45 e assim por diante. Escreva uma
função que cria uma cartela de bingo e a armazena em um dicionário. As chaves do dicionário
são as letras B, I, N, G e O. Os valores devem ser listas de 5 números cada, que aparecem
abaixo de cada letra na cartela. A função deve retornar o dicionário. Escreva uma segunda
função que recebe o dicionário e exibe a cartela de bingo com as colunas rotuladas
apropriadamente. Escreva um programa main que gere e exiba uma cartela de bingo usando
suas funções.'''

from random import sample

def criar_cartela():
    cartela = {
        'B': sample(range(1, 16), 5),
        'I': sample(range(16, 30), 5),
        'N': sample(range(31, 45), 5),
        'G': sample(range(46, 60), 5),
        'O': sample(range(61, 75), 5)
    }
    return cartela

def exibir_cartela(cartela):
    print("-"*35)
    print("| B\tI\tN\tG\tO |")
    print("-"*35) 

    for i in range(5):
        for letra in 'BINGO':
            if letra == "B":
                print(f"|{cartela[letra][i]:2}", end="\t")
            elif letra == "O":
                print(f"{cartela[letra][i]:2}|")
            else:    
                print(f"{cartela[letra][i]:2}", end="\t")
    print("-"*35)

def main():
    cartela = criar_cartela()
    return exibir_cartela(cartela)

if __name__ == "__main__":
    main()
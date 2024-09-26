# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 10

'''Proposta: As posições das casas em tabuleiros de xadrez são identificadas
por uma letra e um número. A letra identifica a coluna e o número define a linha, conforme a
figura abaixo:

* Figura de um tabuleiro de xadrez

Escreva um programa Python que receba do usuário um posição. Use um comando if para
determinar se a coluna informada começa com quadrado preto ou branco. Então, use
aritmética de inteiros para determinar a cor do quadrado da linha correspondente. Por
exemplo, se o usuário entrou com o valor a1, então seu programa deve informar que o
quadrado é preto. Se o usuário entrou com o valor d5, então seu programa deve informar que
o quadrado é branco. Seu programa pode assumir que o usuário vai entrar valores válidos,
não sendo necessário verificar eventuais erros de input.'''

print("=-"*30, "\n[Cor da casa do tabuleiro]")

# colunas onde a primeira linha é de casas brancas
letras_branco = ["b", "d", "f", "h"]

# colunas onde a primeira linha é de casas brancas
letras_preto = ["a", "c", "e", "g"]

casa = input("Insira a casa desejada: ")
casa = casa.lower()

casa_lista = list(casa)

letra = casa_lista[0]
num = casa_lista[1]
num = int(num)

if ((letra in letras_branco) or (letras_preto)) and 0 <= num <= 8:
    if (letra in letras_branco) and num % 2 != 0:
        print(f"A casa {casa} é uma casa da cor branca!")

    elif (letra in letras_branco) and num % 2 == 0:
        print(f"A casa {casa} é uma casa da cor preta!")

    elif (letra in letras_preto) and num % 2 != 0:
        print(f"A casa {casa} é uma casa da cor preta!")

    elif (letra in letras_preto) and num % 2 == 0:
        print(f"A casa {casa} é uma casa da cor branca!")

else:
    print(f"{casa} não é uma casa válida em um tabuleiro de xadrez 8x8.")

print("=-"*30)
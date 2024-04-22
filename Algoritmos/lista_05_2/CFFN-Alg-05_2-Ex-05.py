# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 05

'''Palavras como primeiro, segundo e terceiro são chamadas de números
ordinais. Neste exercício, você deve escrever uma função que recebe um inteiro como seu
único parâmetro e retorna uma string contendo o número ordinal em português como seu
único resultado. Sua função deve lidar com números inteiros entre 1 e 12 (inclusive). Ela deve
retornar uma string vazia se um valor fora desse intervalo for fornecido como um parâmetro.
Inclua um programa principal que demonstra sua função exibindo cada inteiro de 1 a 12 e seu
respectivo número ordinal.'''


def ordinal(n):
    ordinais = ["", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "sétimo", "oitavo", "nono", "décimo", "décimo primeiro", "décimo segundo"]
    if 1 <= n <= 12:
        return ordinais[n]
    else:
        return ""

def main():
    n = 1
    while n <= 12:
        print(f"{n}: {ordinal(n)}")
        n += 1

if __name__ == "__main__":
    main()
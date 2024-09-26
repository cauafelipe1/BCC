# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 15

'''Escreva duas funções chamadas hex2int e int2hex, que
devem fazer a conversão entre dígitos hexadecimais (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E e
F) e números inteiros de base 10 . A função hex2int é responsável por converter uma string
contendo um único dígito hexadecimal em um inteiro de base 10, enquanto a função int2hex
é responsável por converter um inteiro entre 0 e 15 em um único dígito hexadecimal. Cada
função pegará o valor a ser convertido como seu único parâmetro e retornará o valor
convertido como o único resultado da função. Certifique-se de que a função hex2int funcione
corretamente para letras maiúsculas e minúsculas. Observação: se você não sabe como
converter números entre bases diferentes, veja o quadro explicativo ao final da lista de
exercícios.'''

def int2hex(n):
    base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    convertido = ""
    while n > 0:
        resto = n % 16
        convertido = base[resto] + convertido
        n = n//16
    return convertido

def hex2int(n):
    base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    convertido = 0
    expoente = len(n) - 1
    for digito in n:
        if digito.isdigit():
            convertido += int(digito) * (16 ** expoente)
        else:
            convertido += (ord(digito.upper()) - 55) * (16 ** expoente)
        expoente -= 1
    return convertido

def main():
    n = int(input("Insira um valor inteiro na base decimal: "))
    n2 = input("Insira um valor na base hexadecimal: ")
    x = print(f"O número {n} na base decimal equivale ao {int2hex(n)} na base hexadecimal!")
    y = print(f"O valor {n2} na base hexadecimal equivale ao {hex2int(n2)} na base decimal!")
    return x, y

if __name__ == "__main__":
    main()
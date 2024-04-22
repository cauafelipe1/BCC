# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 16

'''numérica. Escreva um programa que permita ao usuário
converter um número de uma base para base 10 e vice-versa. Seu programa deve suportar
bases entre 2 (binário) e 16 (hexadecimal) para o número de entrada e o número de resultado.
Divida seu programa em várias funções, incluindo uma função que converte de uma base
arbitrária em uma base 10, uma função que converte de uma base 10 em uma base arbitrária.
A primeira função deve receber como parâmetros uma string com o número a ser convertido
para base 10, e o valor da base deste número (portanto, de 2 a 16) e deve retornar como
resultado o número convertido na base 10. A segunda função deve receber como parâmetros
um numero na base 10 e a base para qual queremos converter o número. Como resultado, a
função deve retornar uma string com o número convertido. Além disso, faça um programa
principal que lê as bases e o número de entrada do usuário. Você pode encontrar parte da
solução deste problema no exercício anterior e nos exercícios 14 e 15 da lista 4.'''

def int2arbitrario(n, base):
    convertido = ""
    n = int(n)
    if base == 16:
        base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        while n > 0:
            resto = n % 16
            convertido = base[resto] + convertido
            n = n//16

    else:
        while n > 0:
            resto = n % 2
            convertido = str(resto) + convertido
            n = n//2
    return convertido

def arbitrario2int(n, base):
    convertido = 0
    if base == 16:
        base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        expoente = len(n) - 1
        for digito in n:
            if digito.isdigit():
                convertido += int(digito) * (16 ** expoente)
            else:
                convertido += (ord(digito.upper()) - 55) * (16 ** expoente)
            expoente -= 1
    else:
        expoente = len(n) - 1
        for digito in n:
            convertido += int(digito) * (2 ** expoente)
            expoente -= 1
    return convertido

def opcoes(n, base):
    print("Escolha a operação:")
    x = int(input("1. Arbitrário para decimal\n2. Decimal para arbitrário:\n"))
    if base == 2:
        bases = "binária"
    else:
        bases = "hexadecimal"
    if x == 1:
        result = print(f"O número {n} na base {bases} equivale ao {arbitrario2int(n, base)} na base decimal!")
    else:
        result = print(f"O número {n} na base decimal equivale ao {int2arbitrario(n, base)} na base {bases}!")
    return result

def main():
    n = input("Insira um valor arbitrario: ")
    base = int(input("Insira a base deste valor: "))
    return opcoes(n, base)

if __name__ == "__main__":
    main()
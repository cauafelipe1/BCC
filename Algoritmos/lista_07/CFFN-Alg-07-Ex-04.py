# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 04

'''O código morse é um esquema de codificação de letras e números utilizando
pontos e traços. Neste exercício você deve escrever um programa que usa um dicionário para
armazenar o mapeamento de letras e números para código Morse. Voce deve representar os
pontos com símbolo de ponto “.” e traços com sinal de subtração “-“. A tabela abaixo mostra o
mapeamento de letras e números para código Morse. Seu programa deve ler uma mensagem
do usuário e então deve traduzir cada letra e número para código Morse, deixando um espaço
em branco entra cada caractere traduzido. O programa deve ignorar qualquer caracter que
não seja letra ou número. Por exemplo, a mensagem Hello, World! Deve ser exibida da
seguinte forma: .... . .-. .-.. --- .-- --- .-. .-.. -..
Letter Code       Letter Code      Letter Code      Number Code
A       .-        J      .- - -    S      ...       1      .- - - -
B       -...      K      -.-       T      -         2      ..- - -
C       -.-.      L      .-..      U      ..-       3      ...- -
D       -..       M      - -       V      ...-      4      ....-
E       .         N      -.        W      .- -      5      .....
F       ..-.      O      ---       X      -..-      6      -....
G       - -.      P      .- -.     Y      -.- -     7      - -...
H       ....      Q      - -.-     Z      - -..     8      - - -..
I       ..        R      .-.       0      -----     9      - - - -.'''

def codificar(s):
    string_codificada = ""
    s = s.upper()
    dicionario_morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' '}
    for i in s:
        if i not in dicionario_morse.keys():
            pass
        else:
            string_codificada += dicionario_morse[i] + " "
    return string_codificada
            
        

    
def main():
    s = input("Insira uma string: ")
    return print(codificar(s))

if __name__ == "__main__":
    main()
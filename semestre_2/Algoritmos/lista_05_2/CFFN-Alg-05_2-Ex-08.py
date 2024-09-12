# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 08

'''Muitas pessoas não usam letras maiúsculas corretamente, especialmente
ao digitar em smartphones. Neste exercício, você escreverá uma função que coloca em
maiúscula os caracteres apropriados em uma string. O primeiro caractere da string deve ser
convertido em letra maiúscula, assim como o primeiro caractere (que não seja espaço) após
um “.”, “!” ou "?". Por exemplo, se a função for fornecida com a string “que horas eu tenho que
estar lá? qual é o endereço?" então ele deve retornar a string “Que horas eu tenho que estar
lá? Qual é o endereço?". Inclua um programa principal que leia uma string do usuário, corrige
as letras maiúsculas usando sua função e exibe o resultado.'''

def corretor(string):
    corrigida = ""
    prox_letra_maiuscula = True

    for letra in string:
        
        if letra.isalpha():

            if prox_letra_maiuscula:
                corrigida += letra.upper()
                prox_letra_maiuscula = False

            else:
                corrigida += letra.lower()

        else:
            corrigida += letra

        if letra in ".!?":
            prox_letra_maiuscula = True

    return corrigida


def main():
    string = input("Insira uma mensagem: ")
    return print(corretor(string))

if __name__ == "__main__":
    main()

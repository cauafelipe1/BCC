# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 11

'''Escreva uma função que gere uma senha aleatória. A senha deve ter um
comprimento aleatório de 7 a 10 caracteres. Cada caractere deve ser selecionado
aleatoriamente das posições 33 a 126 na tabela ASCII. Sua função não receberá nenhum
parâmetro. Ele retornará a senha gerada aleatoriamente como seu único resultado. Exiba a
senha gerada aleatoriamente no programa principal do seu arquivo fonte.'''

from random import randint
def gerarSenha():
    x = ""
    n = randint(7, 10)

    for i in range(n):
        x += chr(randint(33, 126))
    
    return print(x)


def main():
    print("Senha aleatória:")
    return gerarSenha()

if __name__ == "__main__":
    main()
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 09

'''Neste exercício, você deve escrever uma função chamada
isInteger que determina se os caracteres em uma string representam ou não um inteiro válido,
retornando um valor lógico como resultado. Ao determinar se uma string representa um inteiro,
você deve ignorar qualquer espaço em branco à esquerda ou à direita. Uma vez que este
espaço em branco é ignorado, uma string representa um inteiro se seu comprimento for pelo
menos 1 e contiver apenas dígitos, ou se seu primeiro caractere for + ou - e o primeiro
caractere é seguido por um ou mais caracteres, todos os quais são dígitos. Escreva um
programa principal que leia uma string do usuário e informe se ela representa ou não um
número inteiro.'''

def isInteger(n):
    n = n.strip()
    result = True

    if n[0] in "-+":
        result = True

        for char in n[1:]:
            if char in "0123456789":
                result = True
            else:
                result = False
    else:
        for char in n:
            if char in "0123456789":
                result = True
            else:
                result = False    
    return result
    
def main():
    n = input("Digite uma string para saber se ela é ou não um número: ")
    if isInteger(n):
        x = "É um número!"
    else:
        x = "Não é um número!"
    return print(x)

if __name__ == "__main__":
    main()
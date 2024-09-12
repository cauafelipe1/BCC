# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 06
'''Euclides foi um matemático grego que viveu há
aproximadamente 2.300 anos. Seu algoritmo para calcular o MDC - máximo divisor comum de
dois inteiros positivos, a e b, é eficiente e recursivo. Está descrito abaixo:
MDC(a, b)
    if b == 0 then
        return a
    else
        c ← a%b
    return MDC(b,c)
    end
Escreva um programa que implemente o algoritmo recursivo de Euclides e o use para
determinar o máximo divisor comum de dois inteiros inseridos pelo usuário.'''

def MDC(a, b):
    if b == 0:
        return a
    else:
        c = a % b
    return MDC(b, c)

def main():
    a = int(input("Insira um valor inteiro positivo para a: "))
    b = int(input("Insira um valor inteiro positivo para b: "))
    mdc = MDC(a, b)
    return print(f"O máximo divisor comum entre {a} e {b} é {mdc}")

if __name__ == "__main__":
    main()
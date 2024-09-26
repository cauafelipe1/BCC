# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 07

'''Um número inteiro positivo n é chamado de número perfeito se a soma
de todos os divisores de n é igual a n. Por exemplo, 28 é um número perfeito porque seus
divisores são 1, 2, 4, 7 e 14; e 1+2+4+7+14=28. Escreva uma função para verificar se um
número é perfeito. A função deve receber somente um número inteiro positivo e retornar True
se ele for perfeito ou False caso contrário. Escreva uma função main para identificar e imprimir
todos os números perfeitos de 1 a 10.000. Obs.: você pode usar o código do exercício anterior
para lhe ajudar nesta tarefa.'''

def numero_perfeito(n):
    divisores = []

    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)

    soma = sum(divisores)
    if soma == n:
        return True
    else:
        return False

def main():
    print("Números considerados perfeitos de 1 a 10.000:")
    n = 1
    print(n) # necessario pois n = 1 não se encaixa na função número_perfeito
    
    while n <= 10000:
        if numero_perfeito(n):
            print(n)
        n +=1

if __name__ == "__main__":
    main()
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 13

'''Proposta: A fatoração de um número inteiro n pode ser feita por meio de números
primos de acordo com o procedimento descrito abaixo:
Inicialize fator com valor 2
Enquanto fator for menor ou igual a n, faça
Se n for divisível por fator então
Concluímos que fator faz parte da fatoração de n
Faça divisão inteira de n por fator
Senão
Incremente fator em uma unidade'''

while True:
    try:
        n = int(input("Insira um valor inteiro (maior ou igual a 2): "))
        #atribuindo um valor constante a n para a formatação do print
        constante = n
        fator = 2
        if n < fator:
            print("Insira um valor válido!!")
            continue
        else:
            while fator <= n:
                if n % fator == 0:
                    print(f"{fator} faz parte da fatoração de {constante}")
                    n = n // fator

                else:
                    fator += 1
            break
    except ValueError:
        print("Insira um valor válido!!")
        continue


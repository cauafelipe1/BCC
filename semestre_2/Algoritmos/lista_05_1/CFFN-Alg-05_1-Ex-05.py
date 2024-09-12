# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 05

'''Escreva uma função Python chamada potencia(x, y), que vai receber receber 2 números
reais x e y, e vai retornar o valor de x elevado a y. Obs.: faça a operação de potenciação
usando laço de repetição com comandos for ou while.'''

while True:
    try:
        x = int(input("Insira o valor de x: "))
        y = int(input("Insira o valor de y: "))
        break
    except ValueError:
        print("Algum dos valores inseridos não é válido! Insira novamente..")
        continue

def potencia(x, y):
    result = 1
    for i in range(y):
        result *= x
    
    print(f"{x}^{y} = {result}")

potencia(x, y)
    
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 03

'''Escreva uma função Python chamada quociente(x, y), que vai receber receber 2 números
reais x e y, e vai retornar o valor da divisão de x por y.'''

while True:
    try:
        x = float(input("Insira o valor de x: "))
        y = float(input("Insira o valor de y: "))
        break
    except ValueError:
        print("Algum dos valores inseridos não é válido! Insira novamente..")
        continue

def quociente(x, y):
    try:
        divisao = x/y
        print(f"Tomando x = {x} e y = {y}, temos:\nx/y = {divisao}")
    
    except ZeroDivisionError:
        print("x não pode ser dividido por 0!!")

quociente(x, y)
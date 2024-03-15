# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 11

from math import sqrt
'''Proposta: Uma função quadrática pode ser descrita da seguinte forma:
f(x) = ax² + bx + c, onde a, b e c são constantes, e a é diferente de zero. As raízes da
função quadrática podem ser encontradas determinando-se os valores de x que satisfaçam a
equação quadrática ax² + bx + c = 0. . Uma função quadrática pode ter 0, 1 ou 2 raízes
reais. Essas raízes podem ser calculadas pela fórmula da Bháskara, mostrada abaixo:

raiz = (-b ± √b²-4ac)/2a

A parte da expressão dentro da raiz quadrada é chamada de discriminante. Se o discriminante
for negativo, a equação não possui raízes reais. Se o discriminante for igual a zero, então a
equação tem apenas uma raiz real. Caso contrário, a equação tem duas raízes reais e a
expressão deve ser computada duas vezes, uma com o sinal de + e a outra com o sinal de -
ao se calcular o numerador da fração.

Escreva um programa Python que calcula as raízes reais de uma função quadrática. Seu
programa deve iniciar solicitando ao usuário os valores de a, b e c. Então o programa deve
exibir uma mensagem informando a quantidade de raízes reais e o(s) valor(es) da(s) raiz(es).'''


print("=-"*30, "\n[Raízes de equação quadrática]")

a = float(input("Insira o valor de a de sua equação: "))
b = float(input("Insira o valor de b de sua equação: "))
c = float(input("Insira o valor de c de sua equação: "))

# discriminante
delta = (b ** 2) - 4 * a * c

if a != 0:
    if delta < 0:
        print("A equação não possui raízes reais.")

    elif delta > 0:
        x1 = (- b + sqrt(delta))/(2*a)
        x2 = (- b - sqrt(delta))/(2*a)
        
        print("A função possui duas raízes reais.")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    
    elif delta == 0:
        x1 = (- b + sqrt(delta))/(2*a)
        print("A equação possui apenas uma raíz real.")
        print(f"x1 = {x1}")

else:
    print("O valor de a não pode ser igual a zero.")
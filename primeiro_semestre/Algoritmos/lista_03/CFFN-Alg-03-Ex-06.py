# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 06

'''Proposta: Baseado nos comprimentos dos seus lados, um triângulo pode ser
classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando
apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um
programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba
uma mensagem informando qual é o tipo do triângulo.'''

print("=-"*30, "\n[Classifique o triângulo]")

l1 = float(input("Digite o comprimento do primeiro lado do seu triângulo: "))
l2 = float(input("Digite o comprimento do segundo lado do seu triângulo: "))
l3 = float(input("Digite o comprimento do terceiro lado do seu triângulo: "))

if (l1 > 0) and (l2 > 0) and (l3 > 0):
    if (l1 == l2) and (l2 == l3):
        print("O triângulo cujo o comprimento dos três lados inseridos é classificado como triângulo equilátero.")

    elif ((l1 == l2) and (l1 != l3)) or ((l2 == l3) and (l2 != l1)) or ((l1 == l3) and (l1 != l2)):
        print("O triângulo cujo o comprimento dos três lados inseridos é classificado como triângulo isóceles.")

    elif (l1 != l2) and (l1 != l3):
        print("O triângulo cujo o comprimento dos três lados inseridos é classificado como triângulo escaleno.")

else:
    print("Algum dos valores inseridos não é valido.")

print("=-"*30)


'''OBS: O código ainda está incompleto, pois ele não verifica se os valores de comprimento
iseridos são de um triângulo possível. Ou seja, não seguem a regra: 

"Só irá existir um triângulo se, somente se, um de seus lados deve ser maior que o 
valor absoluto (módulo) da diferença dos outros dois lados
e menor que a soma dos outros dois lados."'''
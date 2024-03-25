# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 10

'''Proposta: Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica
à string original. Por exemplo: “arara”, “osso”, “radar”. Escreva um programa Python usando
laço de repetição para determinar se uma palavra fornecida pelo usuário é ou não é um
palíndromo. Seu programa deve exibir uma mensagem informando o resultado.'''

# o programa ainda considera apenas uma palavra pois no exercício 11
# serão solicitadas melhorias deste mesmo, considerando espaços, pontuações e múltiplas palavras
palavra = (input("Insira uma palavra: "))

contador = 0
for i in range(len(palavra)):
    if palavra[i] == palavra[-(i+1)]:
        contador += 1

if contador == len(palavra):
    print(f"A palavra {palavra} é um palíndromo!")

else:
    print(f"A palavra {palavra} não é um palíndromo!")
    
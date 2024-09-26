# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 11

'''Proposta: O conceito de palíndromo também pode ser aplicado
a frases, por exemplo: “A base do teto desaba”. Faça um novo programa Python que
modifique o programa do exercício anterior para verificar se frases são palíndromos. Seu
programa vai precisar ignorar os espaços em brando das frases. Como desafio adicional,
amplie sua solução para que também ignore sinais de pontuação e trate letras maiúsculas e
minúsculas como equivalentes'''

frase = (input("Insira uma frase: "))
alfabeto = "abcdefghijklmnopqrstuvwxyz"
contador = 0

nova_frase = ""

for i in range(len(frase)):
    if frase.lower()[i] in alfabeto:
        nova_frase += frase.lower()[i]

for i in range(len(nova_frase)):
        if nova_frase[i] == nova_frase[-(i+1)]:
            contador += 1

if contador == len(nova_frase):
    print(f"A frase {frase} é um palíndromo!")

else:
    print(f"A frase {frase} não é um palíndromo!")
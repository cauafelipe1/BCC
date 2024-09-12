# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 08

'''Proposta: Parte 2 - Comando WHILE - faça todos os exercícios desta parte com "while":
8. Faça um programa Python que peça 10 números inteiros e apresente: a média, o maior e o
menor dentre os 10 números fornecidos.'''

print("=-"*30, "\n[Média, maior e menor]")
numeros = []
i = 1

while i <= 10:
    try:
        n = int(input(f"Insira o {i}° inteiro: "))
        numeros.append(n)
        i += 1
    except ValueError:
        print("Você deve inserir valor inteiro!!")
        pass

media = (sum(numeros))/10

print(f"\nMédia dos números fornecidos: {media}")
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")

print("=-"*30)
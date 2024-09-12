# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-03
# Exercício: 03

'''Proposta: Escreva um programa Python que peça para o usuário uma letra do
alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma
mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a
mensagem informando que a letra é uma consoante.'''

print("=-"*30, "\n[Vogal ou consoante?]")

letra = input("Insira uma letra: ")

vogais = ["a", "e", "i", "o", "u"]

if letra.lower() in vogais:
    print(f"A letra {letra} é uma vogal!")

else:
    print(f"A letra {letra} é uma consoante!")

# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 01

'''Escreva uma função Python chamada imprime_nome(nome), que vai receber uma string e
vai imprimir essa string 5 vezes.'''

def imprime_nome(nome):
    for i in range(5):
        print(nome)

nome = input("Insira o seu nome: ")
imprime_nome(nome)
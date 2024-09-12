# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 02

'''Escreva uma função Python chamada imprime_n_vezes(nome, n), que vai receber uma
string e um numero inteiro n, e vai imprimir essa string n vezes.'''

def imprime_n_vezes(nome, n):
    for i in range(n):
        print(nome)
nome = input("Insira o seu nome: ")

n = int(input("Quantas vezes deseja exibir seu nome? "))

imprime_n_vezes(nome, n)
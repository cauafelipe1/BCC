# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 03

'''Proposta: Parte 1 - Comando FOR - faça todos os exercícios desta parte com comando “for" e função
“range":
3. Faça um programa Python que calcule os quadrados e cubos dos números de 0 a 10 e
imprima os valores resultantes no formato de tabela, como segue:
Número              Quadrado        Cubo
0                      0              0
1                      1              1
2                      4              8
3                      9              27
4                      16             64
5                      25             125
6                      36             216
7                      49             343
8                      64             512
9                      81             729
10                     100            1000

Observação: para imprimir com espaços tabulados (tecla “tab”), coloque o caracter “\t” dentro
da string a ser impressa. Por exemplo: print(“Número\t\tQuadrado\t\tCubo”)'''

print("=-"*30, "\n[Quadrados e cubos de 1 a 10]")

print("Número\t\tQuadrado\tCubo")
for i in range(11):
    print(f"{i}\t\t {i**2}\t\t {i**3}")

print("=-"*30)
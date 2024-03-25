# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 15

'''Proposta: Decimal para binário. Escreva um programa Python que converte um número decimal (base 10) para o
correspondente número binário (base 2). Leia o número decimal como um número inteiro fornecido pelo
usuário. Depois disso, use o algoritmo de divisão mostrado abaixo para fazer a conversão. Quando o
algoritmo terminar, a variável result contém a representação binária do número. Ao final exiba uma
mensagem informando o valor de result.
Inicialize result como uma string vazia
Seja q o número decimal a ser convertido
Repita
r recebe o resto da divisão de q por 2
converta r para uma string e adicione no início de result
faça a divisão inteira de q por 2 (descartando o resto) e guarde o resultado em q
Até que q seja igual a zero'''

result = ""

q = int(input("Insira o número decimal que deseja converter para binário: "))
decimal_inserido = str(q)

while q != 0:
    r = q % 2
    result = str(r) + result
    q = q//2

print(f"O decimal {decimal_inserido} equivale a {result} em binário")
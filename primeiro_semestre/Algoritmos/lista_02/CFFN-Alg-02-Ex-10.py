# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 10

'''Proposta: Suponha que uma escola utilize, como código de matrícula, um
número inteiro no formato AASDDD, onde:
• os dois primeiros dígitos, representados pela letra A, são os dois últimos algarismos do ano
da matrícula;
• o terceiro dígitos, representado pela letra S, vale 1 ou 2, conforme o aluno tenha se
matriculado no 1o ou 2o semestre;
• os três últimos dígitos, representados pela letra D, correspondem à ordem da matrícula do
aluno, no semestre e no ano em questão.
Crie um programa Python que leia o número de matrícula de um aluno e imprima o ano e o
semestre em que ele foi matriculado. Por exemplo, um número de matrícula 182034 deve
resultar ano 18 e semestre 2.'''

print("=-"*30, "\nDescrição de matrícula")

m = int(input("Insira um valor inteiro que representa uma matrícula no formato AASDDD: "))

ano = m//10000
resto = m%10000

semestre = resto//1000

print(f"O número de matrícula {m} corresponde ao estudante que ingressou no ano de final {ano} e no {semestre}° semestre.")



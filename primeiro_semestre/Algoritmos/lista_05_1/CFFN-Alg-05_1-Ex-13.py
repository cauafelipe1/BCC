# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 13

'''Usando a função do exercício anterior, faça um programa que lê dois inteiros positivos a e b e
verifica se o menor deles é segmento do outro.
Exemplos:
a       b
567890 678 => b é segmento de a
1243 2212435 => a é segmento de b
235 236 => um não é segmento do outro'''

a = int(input("Insira um valor para a: "))
b = int(input("Insira um valor para b: "))

def verifica_segmento(a, b):
    if a < b:
        if str(a) in str(b):
            return "a é segmento de b"
        else:
            return "um não é segmento do outro"

    elif b < a:

        if str(b) in str(a):
            return "b é seguimento de a"
        else:
            return "um não é segmento do outro"

    else:
        return "os números são iguais"

print(f"a\tb\n{a}\t{b}\t=> {verifica_segmento(a, b)}")
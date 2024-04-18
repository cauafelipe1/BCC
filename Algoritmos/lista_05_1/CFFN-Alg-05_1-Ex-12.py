# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.1
# Exercício: 12

'''Construa uma função chamada "encaixa" que, dados dois inteiros positivos a e b, verifica se b
corresponde aos últimos dígitos de a.
Exemplos:
a b
567890 890 => encaixa
1243 1243 => encaixa
2457 245 => não encaixa
457 2457 => não encaixa'''

a = int(input("Insira um valor para a: "))
b = int(input("Insira um valor para b: "))

def encaixa(a, b):

    a_str = str(a)
    b_str = str(b)
    
    if len(b_str) > len(a_str):
        return False  
    
    return a_str[-len(b_str):] == b_str

if encaixa(a, b):
    print(f"a\tb\n{a}\t{b}\t=> encaixa")
else:
    print(f"a\tb\n{a}\t{b}\t=> não encaixa")
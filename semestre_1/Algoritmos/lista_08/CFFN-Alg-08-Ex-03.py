# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 03

'''Faça uma função Python recursiva que recebe uma string e retorne um valor
lógico indicando se ela é ou não é um palíndromo. OBS: Um palíndromo é uma palavra ou
frase, que é igual quando lida da esquerda para a direita ou da direita para a esquerda
(Espaços em branco e sinais de pontuação devem ser descartados). Exemplo de palíndromo:
"saudavel leva duas”.'''

def isolar_caracteres(s):
    chars = ".!?:;,"
    for i in s:
        if i in chars:
            s.replace(i, "")
    s = s.replace(" ", "")
    return s

def palindromo(s):
    return s == s[::-1]
    
def main():
    s = input("Insira uma palavra ou frase: ")
    string = isolar_caracteres(s)

    if palindromo(string):
        return print(f'"{s}" é um palíndromo!!')
    return print(f'"{s}" não é um palíndromo!!')
if __name__ == "__main__":
    main()
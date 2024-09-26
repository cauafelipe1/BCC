# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 01

'''Escreva uma função Python para verificar se uma string possui
caracteres únicos. Por exemplo, a string “azul" não repete letras, mas a string
“ferramenta"possui letras repetidas. A função deve receber uma string e retornar True no
primeiro caso (letras únicas) ou False caso contrário (letras repetidas). Você deve usar
conjuntos para implementar a função.'''

def char_unicos(string):
    caracteres = set()

    for i in string:
        if i in caracteres:
            return False
        caracteres.add(i)
    return True
    
def main():
    string = input("Insira uma string: ")
    if char_unicos(string):
        return print(f"A string {string} possui apenas characteres únicos!!")
    return print(f"A string {string} possui caracteres repetidos!!")


if __name__ == "__main__":
    main()
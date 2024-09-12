# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 11

'''Escreva uma função recursiva que implemente a técnica de
compressão run-lenght descrita no exercício anterior. Sua função deve receber uma lista ou
uma string como seu único parâmetro. Ela deve retornar a lista compactada em run-lenght
como seu único resultado. Inclua um programa principal que leia uma string do usuário, a
compacte e exiba o resultado codificado em run-lenght.'''

def compactar_run_lenght(s):
    if not s:
        return []
    
    char = s[0]
    contador = 1
    while contador < len(s) and s[contador] == char:
        contador += 1
    return [char, contador] + compactar_run_lenght(s[contador:])

def main():
    s = input("Insira uma string que vc deseja comprimir utilizando o método run lenght: ")
    lista_compactada = compactar_run_lenght(s)
    return print(f'String "{s}" compactada: {lista_compactada}')

if __name__ == "__main__":
    main()
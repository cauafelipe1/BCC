# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 06
'''Neste exercício você deve desenvolver um
programa Python para identificar a(s) palavra(s) mais longa(s) de um arquivo. Seu programa
deve exibir uma mensagem que inclua o tamanho da palavra mais longa, juntamente com
todas as palavras daquele tamanho que existem no arquivo. Trate cada grupo de caracteres
sem espaço como uma palavra, mesmo se esse grupo contiver números ou sinais de
pontuação.'''

if __name__ == "__main__":
    arquivo_entrada = input("Insira o arquivo: ")
    with open(arquivo_entrada, "r") as arquivo:
            conteudo = arquivo.readlines()
            texto = ""
            for i in conteudo:
                texto += i.replace("\n", " ")
            texto = texto.split()
            maior_palavra = (max(texto,key=len))
            print(f'A maior palavra no arquivo é "{maior_palavra}", contendo {len(maior_palavra)} letras!')

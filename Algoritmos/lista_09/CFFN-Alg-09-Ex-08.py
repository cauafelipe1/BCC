# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 08

'''Escreva um programa que exiba a palavra
(ou palavras) que ocorrem com mais frequência em um arquivo. Seu programa deve começar
lendo o nome do arquivo do usuário. Em seguida, ele deve encontrar a (s) palavra (s) dividindo
cada linha do arquivo em cada espaço. Finalmente, quaisquer sinais de pontuação à esquerda
ou à direita devem ser removidos de cada palavra. Além disso, seu programa deve ignorar a
capitalização. Como resultado, porta, porta!, Porta e PoRTA devem ser tratados como a
mesma palavra, por exemplo. Você provavelmente verá que sua solução para o exercício 8 da
lista 6 (sobre strings) é útil para resolver este problema.'''
import sys
from collections import Counter


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as arquivo:
            conteudo = arquivo.readlines()
            texto = ""
            for i in conteudo:
                texto += i.replace("\n", " ")
            traducao = str.maketrans("", "", ".,:?!/()0123456789")
            texto_sem_pontuacao = texto.translate(traducao)
            texto = texto_sem_pontuacao.split()
            frequencias = Counter(texto)
            maior_freq = max(frequencias, key= frequencias.get)
            print(f'A palavra com maior frequencia no arquivo {sys.argv[1]} é "{maior_freq}"')

    except Exception as e:
        print(f"Ocorreu algo inesperado! Erro: {e}")
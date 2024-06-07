# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 07

'''Uma técnica que pode ser usada para quebrar formas simples de
encriptação é a análise de frequência. Essa análise examina o texto encriptado para
determinar quais caracteres são mais frequentes. Depois ela tenta mapear as letras mais
comuns na língua portuguesa, tais como A, R, S, etc.. para os caracteres mais frequentes do
texto encriptado.
Escreva um programa Python que faz a primeira parte deste processo, determinando e
exibindo a frequência (percentual) de ocorrência de todas as letras em um arquivo. Ignore
espaços, números e sinais de pontuação. Seu programa não deve diferenciar letras
maiúsculas e minúsculas (portento deve tratar A e a como sendo a mesma letra). O usuário
deve fornecer o nome do arquivo como argumento em linha de comando. O programa deve
exibir uma mensagem de erro caso não consiga ler o arquivo ou caso não tenha sido passado
nenhum argumento para o programa em linha de comando.'''
import sys
from collections import Counter


if __name__ == "__main__":
    try:
        with open(sys.argv[1], "r") as arquivo:
            conteudo = arquivo.readlines()
            texto = ""
            for i in conteudo:
                texto += i.replace("\n", " ")
                
            traducao = str.maketrans("", "", ".,:?!/()0123456789 ")
            texto_sem_pontuacao = texto.translate(traducao)
            frequencias = Counter(texto_sem_pontuacao)
            total_caracteres = sum(frequencias.values())

            print(f"Percentual de frequência de cada caractere no arquivo {sys.argv[1]}")
            for caractere, frequencia in frequencias.items():
                freq_percentual = (frequencia / total_caracteres) * 100
                print(f"{caractere}: {freq_percentual:.2f}%")

    except Exception as e:
        print(f"Ocorreu algo inesperado! Erro: {e}")
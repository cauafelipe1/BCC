# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 10

'''O romance “Gadsby”, de Ernest Vincent Wright, tem mais de 50.000
palavras. Embora 50.000 palavras não sejam normalmente notáveis para um romance, neste
caso é porque nenhuma das palavras do livro usa a letra “e”. Isso é particularmente notável
quando se considera que "e" é a letra mais comum em inglês. Escreva um programa que leia
uma lista de palavras de um arquivo e determine qual proporção das palavras usam cada letra
do alfabeto. Exibe o resultado para todas as 26 letras. Inclua uma mensagem adicional
identificando a letra usada na menor quantidade de palavras. Seu programa deve ignorar
quaisquer sinais de pontuação e deve tratar letras maiúsculas e minúsculas como
equivalentes.'''

import string, sys

if __name__ == "__main__":
    arquivo_entrada = sys.argv[1]
    try:
        with open(arquivo_entrada, "r") as arquivo:
            palavras = arquivo.read().split()

        total_palavras = len(palavras)
        contagem_letras = {letra: 0 for letra in string.ascii_lowercase}
        
        for palavra in palavras:
            palavra_normalizada = ''.join(char.lower() for char in palavra if char.isalpha())
            letras_unicas = set(palavra_normalizada)
            for letra in letras_unicas:
                if letra in contagem_letras:
                    contagem_letras[letra] += 1
        
        proporcoes_letras = {letra: contagem / total_palavras for letra, contagem in contagem_letras.items()}
        letra_menos_usada = min(proporcoes_letras, key=proporcoes_letras.get)

        print(f"Proporções das letras no arquivo {arquivo_entrada}:")
        for letra, proporcao in proporcoes_letras.items():
            print(f'palavras que usam a letra {letra}: {proporcao:.2%}')
        
        print(f'A letra usada na menor quantidade é: {letra_menos_usada}, usada em {proporcoes_letras[letra_menos_usada]:.2%} palavras.')
    
    except Exception as e:
        print(f"Ocorreu algo inesperado! Erro: {e}")

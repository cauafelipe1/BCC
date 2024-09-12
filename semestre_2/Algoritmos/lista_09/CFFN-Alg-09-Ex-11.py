# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 11

'''Um corretor ortográfico pode ser uma ferramenta útil para pessoas que
têm dificuldade em escrever palavras corretamente. Neste exercício, você escreverá um
programa que lê um arquivo e exibe todas as palavras com erros ortográficos contidas nele.
Palavras com erros ortográficos serão identificadas comparando cada palavra do arquivo com
uma lista de palavras conhecidas do Português. Quaisquer palavras no arquivo do usuário que
não aparecerem na lista de palavras conhecidas serão relatadas como erros ortográficos. O
usuário deve fornecer como parâmetro de linha de comando o nome do arquivo para verificar
se há erros de ortografia. Seu programa deve exibir uma mensagem de erro apropriada se o
parâmetro da linha de comando estiver ausente. Uma mensagem de erro também deve ser
exibida se o seu programa não conseguir abrir o arquivo do usuário. Use a solução do
exercício 8 da lista 6 ao criar a solução para este exercício, de forma que palavras seguidas
de vírgula, ponto ou outro sinal de pontuação não sejam relatadas como erros ortográficos.
Ignore a capitalização das palavras ao verificar a ortografia. No google classroom há um
arquivo texto com todas as palavras do Português Brasileiro para você usar neste exercício.'''

if __name__ == "__main__":
    arquivo_entrada = input("Insira o nome do arquivo de entrada: ")
    try:
        with open(arquivo_entrada, "r") as arquivo:
            conteudo = arquivo.readlines()
            texto = ""
            for i in conteudo:
                texto += i.replace("\n", " ")
                
            traducao = str.maketrans("", "", ".,:?!#/()0123456789")
            texto_sem_pontuacao = texto.translate(traducao)
            lista_de_palavras = texto_sem_pontuacao.split()
            
            erros_ortograficos = []
            for i in lista_de_palavras:
                if i in open('Palavras_portugues_br-utf8.txt').read():
                    continue
                else:
                    erros_ortograficos.append(i)
            if not erros_ortograficos:
                print(f"O arquivo {arquivo_entrada} não possui erros ortográficos!")
            else:
                print(f"Palavras com erro ortográfico no arquivo {arquivo_entrada}:")
                for i in erros_ortograficos:
                    print(i)
    except Exception as e:
        print(f"Ocorreu algo inesperado! Erro: {e}")
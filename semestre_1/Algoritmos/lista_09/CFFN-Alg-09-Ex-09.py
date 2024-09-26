# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 09
'''Python usa o caractere # para marcar o início de um comentário.
O comentário termina no final da linha que contém o caractere #. Neste exercício, você deve
criar um programa que remove todos os comentários de um arquivo-fonte Python. Verifique
cada linha no arquivo para determinar se um caractere # está presente. Se for, então seu
programa deve remover todos os caracteres do caractere # até o final da linha (ignoraremos a
situação em que o caractere de comentário ocorre dentro de uma string). Salve o arquivo
modificado usando um novo nome que será inserido pelo usuário. O usuário também irá inserir
o nome do arquivo de entrada. Certifique-se de que uma mensagem de erro apropriada seja
exibida se for encontrado um problema ao acessar os arquivos.
'''

if __name__ == "__main__":
    arquivo_entrada = input("Insira o arquivo de entrada: ")
    arquivo_saida = input("Insira o arquivo de saída:")
    try:
        with open(arquivo_entrada, "r") as arquivo:
            conteudo = arquivo.readlines()
            texto = ""
            print(conteudo)

        with open(arquivo_saida, "w") as novo_arquivo:
            for i in conteudo:
                if i[0] == "#":
                    continue
                else:
                    novo_arquivo.write(i)

        with open(arquivo_saida, "r") as arquivo:
            conteudo = arquivo.readlines()
            print(f"Conteúdo do arquivo {arquivo_saida} (arquivo de saída):")
            for i in conteudo:
                print(i)

    except Exception as e:
        print(f"Ocorreu algo inesperado! Erro: {e}")
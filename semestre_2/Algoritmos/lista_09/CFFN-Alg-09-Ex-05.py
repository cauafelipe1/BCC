# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 05

'''Escreva um programa Python que adicione números de
linhas em um arquivo. O programa deve receber do usuário os nomes do arquivo de entrada e
do arquivo de saída (que será um novo arquivo criado pelo programa). Cada linha do arquivo
de saída deve começar com leu número, seguido de dois pontos, um espaço em branco,
seguido do conteúdo da linha do arquivo original.'''

if __name__ == "__main__":
    arquivo_entrada = input("Insira o arquivo de entrada: ")
    arquivo_saida = input("Insira o arquivo de saída:")
    try:
        with open(arquivo_entrada, "r") as arquivo:
            conteudo = arquivo.readlines()
        with open(arquivo_saida, "w") as novo_arquivo:
            for i, linha in enumerate(conteudo):
                novo_arquivo.write(f"leu {i+1}: {linha}")
        with open(arquivo_saida, "r") as arquivo:
            conteudo = arquivo.readlines()
            print(f"Conteúdo do arquivo {arquivo_saida} (arquivo de saída):")
            for i in conteudo:
                print(i)
    except Exception as e:
        print(f"Parece que houve algum problema! Erro: {e}")

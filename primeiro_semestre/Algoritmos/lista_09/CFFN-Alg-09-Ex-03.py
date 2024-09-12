# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 03

'''Os sistemas operacionais baseados em Unix
normalmente também possuem um comando chamado tail, que exibe as 10 últimas linhas
de um arquivo cujo nome é passado como argumento em linha de comando. Escreva um
programa Python que apresente o mesmo comportamento. O programa deve exibir uma
mensagem de erro caso não exista o arquivo ou caso não tenha sido passado nenhum
argumento para o programa em linha de comando.'''
import sys
from subprocess import run, PIPE

if __name__ == "__main__":
# método 1
    print("*"*30, "\nMétodo 1")
    print(f"Número de argumentos: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("Nenhum argumento além do próprio script foi passado")
    else:
        for i, arg in enumerate(sys.argv):
            print(f"Argumento {i}: {arg}")
            if i == 0:
                continue
            try:
                arquivo = open(f"{arg}")
                conteudo = arquivo.readlines()
                print(f"Conteúdo do arquivo {arg} (10 últimas linhas):")
                for x in conteudo[-10:]:
                    x = x.replace("\n", "")
                    print(x)
            except Exception as e:
                print(f"Parece que o arquivo {arg} nao foi encontrado! Erro: {e}")

# método 2
    print("*"*30, "\nMétodo 2")
    print(f"Número de argumentos: {len(sys.argv)}")
    if len(sys.argv) == 1:
        print("Nenhum argumento além do próprio script foi passado")
    else:
        for i, arg in enumerate(sys.argv):
            print(f"Argumento {i}: {arg}")
            if i == 0:
                    continue
            try:
                print(f"Conteúdo do arquivo {arg} (10 últimas linhas):")
                comando = ['tail', f'{arg}']
                executador = run(comando, stderr=PIPE, check=True, text=True)  
                print()
            except Exception as e:
                print(f"Parece que o arquivo {arg} não foi encontrado! Erro: {e}")
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-09
# Exercício: 04

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
                print(f"Conteúdo do arquivo {arg}:")
                for x in conteudo:
                    x = x.replace("\n", "")
                    print(x)
            except Exception as e:
                print(f"Parece que o arquivo {arg} não foi encontrado OU não pôde ser lido! Erro: {e}")

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
                print(f"Conteúdo do arquivo {arg}:")
                comando = ['cat', f'{arg}']
                executador = run(comando, stderr=PIPE, check=True, text=True)  
                print()
            except Exception as e:
                print(f"Parece que o arquivo {arg} não foi encontrado OU não pôde ser lido! Erro: {e}")
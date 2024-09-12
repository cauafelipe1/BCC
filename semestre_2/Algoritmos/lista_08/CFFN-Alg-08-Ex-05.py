# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 05

'''Escreva um programa que leia os valores numéricos do usuário
até que uma linha em branco seja inserida. Exiba a soma total de valores inseridos pelo
usuário (ou 0,0 se o primeiro valor inserido for uma linha em branco). Conclua esta tarefa
usando recursão. Seu programa não pode usar nenhum laço de repetição.'''

def soma_recursiva():
    n = input("Insira um valor numérico (enter para encerrar): ")
    if n == "":
        return 0.0
    else:
        return float(n) + soma_recursiva()
def main():
    total = soma_recursiva()
    return print(f"Soma dos valores inseridos: {total}")

if __name__ == "__main__":
    main()
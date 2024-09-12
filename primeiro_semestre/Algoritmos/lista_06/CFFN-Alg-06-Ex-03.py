# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 03

'''Ao analisar os dados coletados como parte de um experimento
científico, pode ser desejável remover os valores mais extremos antes de realizar outros
cálculos. Escreva uma função que tenha uma lista de valores e um número inteiro não
negativo, n, como seus parâmetros. A função deve criar uma nova cópia da lista com os n
maiores elementos e os n menores elementos removidos. Em seguida, ele deve retornar a
nova cópia da lista como o único resultado da função. A ordem dos elementos na lista
retornada não precisa coincidir com a ordem dos elementos na lista original.'''

def ordenar(dados, n):
    dados.sort()
   
    i = 1
    for i in range(n):
        dados.remove(dados[0])
    for i in range(n):
        dados.remove(dados[-1])
    
    return dados
        


def main():

    dados = []
    while True:
        try:
            x = int(input("Insira o valor inteiro (0 para encerrar):"))
            if x == 0:
                while True:
                    try: 
                        n = int(input("Insira o número de n elementos extremos que deseja remover: "))
                        if n >=0:
                            break
                        else:
                            print("Insira um valor inteiro não negativo!!")
                            continue
                    except ValueError:
                        print("Insira um valor inteiro não negativo!!")
                break
            else:
                dados.append(x)
        except ValueError:
            print("Insira um valor inteiro!!")
            continue
    return print(f"Dados ordenados: {ordenar(dados, n)}")

if __name__ == "__main__":
    main()
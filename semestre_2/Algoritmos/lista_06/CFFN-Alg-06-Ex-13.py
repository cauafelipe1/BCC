# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 13

'''A biblioteca padrão de funções do Python possui um método
chamado count, que determina quantas vezes um determinado valor ocorre em uma lista.
Neste exercício você deve criar uma nova função chamada countRange que deve determinar
e retornar a quantidade de elementos em uma lista que são maiores ou iguais a um valor
mínimo e menores que um valor máximo. Sua função deve receber três parâmetros: a lista (de
números), o valor mínimo e o valor máximo. Ela deve retornar um valor inteiro maior ou igual a
zero. Escreva uma função main demonstrando o funcionamento de sua função.'''

def countRange(dados, minimo, maximo):
    contador = 0
    for i in dados:
        if (i >= minimo) and (i < maximo):
            contador += 1
    return contador

def coletar_dados():
    dados = []
    while True:
        try:
            x = input("Insira valores inteiros para a lista (tecle enter para encerrar):")
            if x == "":
                break
            else:
                dados.append(int(x))
        except ValueError:
            print("Digite um valor inteiro!")
            continue

    while True:
        try:
            minimo = int(input("Digite um valor mínimo: "))
            maximo = int(input("Digite um valor máximo: "))
            if minimo < maximo:
                break
            else:
                print("O número mínimo deve ser menor que o máximo!!")
                continue
        except ValueError:
            print("Insira apenas valores inteiros!")
            continue
   
    return dados, minimo, maximo
def main():
    pacote_de_dados = coletar_dados()
    result = countRange(pacote_de_dados[0], pacote_de_dados[1], pacote_de_dados[2])
    return print(f"Conforme os dados inseridos, existem {result} valores entre os valores mínimo e máximo!")




if __name__ == "__main__":
    main()
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 04

'''Escreva uma função que recebe três números como parâmetros e
retorna o valor da mediana desses parâmetros como seu resultado. Inclua um programa
principal que lê três valores do usuário e exibe a mediana destes valores.'''

def mediana(x,y ,z):
    valores = [x, y, z]
    mediana = (x + y + z) - max(valores) - min(valores)
    x = print(f"A mediana dos números {x}, {y} e {z} é {mediana}!")
    return x 

def main():
    x = float(input("Insira o primeiro valor: "))
    y = float(input("Insira o segundo valor: "))
    z = float(input("Insira o terceiro valor: "))
    return mediana(x, y, z)

if __name__ == "__main__":
    main()
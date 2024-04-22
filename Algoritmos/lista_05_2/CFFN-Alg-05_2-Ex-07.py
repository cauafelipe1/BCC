# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 07

'''válido? Se você possui 3 canudos, possivelmente de tamanhos diferentes, pode ou
não ser possível montar um triângulo juntando as pontas dos canudos. Por exemplo, se todos
tiverem 15 cm de comprimento, facilmente você pode formar um triângulo equilátero. Porém,
se um canudo tem 15 cm e os outros dois tem 5 cm cada, você não consegue formar o
triângulo. Generalizando: se o comprimento de um canudo é maior ou igual que a soma dos
comprimentos dos outros dois outros canudos, eles não podem formar um triângulo. Caso
contrário, podem formar um triângulo. Escreva uma função que determina se 3 comprimentos
podem ou não formar um triângulo. A função deve receber 3 parâmetros e retornar um valor
lógico. Além disso, escreva um programa que leia 3 valores do usuário e demonstre o
comportamento desta função.'''

def triangular(x, y, z):
    if (x >= (y + z)) or (y >= (x + z)) or (z >= (x + y)):
        return False
    else:
        return True
    
def main():
    x = float(input("Insira o valor do 1º canudo: "))
    y = float(input("Insira o valor do 2º canudo: "))
    z = float(input("Insira o valor do 2º canudo: "))
    if triangular(x, y, z):
        x = "Os canudos fornecidos podem formar um triângulo!"
    else:
        x = "Os canudos fornecidos não podem formar um triângulo!"
    return print(x)

if __name__ == "__main__":
    main()
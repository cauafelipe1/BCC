# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 02

'''Escreva uma função Python que recebe dois conjuntos de números
inteiros M e N e retorna uma lista com sua diferença simétrica em ordem ascendente. O termo
diferença simétrica denota os valores que existem nos conjuntos M ou N, mas não existem em
ambos os conjuntos simultaneamente. Por exemplo, para os conjuntos M = {2, 4, 5, 9} e N =
{2, 4, 11, 12}, a resposta deveria ser [5, 9, 11, 12].'''

def diferenca_simetrica(m, n):
    result = m.symmetric_difference(n)
    return sorted(result)

def coletar_dados(valor):
    conjunto = set()
    while True:
        try:
            x = input(f"Insira os valores de {valor} (enter para finalizar):")
            if x == "":
                break
            else:
                conjunto.add(int(x))
        except:
            print("Insira apenas valores inteiros!!")
    return conjunto

def main():
    conjunto_m = coletar_dados("M")
    conjunto_n = coletar_dados("N")
    return print(diferenca_simetrica(conjunto_m, conjunto_n))

if __name__ == "__main__":
    main()
# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 07

'''Escreva uma função que converte um número
decimal (base 10) em binário (base 2). A função deve receber como parâmetro o número
inteiro decimal (q) e, em seguida, deve realizar a conversão usando o algoritmo de divisão
mostrado abaixo. Quando o algoritmo for concluído, o resultado contém a representação
binária do número, que deve ser retornada pela função como uma string.
DecBinIterativo(q)
    result ← ””
    repeat
        r ← q%2
        result ← str(r) + result
        q ← q//2
    until q == 0;
    return result'''

def DecBinIterativo(q):
    result = ""
    while q != 0:
        r = q % 2
        result = str(r) + result
        q = q//2
    return result
def main():
    q = int(input("Insira um valor inteiro decimal positivo (base 10): "))
    return print(f"O número decimal {q} é equivalente ao {DecBinIterativo(q)} em binário")

if __name__ == "__main__":
    main()
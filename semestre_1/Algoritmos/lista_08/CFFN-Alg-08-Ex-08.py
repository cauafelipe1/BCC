# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 08

'''No exercício anterior, você escreveu um programa
que usava um laço de repetição para converter um número decimal para sua representação
binária. Neste exercício, você executará a mesma tarefa usando recursividade.
Escreva uma função recursiva que converta um número decimal não negativo em binário.
Trate 0 e 1 como casos básicos que retornam uma string contendo o dígito apropriado. Para
todos os outros inteiros positivos, n, você deve calcular o próximo dígito usando o operador de
resto e, em seguida, fazer uma chamada recursiva para calcular os dígitos de n // 2.
Finalmente, você deve concatenar o resultado da chamada recursiva (que será um string) e o
próximo dígito (que você precisará converter em uma string) e retornar essa string como o
resultado da função.
Escreva um programa principal que use sua função recursiva para converter um inteiro não
negativo inserido pelo usuário de decimal para binário. Seu programa deve exibir uma
mensagem de erro apropriada se o usuário inserir um valor negativo.'''

def DecBinRecursivo(q):
    if q == 0:
        result = ""
    else:
        result = DecBinRecursivo(q // 2) + str(q % 2)
    return result
def main():
    q = int(input("Insira um valor inteiro decimal positivo (base 10): "))
    if q < 0:
        return print(f"ERRO!! {q} é um número negativo e este programa não suporta sua conversão para binário.")
    elif DecBinRecursivo(q) == "":
        return print(f"O número decimal {q} é equivalente a 0 em binário")
    return print(f"O número decimal {q} é equivalente ao {DecBinRecursivo(q)} em binário")

if __name__ == "__main__":
    main()
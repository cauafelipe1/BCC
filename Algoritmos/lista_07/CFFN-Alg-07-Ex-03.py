# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 03

'''Escreva uma função chamada buscaReversa, que encontra todas as chaves
de um dicionário que estão mapeadas para um determinado valor. A função deve receber
como parâmetros um dicionário e um valor para ser buscado no dicionário. A função deve
retornar uma lista (possivelmente vazia) com as chaves encontradas. Escreva uma função
main para demonstrar sua função. Note que a função deve funcionar independentemente de
ela retornar múltiplas chaves, uma única chave, ou nenhuma chave.'''

def buscaReversa(dicionario, valor_procurado):
    chaves_encontradas = []
    for chave, valor in dicionario.items():
        if valor == valor_procurado:
            chaves_encontradas.append(chave)
    return chaves_encontradas

def main():
    exemplo = {"chaves": "fagundes", "charles": 12, "charleco": "morto", "dia": 12, "mebous": 12, "sarney": 12}
    valor_procurado = 12
    return print(buscaReversa(exemplo, exemplo["dia"]))

if __name__ == "__main__":
    main()
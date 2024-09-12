# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-08
# Exercício: 10

'''A codificação run-length é uma técnica simples de compressão de
dados que pode ser eficaz quando valores repetidos ocorrem em posições adjacentes dentro
de uma lista. Compressão é obtida substituindo grupos de valores repetidos por uma cópia do
valor, seguido pelo número de vezes que o valor deve ser repetido. Por exemplo, a lista ["A",
"A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B",
"A", "A", "A", "A", "A", "A", "B"] seria comprimida como ["A", 12, "B", 4, "A",
6, "B", 1]. A descompressão é realizada replicando cada valor da lista o número de vezes
indicado.
Escreva uma função recursiva que descompacte uma lista codificada run-lenght. Sua função
recursiva deve ter uma lista compactada em run-lenght como seu único parâmetro. Ela deve
retornar a lista descompactada como seu único resultado. Crie um programa principal que
exibe uma lista codificada em run-lenght e o resultado da decodificação.'''

def descompactar_run_length(lista_compactada):
    if not lista_compactada:
        return []
    
    if len(lista_compactada)%2 != 0:
        raise ValueError("A lista não está corretamente compactada, pois seus valores devem ser pares, contendo para cada letra, um número representando quantas vezes ela aparece na lista.")
    
    valor = lista_compactada[0]
    contagem = lista_compactada[1] 
    
    descompactado = [valor] * contagem
    return descompactado + descompactar_run_length(lista_compactada[2:])
def main():
    lista_compactada = ["A", 12, "B", 4, "A", 6, "B", 1]
    print(f"Exemplo de lista compactada: {lista_compactada}")
    lista_descompactada = descompactar_run_length(lista_compactada)
    return print(f"Lista descompactada: {lista_descompactada}")
    

if __name__ == "__main__":
    main()
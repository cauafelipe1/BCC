# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 08

'''Uma cartela de bingo vencedora deve conter
uma linha (ou coluna ou diagonal) com 5 números que foram sorteados. Normalmente, nas
cartelas de papel, os jogadores fazem um X sobre o número sorteado. Na sua implementação
(no seu dicionário representando a cartela), vamos substituir por 0 o número que foi sorteado.
Escreva uma função que receba como único parâmetro um dicionário representando uma
cartela. Se a cartela contiver uma linha, coluna ou diagonal preenchida com zeros, a função
deve retornar True. Caso contrário deve retornar False. Crie um programa que demonstre o
funcionamento da sua solução criando e exibindo várias cartelas de bingo e indicando se cada
uma é ou não é vencedora. Você deve mostrar pelo menos uma cartela com linha horizontal,
uma com linha v ertical, uma com diagonal e por fim uma com alguns zeros cruzados, mas
que não é vencedora. Você pode usar sua solução do problema anterior como ponto de
partida para este exercício. Dica: como a cartela não tem números negativos, encontrar uma
sequencia de 5 zeros é análogo a descobrir se a soma de uma sequencia de 5 números é
igual a zero. Talvez você ache mais fácil fazer desse jeito.'''

from random import sample

def criar_cartela():
    cartela = {
        'B': sample(range(1, 16), 5),
        'I': sample(range(16, 30), 5),
        'N': sample(range(31, 45), 5),
        'G': sample(range(46, 60), 5),
        'O': sample(range(61, 75), 5)
    }
    return cartela

def exibir_cartela(cartela):
    print("-"*35)
    print("| B\tI\tN\tG\tO |")
    print("-"*35) 

    for i in range(5):
        for letra in 'BINGO':
            if letra == "B":
                print(f"|{cartela[letra][i]:2}", end="\t")
            elif letra == "O":
                print(f"{cartela[letra][i]:2}|")
            else:    
                print(f"{cartela[letra][i]:2}", end="\t")
    print("-"*35)

def cartela_vencedora(cartela):
    for i in range(5):
        if all(cartela[letra][i] == 0 for letra in 'BINGO'):
            return True
    
    for letra in 'BINGO':
        if all(cartela[letra][i] == 0 for i in range(5)):
            return True
    
    if all(cartela[letra][i] == 0 for i, letra in enumerate('BINGO')):
        return True
    
    if all(cartela[letra][4 - i] == 0 for i, letra in enumerate('BINGO')):
        return True
    
    return False

def main():
    cartela1 = criar_cartela()
    cartela1['B'][0] = cartela1['I'][1] = cartela1['N'][2] = cartela1['G'][3] = cartela1['O'][4] = 0
    
    cartela2 = criar_cartela()
    cartela2['B'][0] = cartela2['B'][1] = cartela2['B'][2] = cartela2['B'][3] = cartela2['B'][4] = 0  
    
    cartela3 = criar_cartela()
    cartela3['B'][0] = cartela3['I'][0] = cartela3['N'][0] = cartela3['G'][0] = cartela3['O'][0] = 0  
    
    cartela4 = criar_cartela()
    cartela4['B'][0] = cartela4['I'][1] = cartela4['N'][3] = cartela4['G'][4] = cartela4['O'][4] = 0  
    
    cartelas = [cartela1, cartela2, cartela3, cartela4]

    for i, cartela in enumerate(cartelas ):
        print(f"\nCartela {i + 1}:")
        exibir_cartela(cartela)
        if cartela_vencedora(cartela):
            print("BINGO! Cartela vencedora!!")
        else:
            print("Mais sorte na próxima! Essa não é uma cartela vencedora..")
if __name__ == "__main__":
    main()

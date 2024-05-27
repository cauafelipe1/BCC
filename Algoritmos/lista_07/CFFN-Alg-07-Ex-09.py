# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 09

'''Neste exercício você vai simular o jogo de Bingo para apenas uma cartela.
Começa gerando uma lista de todas as chamadas válidas de bingo (B1 até O75). Depois que
a lista estiver pronta, você pode embaralhar seus elementos chamando a função shuffle do
módulo random do Python. Então seu programa deve ir utilizando os valores da lista para
anunciar os números sorteados e zerar os números correspondentes na cartela até que ela
contenha uma linha, coluna ou diagonal zerada. No seu programa principal, faça uma
simulação de 1.000 partidas (sempre com uma nova cartela) e mostre o número mínimo, o
máximo e a média de chamadas até que se tenha uma cartela vencedora. Utilize seu código
dos dois exercícios anteriores e não se esqueça de criar novas funções sempre que você
identificar algum procedimento que pode ser melhor organizado dentro de uma função.'''
import random

def criar_cartela():
    cartela = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
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

def eh_vencedora(cartela):

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

def gerar_chamadas_bingo():
    chamadas = [f"{letra}{num}" for letra, inicio in zip("BINGO", range(1, 76, 15)) for num in range(inicio, inicio + 15)]
    random.shuffle(chamadas)
    return chamadas

def atualizar_cartela(cartela, chamada):
    letra, numero = chamada[0], int(chamada[1:])
    for i in range(5):
        if cartela[letra][i] == numero:
            cartela[letra][i] = 0
            break

def simular_jogo():
    cartela = criar_cartela()
    chamadas = gerar_chamadas_bingo()
    for i, chamada in enumerate(chamadas):
        atualizar_cartela(cartela, chamada)
        if eh_vencedora(cartela):
            return i + 1  
    return len(chamadas)

def main():
    num_simulacoes = 1000
    resultados = [simular_jogo() for _ in range(num_simulacoes)]
    min_chamadas = min(resultados)
    max_chamadas = max(resultados)
    media_chamadas = sum(resultados) / num_simulacoes
    
    print(f"Minimo: {min_chamadas}")
    print(f"Medio: {media_chamadas:.2f}")
    print(f"Máximo: {max_chamadas}")


if __name__ == "__main__":
    main()
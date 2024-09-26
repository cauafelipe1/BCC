# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 11

'''Para ganhar o prêmio da mega-sena, é necessário acertar todos os 6 números
em seu bilhete com os 6 números entre 1 e 60 sorteados pelo organizador da loteria. Escreva
um programa que gere uma seleção aleatória de 6 números para um bilhete de mega-sena.
Certifique-se de que não haja números repetidos entre os sorteados. Exiba os números em
ordem crescente.'''
from random import randint

def gerar_bilhete():
    bilhete = []
    while len(bilhete) < 6:
        n = randint(1,60)
        if n not in bilhete:
            bilhete.append(n)
    
    bilhete.sort()

    return print(f"Bilhete com números aleatórios da mega-sena: {bilhete}")
    
def main():
    return gerar_bilhete()




if __name__ == "__main__":
    main()
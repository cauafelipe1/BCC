# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 06

'''Proposta: Um bit de paridade é um mecanismo para detecção de erros em dados
transmitidos por uma conexão não confiável, como linha telefônica por exemplo. A idéia básica
é que, a cada grupo de 8 bits, seja acrescentado um bit adicional de forma que erros em bits
individuais possam ser detectados.
Os bit de paridade podem ser computados para paridade par ou paridade ímpar. Se for usada
paridade par, então o bit de paridade a ser transmitido deve ser tal que o número total de bits
“1” transmitidos (8 bits de dados + 1 bit de paridade) é par. Se for utilizada paridade ímpar, o
número total de bits “1” transmitidos deve ser ímpar.
Escreva um programa Python que compute o bit de paridade para grupos de 8 bits fornecidos
pelo usuário utilizando paridade par. Seu programa deve ler strings contendo 8 bits (portanto
as strings vai ser sequencias de 8 caracteres 0 ou 1) até que o usuário entre com uma linha
em branco. Logo após o usuário fornecer cada string, seu programa deve exibir uma
mensagem informando se o bit de paridade deve ser 0 ou 1. O programa também deve exibir 
uma mensagem de erro caso o usuário entre com algo que não seja a sequência de 8 bits'''

while True:
    try:
        bits = input("Forneça um grupo contendo 8 bits (enter para encerrar o programa): ")
        if bits == "":
            break
        if len(bits) != 8 or bits.count("0") + bits.count("1") != 8:
            print("Insira um valor válido!!")
            pass

        else:
            paridade = 1

            if bits.count("1") % 2 == 0:
                paridade = 0
                
            print(f"A sequencia de bits {bits} tem como bit de paridade {paridade}")
        
    except ValueError:
        print("Insira um valor válido!!")
        pass
    
    
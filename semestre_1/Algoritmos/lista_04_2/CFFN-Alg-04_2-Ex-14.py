# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 14

'''Proposta: Escreva um programa Python que converte um número binário (base 2) para
decimal (base 10). Seu programa deve iniciar lendo um número binário como uma string. Então, ele
deve computar o número decimal equivalente processando cada dígito do número binário. Finalmente
seu programa deve exibir uma mensagem informando o número decimal calculado.'''


while True:
    try:
        binario_inserido = input("Digite um número binário: ")
        contador = 0
        binario_formatado = ""
        for x in binario_inserido:
            if x not in "01":
                if x in "23456789":
                    contador += 1
                else:
                    pass
            else: 
                binario_formatado += x
    
        if contador > 0:
              print("Insira um valor verdadeiramente binário!!")
              continue
        else:
            binario = int(binario_formatado)
            decimal = 0
            i = 0

            while(binario != 0):
                dec = binario % 10
                decimal = decimal + dec * 2**i
                binario = binario//10
                i += 1
            break                 
    except ValueError:
        print("Insira um valor válido!!")
        continue

print(f"O número {binario_inserido} é equivalente a {decimal} na casa decimal!")
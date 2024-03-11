# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 05

'''Proposta: Considere o software que controla uma máquina automática de compras.
Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.'''

print("=-"*30, "\nCalculando o troco")

troco = int(input("Insira um valor em centavos (0 a 99) que será trocado: "))

moeda_50 = troco//50
resto = troco%50

moeda_25 = resto//25
resto = troco%25

moeda_10 = resto//10
resto = troco%10

moeda_5 = resto//5
resto = troco%5

moeda_1 = resto

print("Para o troco, será necessária a seguinte quantidade de moedas:")
print(f"{moeda_50} de 50 centavos;")
print(f"{moeda_25} de 25 centavos;")
print(f"{moeda_10} de 10 centavos;")
print(f"{moeda_5} de 5 centavos;")
print(f"{moeda_1} de 1 centavo.")
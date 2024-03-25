# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 03

'''Proposta: Escreva um programa Python que mostre uma tabelade conversão
de temperaturas em graus Celsius e graus Fahrenheit. A tabela deve incluir em
suas linhas todas as temperaturas entre 0 e 100 graus Celsius que sejam múltiplas de 10
graus Celsius. Inclua os cabeçalhos apropriados e tabulações para suas colunas. Pesquise na
internet sobre a fórmula de conversão de temperaturas Celsius para Fahrenheit.'''

print("[Tabela de conversão de temperaturas]")

print("=-"*20)
print("Celsius\t\t\tFahrenheit")
for i in range(100+1):
    celsius = i
    fahrenheit = celsius * (9/5) + 32
    print(f"{celsius}°C\t\t\t{round(fahrenheit, 1)}°F")

print("=-"*20)
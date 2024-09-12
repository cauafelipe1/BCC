# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 14

'''Uma “data mágica” é uma data na qual a multiplicação do dia pelo mês é
igual aos dois últimos dígitos do ano. Por exemplo, 10 de junho de 1960 é uma data mágica
porque 10 vezes 6 é igual a 60, que são os dois últimos dígitos do ano. Escreva uma função
que determina se uma data é ou não mágica. A função deve receber 3 parâmetros inteiros
(dia, mês e ano), e retornar um valor lógico. Escreva um programa main que utilize sua função
para determinar e imprimir todas as datas mágicas do século XX. O exercício anterior pode ser
útil para resolver este problema.'''

def dataMagica(dia, mes, ano):
    ano = str(ano)
    ano = ano[2:]
    ano = int(ano)
    if dia * mes == ano:
        return True
    else:
        return False


def main():
    dia = int(input("Insira um dia: "))
    mes = int(input("Insira o mês: "))
    ano = int(input("Insira o ano: "))
    meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro","dezembro"]
    if dataMagica(dia, mes, ano):
        x = print(f"O dia {dia} de {meses[mes]} de {ano} é uma data mágica!")
    else:
        x = print(f"O dia {dia} de {meses[mes]} de {ano} não é uma data mágica!")

    return x

if __name__ == "__main__":
    main()
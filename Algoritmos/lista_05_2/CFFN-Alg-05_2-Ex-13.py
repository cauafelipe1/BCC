# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 13

'''Escreva uma função que determina quantos dias há em um determinado
mês. Sua função deve receber dois parâmetros: o mês como um número inteiro entre 1 e 12 e
o ano como um número inteiro de quatro dígitos. Certifique-se de que sua função retorne o
número correto de dias em fevereiro para os anos bissextos. Inclua um programa principal que
lê um mês e ano do usuário e exibe o número de dias naquele mês. O exercício 12 da lista 3
pode ajudá-lo a resolver esse problema.'''

def contarDias(mes, ano):
    dias = 31
    trinta_dias = [4, 6, 9, 11]

    if mes == 2:
        if eh_bissexto(ano):
            dias = 29
        else:
            dias = 28
    elif mes in trinta_dias:
        dias = 30
    
    return dias



def eh_bissexto(ano):
    if (ano % 4 == 0) and ((ano % 100 != 0) or (ano % 400 == 0)):
        return True
    else:
        return False
    

def main():
    mes = int(input("Insira o mês: "))
    ano = int(input("Insira o ano: "))
    meses = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro","dezembro"]
    x = print(f"O mês {mes} ({meses[mes]}) do ano {ano} possui {contarDias(mes, ano)} dias!")
    return x

if __name__ == "__main__":
    main()        
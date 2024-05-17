# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-06
# Exercício: 09

'''Escreva um programa que leia números do usuário até que uma
linha em branco seja inserida. Seu programa deve exibir a média de todos os valores inseridos
pelo usuário. Em seguida, o programa deve exibir todos os valores abaixo da média, seguidos
por todos os valores médios (se houver), seguidos por todos os valores acima da média. Uma
mensagem apropriada deve ser exibida antes de cada lista de valores.'''


def operacoes(dados):
    media = sum(dados)/len(dados)
    abaixo_da_media = []
    valores_medios = []
    acima_da_media = []
    
    for i in dados:
        if i < media:
            abaixo_da_media.append(i)
        elif i == media:
            valores_medios.append(i)
        else:
            acima_da_media.append(i)
            
    print(f"Média de valores: {media}")
    print(f"Valores abaixo da media: {abaixo_da_media}")
    print(f"Valores médios: {valores_medios}")
    print(f"Valores acima da média: {acima_da_media}")

def main():

    dados = []
    while True:
        try:
            x = (input("Insira um valor inteiro (tecle enter para encerrar):"))
            if x == "":
                break
            else:
                x = int(x)
                dados.append(x)
        except ValueError:
            print("Insira um valor inteiro!!")
            continue
    
    return operacoes(dados)
        
if __name__ == "__main__":
    main()
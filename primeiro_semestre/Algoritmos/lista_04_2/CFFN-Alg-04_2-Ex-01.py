# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 01

'''Proposta: Escreva um programa Python que calcula a média aritmética de um
conjunto de valores fornecidos pelo usuário. O usuário deve entrar com o valor 0 indicando
que não serão mais fornecidos novos valores. Seu programa deve exibir uma mensagem de
erro se o primeiro valor fornecido pelo usuário for 0.
Dica: o número 0 não deve ser incluído no cálculo da média, pois ele só serve para sinalizar
o final da entrada de dados.'''

print("[Média de um número indeterminado de notas]\n")

notas = []
i = 1
while True:
    try:
        n = input(f"Forneça a {i}ª nota (escreva 0 caso não queira mais inserir nenhuma nota): ")
        if n == "0":
            if len(notas) == 0:
                print("Você deve inserir pelo menos uma nota!!")
                continue
            else:
                break
        elif not (0 < float(n) <= 10):
            print("Insira um valor válido!!")
            continue
        else:
            notas.append(float(n))
            i += 1

    except ValueError:
        print("Você deve inserir uma nota válida!")
        continue

media = sum(notas)/len(notas)


print(f"\nNotas fornecidas:", end=" ")
print(*notas, sep=", ")

print(f"A média das notas fornecidas é: {media}")
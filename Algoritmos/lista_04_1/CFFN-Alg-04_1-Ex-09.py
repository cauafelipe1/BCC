# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.1
# Exercício: 09

'''Proposta: Parte 2 - Comando WHILE - faça todos os exercícios desta parte com "while":
9. Adapte seu programa da questão anterior para que ele receba uma quantidade indefinida de
notas até que o usuário pressione <enter> sem fornecer nenhuma nota.'''

print("=-"*30, "\n[Média de um número indeterminado de notas]")
notas = []
i = 1

while True:
    try:
        n = input(f"Forneça a {i}ª nota (ou pressione enter se já inseriu todas as notas): ")
        if n == "":
            break
        elif not (0 <= float(n) <= 10):
            print("Insira um valor entre 0 e 10!!")
            continue
        else:
            notas.append(float(n))
            i += 1

    except ValueError:
        print("Você deve inserir uma nota válida!")
        continue

media = (sum(notas))/len(notas)

print(f"\nA média das {len(notas)} notas fornecidas é {media}")
print("=-"*30)
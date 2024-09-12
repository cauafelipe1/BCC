# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 05

'''Duas palavras são anagramas se contiverem as mesmas letras, mas em ordens
diferentes. Por exemplo: “amor" e “roma" são anagramas porque cada uma delas contém um
"a", um "o", um "m" e um “r”. Crie uma função Python que recebe duas strings e retorna True
se elas forem anagramas, ou False caso contrário.'''

def anagramar(palavra1, palavra2):
    palavra1 = palavra1.lower()
    palavra2 = palavra2.lower()

    if len(palavra1) != len(palavra2):
        return False
    
    dicionario1 = {}
    dicionario2 = {}
    
    for letra in palavra1:
            if letra in dicionario1:
                dicionario1[letra] += 1
            else:
                dicionario1[letra] = 1
        
    for letra in palavra2:
        if letra in dicionario2:
            dicionario2[letra] += 1
        else:
            dicionario2[letra] = 1
    
    return dicionario1 == dicionario2

def main():
    palavra1 = input("Insira a primeira palavra: ")
    palavra2 = input("Insira a segunda palavra: ")
    if anagramar(palavra1, palavra2):
        return (print(f"As palavras {palavra1} e {palavra2} são anagramas!!"))
    return (print(f"As palavras {palavra1} e {palavra2} não são anagramas!!"))

if __name__ == "__main__":
    main()
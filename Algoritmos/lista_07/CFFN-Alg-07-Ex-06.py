# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-07
# Exercício: 06
'''A noção de anagramas pode ser estendida para múltiplas palavras.
Por exemplo: "William Shakespeare” e “I am a weakish speller” são anagramas se ignorarmos
se as letras são maiúsculas e também os espaços. Crie uma nova versão da sua função do
exercício anterior para verificar se duas frases são anagramas. Sua função deve
desconsiderar se as letras são maiúsculas ou minúsculas, ignorar espaços e sinais de
pontuação.'''

def anagramar(palavra1, palavra2):
    chars = ".!?:;,"
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    for i in palavra1:
        if i in chars:
            palavra1.replace(i, "")

    for i in palavra2:
        if i in chars:
            palavra2.replace(i, "")

    

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
        return (print(f"{palavra1} e {palavra2} são anagramas!!"))
    return (print(f"{palavra1} e {palavra2} não são anagramas!!"))

if __name__ == "__main__":
    main()
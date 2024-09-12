# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-05.2
# Exercício: 12

'''Neste exercício, você deve escrever uma função que determina
se uma senha é válida ou não. Definiremos uma boa senha como aquela que tem pelo menos
8 caracteres e contém pelo menos uma letra maiúscula, pelo menos uma letra minúscula e
pelo menos um número. Sua função deve retornar True se a senha passada a ela como seu
único parâmetro for válida. Caso contrário, ele deve retornar False. Inclua um programa
principal que lê a senha do usuário e informa se ela é ou não válida.'''

def verificador(senha):
    if len(senha) < 8:
        return False
    maiuscula = any(char.isupper() for char in senha)
    minuscula = any(char.islower() for char in senha)
    numero = any(char.isdigit() for char in senha)
    
    return maiuscula and minuscula and numero

def main():
    senha = input("Insira uma senha: ")
    if verificador(senha):
        x = print(f"A senha {senha} é válida!")
    else:
        x = print(f"A senha {senha} não é válida!")
    return x

if __name__ == "__main__":
    main()
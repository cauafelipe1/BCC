# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-04.2
# Exercício: 08

'''Proposta: Um dos primeiros exemplos conhecidos de criptografia foi utilizado pelo
imperador romano Julio César. César precisava fornecer instruções por escrito para seus
generais, mas não queria que seus inimigos descobrissem suas estratégias caso as
mensagens com as instruções fossem extraviadas. Com isso, ele acabou desenvolvendo o
que mais tarde ficou conhecido como a “cifra de César”.
A idéia por trás desta cifra é simples (e portanto não oferece proteção contra as técnicas
modernas de quebra de códigos). Cada letra da mensagem original é deslocada em 3
posições. Com isso, a letra A se torna letra D, B se torna E, C se torna F, e assim por diante. A
ultimas 3 letras do alfabeto são transformadas nas primeiras. X se torna A, Y se torna B e Z se
torna C. Caracteres que não são letras não são convertidos.
Escreva um program Python que implemente a cifra de César. Permita que o usuário forneça a
mensagem e a distância de deslocamento de letras (portanto não será o valor fixo de
deslocamento de 3 letras no alfabeto). Certifique-se que seu programa codifique corretamente
tanto letras maiúsculas quanto minúsculas. Seu programa também deve suportar valores
negativos de deslocamento de letras, assim ele pode ser usado tanto para codificar quanto
para decodificar mensagens.'''

mensagem = input("Digite uma mensagem qualquer: ")
deslocamento = int(input("Digite o deslocamento da mensagem que será codificada: "))

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

mensagem_criptografada = ""

for letra in mensagem:
    posicao = alfabeto.find(letra.upper())

    if posicao == -1:
        mensagem_criptografada += letra
        continue

    nova_posicao = (posicao + deslocamento) % len(alfabeto)
    nova_letra = alfabeto[nova_posicao]
    mensagem_criptografada += nova_letra.lower() if letra.islower() else nova_letra

print(f"Mensagem criptografada: {mensagem_criptografada}")

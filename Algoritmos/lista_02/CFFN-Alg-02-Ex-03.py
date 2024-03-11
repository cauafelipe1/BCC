# Aluno: Cauã Felipe de França Nascimento
# Lista: Alg-02
# Exercício: 03

'''Proposta: Tempo atual. A linguagem Python possui uma biblioteca de funções para lidar com tempo,
incluindo a função asctime no módulo time. Ela lê o tempo atual do Clock interno do
computador e o retorna em um formato legível. Escreva um programa que exiba a data e a
hora atuais. Seu programa não precisa obter qualquer entrada do usuário.'''

import datetime

tempo = datetime.datetime.now()
print(f"Este código foi executado em: {tempo}")
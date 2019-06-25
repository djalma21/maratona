# Crie um jogo do pedra, papel e tesoura de um jogador humano com a máquina.
# Capture o nome do jogador e quantidade de rodadas. A quantidade de rodadas
# deve ser maior que 1 e ímpar. O jogador deve escolher pelas jogadas 1 - Pedra,
# 2 - Papel, 3 - Tesoura. A máquina deverá fazer sua escolha automática e
# aleatoriamente. Faça as decisões necessárias pra decidir quem vence uma
# rodada. (Caso não conheça o jogo, pesquise na internet). Mantenha sempre o
# menu atualizado com o placar e as rodadas.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

nome = input('Insira seu nome:')

print("""Suas opções são:
[0] Pedra
[1] Papel
[2] Tesoura""")

jogador = int(input('Qual é sua jogada? '))
print('1')
sleep(0.6)

print('2')
sleep(0.6)

print('3')
sleep(0.6)

print('e já!!')
sleep(0.4)


print('-=' * 12)
print('O {}'.format(nome), 'jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=' * 12)

if jogador == 0:
    if computador == 0:
        print('Empate')
    elif computador == 1:
        print('Computador Vence')
    elif computador == 2:
        print('{} Vence'.format(nome))

elif jogador == 1:
    if computador == 0:
        print('{} Vence'.format(nome))
    elif computador == 1:
        print('Empate')
    elif computador == 2:
        print('Computador Vence')


elif jogador == 2:
    if computador == 0:
        print('Computador Vence')
    elif computador == 1:
        print('{} Vence'.format(nome))
    elif computador == 2:
        print('Empate')

else:
    print('Jogada Inválida!')

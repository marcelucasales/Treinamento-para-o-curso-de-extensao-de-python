from random import randint
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
jogador = int(input('0 - pedra - 1 - papel - 2 -tesoura:  '))
print('o computador escolheu {}'.format(itens[computador]))
print('Vc escolheu {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Vc ganhou')
    elif jogador == 2:
        print('Vc perdeu')
if computador == 1:
    if jogador == 0:
        print('Vc perdeu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Vc ganhou')
if computador == 2:
    if jogador == 0:
        print('yOU LOSE')
    elif jogador == 1:
        print('Vc ganhou')
    elif jogador == 2:
        print('EMPATE')

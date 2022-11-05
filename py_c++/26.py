from random import randint
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'pi':
        tipo = str(input('Par ou impar [p/i]: ')).strip().lower()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total {total}')
    if tipo in 'p':
        if total % 2 == 0:
            print('You win')
            v += 1
        else:
            print('You lose')
            break
    elif tipo in 'i':
        if total % 2 != 0:
            print('You win')
            v += 1
        else:
            print('You lose')
            break
    print('Quer jogar novamente? ')
print(f'Voce ganhou tantas {v}')        

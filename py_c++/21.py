primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razao: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(primeiro, end=" ")
        primeiro += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos vc quer mostrar mais: '))
print('Progressao finalizada com {} termos'.format(total))
print('Fim')
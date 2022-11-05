nume = list()
s = ' '
while True:
    n = int(input('Digite um numero: '))
    if n not in nume:
        nume.append(n)
    else:
        print('Número duplicado, não irei adicionar.')
    s = str(input('Deseja continuar? Sim[] Não[]: ')).strip().lower()[0]
    while s not in 'sn':
        print('Digite novamente.')
        s = str(input('Deseja continuar? Sim[] Não[]: ')).strip().lower()[0]
    if s in 'n':
        break
nume.sort()
print(nume)
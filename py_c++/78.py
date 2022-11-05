nume = [int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: '))]
print(nume)
nume.sort()
menor = nume[0]
maior = nume[4]
print(f'{maior} esta na posicoes ',end='')
for pos,valor in enumerate(nume):
    if valor == maior:
        print(f'...{pos}')
print(f'{menor} esta na posicoes ',end='')
for pos,valor in enumerate(nume):
    if valor == menor:
        print(f'...{pos}')
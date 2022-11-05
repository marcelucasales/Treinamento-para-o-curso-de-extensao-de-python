#questao 09
contf = 0
med = medf = 0.0
pessoa = {}
maior = {}
menor = {}
lista = []
for i in range(4):
    pessoa.clear()
    pessoa['nome'] = input('Digite o nome da pessoa: ')
    pessoa['altura'] = float(input('Digite sua altura: '))
    pessoa['sexo'] = input('Digite o sexo da pessoa: ').strip().lower()[0]
    lista.append(pessoa.copy())
    med += pessoa['altura']
    if 'f' in pessoa['sexo']:
        medf += pessoa['altura']
        contf += 1
    if i == 0:
        maior = pessoa.copy()
        menor = pessoa.copy()
    else:
        if pessoa['altura'] > maior['altura']:
            maior = pessoa.copy()
        if pessoa['altura'] < menor['altura']:
            menor = pessoa.copy()
med /= len(lista)
medf /= contf
print('A media de altura das pessoas foi: ', med,', já a média de alturas das mulheres foi: ', medf)
print(f'A maior altura das pessoas foi de {maior}')
print(f'A menor altura das pessoas foi de {menor}')

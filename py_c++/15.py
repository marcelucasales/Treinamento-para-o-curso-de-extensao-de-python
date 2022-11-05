cont = 0
id = 0
maior = 0
nome = 'maior'
for i in range(1,5):
    nome = str(input('Qual seu nome? '))
    sexo = str(input('Qual seu sexo? ')).lower()
    idade = int(input('Qual sua idade? '))
    id +=idade
    if sexo == 'masculino':
        if idade >= maior:
            n1 = nome
            maior = idade
    if sexo == 'feminino':
        if idade < 21:
            cont += 1
med = id/4
print('A media de idade e {}'.format(med))
print('O nome do homem mais velho e {} e sua idade: {}'.format(n1,maior))
print('Existe {} mulheres com menos de 21 anos'.format(cont))
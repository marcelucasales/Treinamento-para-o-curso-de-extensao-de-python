
sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('sexo invalido, digite novamente: ')).strip().upper()[0]
if sexo in 'Mm':
    print('masculino')
elif sexo in 'Ff':
    print('Feminino')
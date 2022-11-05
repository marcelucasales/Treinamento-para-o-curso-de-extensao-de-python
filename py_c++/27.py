homens = cont = mulheres = 0
while True:
    sexo = str(input('Qual seu sexo: ')).strip().lower()[0]
    idade = int(input('Qual a sua idade: '))
    if idade > 18:
        cont += 1
    if sexo not in 'mf':
        break
    elif sexo in 'm':
        homens += 1   
    elif sexo in 'f':
        if idade < 20:
            mulheres += 1
    loop = str(input('Deseja continuar? ')).strip().lower()[0]
    if loop in 'n':
        break
    while loop not in 'sn':
        loop = str(input('Deseja continuar? ')).strip().lower()[0]
print(f'{cont} pessoas tem mais de 18 anos, {homens} homens foram cadastrados, {mulheres} mulheres tem menos de 20 anos')
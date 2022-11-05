dados = list()
pessoas = list()
while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    s = str(input('Deseja continuar? Sim[] ou Não[]: ')).strip().lower()[0]
    if s in 'n':
        break
    elif s not in 'sn':
        print('Comando não encontrado.')
        s = str(input('Deseja continuar? Sim[] ou Não[]: ')).strip().lower()[0]
print(f'Foram cadastradas {len(pessoas)} pessoas')
for key,pessoa in enumerate(pessoas):
    if pessoas[key][1] >= 100:
        print(f'Meu nome: {pessoa[0]} e sou uma pessoa pesada com {pessoa[1]} Kg,',end=' ')
    elif pessoas[key][1] <= 60:
        print(f'Meu nome: {pessoa[0]} e sou uma pessoa leve com {pessoa[1]} Kg,',end=' ')
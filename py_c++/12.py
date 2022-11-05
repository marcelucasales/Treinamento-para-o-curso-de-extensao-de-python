from datetime import date
co = 0
cont = 0
for i in range(1,8):
    nas = int(input('Digite o seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - nas
    if idade >= 18:
        cont+=1
    else:
        co+=1
print('Sao {} pessoas de maiores de idade'.format(cont))
print('Sao {} pessoas de menores de idade'.format(co))

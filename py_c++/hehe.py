exp = str(input('Digite a expressao: '))
lista = []
cont = co = 0
for simbolo in exp:
    if simbolo == '(':
        cont += 1
    elif simbolo == ')':
        co += 1
if cont == co:
    print('Expressao valida')
else:
    print('Expressao invalida')
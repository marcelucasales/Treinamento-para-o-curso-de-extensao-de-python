#questao 03
def peso(x: list()) -> float:
    if x[0] > 6:
        x[0] = x[0] * 5
        return 5
    else:
        x[0] = x[0] * 2.5
        return 2.5
#main
dic = {}
dic['a'] = [float(input('Digite o valo de a: '))]
dic['b'] = [float(input('Digite o valo de b: '))]
dic['c'] = [float(input('Digite o valo de c: '))]
pesoa = peso(dic['a'])
pesob = peso(dic['b'])
pesoc = peso(dic['c'])
print('a média ponderada é {}'.format((dic['a'][0]+dic['b'][0]+dic['c'][0])/(pesoa+pesob+pesoc)))
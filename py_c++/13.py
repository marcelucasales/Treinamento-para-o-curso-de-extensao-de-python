frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
pa =''.join(palavras) #Substitui os espacos por ''
#inverso = ''
inverso = pa[::-1]
'''for i in range(len(pa)-1,-1,-1):
    inverso += pa[i]'''
if inverso==pa:
    print('palindromo')
else:
    print('Nao e palindromo')

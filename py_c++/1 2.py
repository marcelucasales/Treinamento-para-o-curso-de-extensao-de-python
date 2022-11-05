lanche = ('Hamburguer','Suco', 'Pizza', 'Pudim')
#for cont in lanche:
 #   print(f'Eu vou comer {cont}')
 #for cont in lanche:
 #   print('Eu vou comer {}'.format(cont))
#for i in range(0,len(lanche)):
#    print(f'Eu vou comer {lanche[i]}')
for i in range(0,len(lanche)):
    print('Eu vou comer {}'.format(lanche[i]))
print('Comi muito!')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')
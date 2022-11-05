preco = float(input('Qual o valor do produto: '))
cond = str(input('Qual a condicao de pagamento? '))
if cond == 'dinheiro':
    preco = preco - (preco*0.1)
    print('O novo valor do produto com desconto: {}'.format(preco))
elif cond == '1x no cartao':
    preco = preco - (preco*0.5)
    print('O novo valor do produto com desconto: {}'.format(preco))
elif cond == '2x no cartao':
    print('O valor do produto continua o mesmo: {}'.format(preco))
elif cond == '3x no cartao':
    preco += (preco*0.2)
    print('O novo valor do produto com juros: {}'.format(preco))

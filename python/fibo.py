# fibo
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, (a+b)

num = fib(10)
print(list(num))
'''
for n in num:
    print(f'{n}', end=' ')
'''
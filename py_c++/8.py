s = 0
for p in range(1,501):
    if p%2!=0 and p%3==0:
        s+=p
print(s)
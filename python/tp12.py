#questao 12
paisa = 90000000.0
paisb = 200000000.0
conta = 0
while paisa < paisb:
    paisa += (paisa*3/100)
    paisb += (paisb*1.5/100)
    conta += 1
print(f'O número de anos necessários foram {conta} anos')

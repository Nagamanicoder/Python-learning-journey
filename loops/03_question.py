# Multiplication table printer

n = int(input('enter the number to print its table: '))

for i in range(1, 11):
    if i==5: continue
    print('{} * {} = {}'.format(n, i, n*i))
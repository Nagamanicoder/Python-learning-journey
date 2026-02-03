# check the if number is prime or not
# the prime numbers have only two factors
# a factor that divides a number evenly , leaving no remainder

n = 5
is_prime = True
for i in range(2,n):
    if(n%i == 0):
        is_prime = False
        break

if is_prime:
    print('{} is Prime number'.format(n))
else:
    print('no!')
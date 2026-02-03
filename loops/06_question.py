# calculate a factorial number using while loop

n = 5
temp = n
fact = 1
while(temp!=1):
    fact *= temp
    temp -= 1
print("factorial of {} is: {}".format(n,fact))
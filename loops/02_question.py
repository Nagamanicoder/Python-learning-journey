# calculate the sum of even numbers upto n

sum_of_even_numbers = 0
n = int(input('enter the n value: '))

for i in range(1,n+1):
    if i%2 == 0:
        sum_of_even_numbers += i 
print("the sum of even numbers is: ", sum_of_even_numbers)
# reverse a string using a loop

name = 'venkatesh'
reversed_string = ''
len_string = len(name)
for i in range(1,len_string+1):
    reversed_string += name[len_string-i]
print(reversed_string)

for char in name:
    reversed_string = char + reversed_string
print(reversed_string)
# given a string, find the first non repeated character

name = 'nagamani'

for char in name:
    if name.count(char) == 1:
        print(char)
        break
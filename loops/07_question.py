# keep asking the user input until they enter a number between 1 and 10

while True:
    n = int(input('enter a number: '))
    if 1<= n >= 10:
        print('yeah!')
    else:
        print('invalid number, try again!')
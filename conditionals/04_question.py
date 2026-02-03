color = input('enter the color of the fruit: ')
fruit = input('enter the fruit name: ')

# unripe - green, ripe - yellow, overripe - brown

if fruit == 'banana':
    if color == 'green':
        print('Unripe') 
    elif color == 'yellow':
        print('ripe')
    else: 
        print('overripe')
else:
    print('I have no information about other fruits!')



weather = input('Provide the weather info: ')

weathers = {'sunny', 'rainy', 'snowy'}

if weather.lower() not in weathers:
    print('Invalid input')
    exit()

if weather.lower() in weathers:
    print('Go for a walk')
elif weather.lower() in weathers:
    print('Read a book')
elif weather.lower() in weathers:
    print('Build a snowman')

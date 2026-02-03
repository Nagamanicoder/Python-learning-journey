# Choose a mode of transportation based on the distance 
# < 3km - walk, 3-15km - bike, > 15km - car

distance = int(input('Say what distancee are you travelling today: ').lower().replace('km', ''))

if(distance <= 0):
    print('Inavlid distance')
    exit()

if(distance > 15):
    print('Drive a Car!')
elif(distance > 3):
    print('Take a Bike!')
elif(distance < 3):
    print('Go by walk!')
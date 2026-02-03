# Customize a coffee order: 'Small', 'medium', 'large with an option for extra shot or espresso

coffee_size = input('enter the coffee size you want: ').lower()
extra_shot = True

if extra_shot:
    coffee = coffee_size + " coffee with an extra shot"
else:
    coffee = coffee_size + " coffee"

print('Your ordered ', coffee)



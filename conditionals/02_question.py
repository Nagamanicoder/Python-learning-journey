# Movie tickets are priced based on age:
#  $12 for adults(18 and over)
# $8 for childern
# Everone gets a $2 discount on wednesday

age = int(input("Enter your age: "))
day = input("Enter the day of the week: ")
# price = 0
# if age >= 18:
#     price += 12
# else: 
#     price += 8

price = 12 if age >= 18 else 8


if day == 'Wednesday':
    price -= 2

print("Ticket price for you is $",price)  
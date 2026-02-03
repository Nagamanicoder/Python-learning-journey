# leap calendar
# the year is called leap year if it has 366 days
# the 366 days are calculated if the year is divisible by 4, followed by 100, followed by 400 then it is a leap year
# if not it is not leap year

year = int(input('enter the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year!')
else:
    print('not a leap year!')
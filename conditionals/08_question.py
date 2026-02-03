# Password strrength checker
# 'weak' - < 6 chars
# 'medium' - 6-10 chars
# 'strong' - > 10 chars

password = input('enter your password to check the strength: ')

password_len = len(password)

if password_len < 6:
    print('Weak - change your password!')
elif password_len <=10:
    print('medium - enhance your password!')
else:
    print('Your password is strong!')


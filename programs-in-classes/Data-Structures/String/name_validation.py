# Input the full name from user and valid it - check if it contains only alpha and space.

full_name = input('Enter your full name: ')

for char in full_name:
    is_valid = True
    if not char.isalpha() and char != " ":
        is_valid = False
        break

if is_valid:
    print('Your name is Validated.')

else:
    print("Re-enter your name.")
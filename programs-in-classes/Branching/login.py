userId = '#99107'
password = 'Pass@123'


userId_from_user = input('Enter your User Id: ')
password_from_user = input('Enter your Password: ')

if (userId == userId_from_user and password == password_from_user):
    print("Valid credentials. You're Logged In.")

else:
    print('Invalid Credentials. Either userId or password.')
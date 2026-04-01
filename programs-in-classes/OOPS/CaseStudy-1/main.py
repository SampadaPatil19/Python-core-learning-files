from manager import Manager

def main():
    ch = 0

    while(ch != '2'):
        print('--------------BANK MANAGEMENT SYSTEM---------------')
        print("""'Please Select one of the option from below: '
              1. Login
              2. Exit
              """)
        ch = input('Enter the choice: ')
        if ch == '1':
            user_name = input('Enter username: ')
            password = input('Enter Password: ')

            if (user_name == 'Admin' and password == '1234'):
                print('''
                      Login Successful...
                      ''')
                manager_emp = Manager()

            else:
                print('Invalid Credentials..')

        elif ch == '2':
            print('THANK YOU!')

        else:
            print('INVALID INPUT.')

main()
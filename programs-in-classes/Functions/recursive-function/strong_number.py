def factorial(num):
    if( num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)

def strongNum(num):
    if(num <= 0):
        return 0
    else:
        last_digit = num % 10
        fact = factorial(last_digit)
        return fact + strongNum(num // 10)

def checkIfStrongNumber(num):
    if num == strongNum(num):
        print(f'{num} is a strong number.')
    else:
        print(f'{num} is not a strong number.')

num = int(input('Enter the number: '))
checkIfStrongNumber(num)
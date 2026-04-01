# we will return for single value, not for multiple values
def digSep(num):
    if (num <= 0):
        pass
    else:
        last_digit = num % 10 # extracting last digit
        print(last_digit)
        num = num // 10 # removing last digit
        digSep(num)

num = int(input('Enter the number: '))
digSep(num)
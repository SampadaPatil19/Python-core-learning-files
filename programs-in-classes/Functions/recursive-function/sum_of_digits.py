# we will return for single value, not for multiple values
def digSep(num):
    if (num == 0):
        return 0
    else:
        last_digit = num % 10 # extracting last digit
        return last_digit + digSep(num//10)

num = int(input('Enter the number: '))
total = digSep(num)
print(total)
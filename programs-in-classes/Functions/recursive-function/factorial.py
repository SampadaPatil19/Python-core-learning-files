def factorial(n):
    if (n < 0):
        return 'negative number'
    
    elif (n == 0 or n == 1):
        return 1
    
    else:
        return n * factorial(n-1)

n = int(input('Enter the number for factorial: '))
print(factorial(n))


"""
Homework
WAP to separate out the digits from given  number
"""
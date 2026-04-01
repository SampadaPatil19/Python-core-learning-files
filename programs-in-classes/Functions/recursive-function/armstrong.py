def armstrong(n, power):
    if (n == 0):
        return 0
    else:
        last_digit = n % 10
        return last_digit**power + armstrong(n // 10, power)

def checkIfArmStrongNum(n, power):
    if n == armstrong(n, power):
        return f'{n} is ArmStrong Number.'
    else:
        return f'{n} is not an ArmStrong Number'

n = int(input('Enter the number: '))
power = int(input('Enter total number of digits in given number: '))
print(checkIfArmStrongNum(n, power))
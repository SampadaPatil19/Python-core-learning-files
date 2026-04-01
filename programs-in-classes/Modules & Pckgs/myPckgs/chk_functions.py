def chk_even(num):
    if num % 2 == 0:
        return True
    
    else:
        return False

# print(chk_even(40))

def chk_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False
    
# print(chk_odd(33))


def chk_positive(num):
    if num > 0:
        return True
    else:
        return False
    
def chk_prime(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                return False
        return True
    else:
        return False

print(chk_prime(29))


def sum_of_series(n):
    if (n <= 0):
        return 0
    else:
        return n + sum_of_series(n-1)
    
n = int(input('Enter the number of terms in series: '))
print(sum_of_series(n))

"""
Homewrok:
n = -5
-5 + -4 + -3 + -2 + -1
"""
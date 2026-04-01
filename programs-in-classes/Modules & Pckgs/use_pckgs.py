# ṃethod 1
from myPckgs import chk_functions
res = chk_functions.chk_even(24)
print("Is 24 even?", res)


# method 2 
from myPckgs.chk_functions import chk_odd
res1 = chk_odd(13)
print("Is 13 odd?", res1)


# method 3 
from myPckgs.chk_functions import *
res2 = chk_positive(-19)
print("Is -19 positive?", res2)


# method 4
from myPckgs.chk_functions import chk_prime as cp
res3 = cp(2)
res4 = cp(4)
print("Is 2 prime number?", res3)
print("Is 4 prime number?", res4)
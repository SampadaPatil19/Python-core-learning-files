# method 1
import functions

res = functions.addition(50, 60)
print("Addition:", res)


# method 2
from functions import subtraction

res1 = subtraction(100, 40)
print("Subtraction: ", res1)


#  method 3
from functions import *

res2 = multiplication(5, 6)
print("Multiplication: ", res2)


# method 4
from functions import division as div

res3 = div(80, 4)
print("Division using alias: ", res3)


# method 5
import functions as func

res4 = func.subtraction(30, 10)
print("Subtraction using alias: ", res4)


# method 6
from functions import addition as add, multiplication as mul
res5 = add(20, 30)
res6 = mul(4, 5)    
print("Addition using alias: ", res5)
print("Multiplication using alias: ", res6)
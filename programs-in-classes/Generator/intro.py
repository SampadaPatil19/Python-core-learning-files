# GENERATOR
"""
1. Generate values from function
2. Used to save memory
3. Will use yeild keyword instead of return
4. It maintain the state of function
5. Doesn't return all values at once
"""

"""
A generator in Python is a special type of function that returns an iterator 
and produces values one at a time using the yield keyword, 
instead of returning all values at once.

Unlike normal functions, generators pause their execution when yield is encountered 
and resume from the same state when the next value is requested.
"""

def intGenerator(n):
    for i in range(1, n+1):
        yield i

res = intGenerator(10)
print(next(res))

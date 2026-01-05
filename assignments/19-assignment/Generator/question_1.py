"""1.  We want to generate Fibonacci numbers up to a certain limit. 
Instead of computing and storing the entire sequence in memory, 
create generator to yield Fibonacci numbers one by one, 
conserving memory and allowing for easy iteration."""

def fibonaaci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a+b

# using next() function
fib_gen = fibonaaci_generator(20)
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))
print(next(fib_gen))

# using for loop on next() function
fib_gen2 = fibonaaci_generator(50)
for _ in range(10):
    print(next(fib_gen2))


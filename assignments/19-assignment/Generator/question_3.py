"""3.  Write a generator function that mimics the behavior of the built-in 
range() function. The generator should take start, stop, and step 
arguments and yield numbers within the specified range."""

def custom_range(start, stop, step=1):
    if step == 0:
        raise ValueError("step must not be zero")
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

for i in custom_range(2, 10, 2):
    print(i)

for i in custom_range(10, 2, -2):
    print(i)

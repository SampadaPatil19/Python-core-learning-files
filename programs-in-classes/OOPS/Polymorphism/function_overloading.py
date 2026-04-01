# Function Overloading: same name, different behavior
# During compile time - it'll decide which func will call
# Python is interpreted lang. so function overloading doesn't work.
# Recent function will overwrite previous function


def sum(num1, num2):
    return num1 + num2


def sum(x, y, z):
    return x+y+z

# print(sum(2, 3))


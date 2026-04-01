def addition(x, y):
    return x + y

def subtraction(x, y):
    return x  - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print(__name__)
# for this file it will print __main__
# for another file it will return file_name when we import this file as module


if __name__ == "__main__":
    result = addition(10, 20)
    print("Addition from functions module:", result)

# __name__ == "__main__" is used to check if module is being run directly or being imported
# if run directly, the code block will execute otherwise it will not execute
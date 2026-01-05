def memorization(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            print("Fetching from cache.")
            return cache[n]
        output = func(n)
        cache[n] = output
        print("Calculating new result.")
        return output
    return wrapper

@memorization
def fact(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

res = fact(5)
print(res)

print("--------------")

res = fact(5)
print(res)
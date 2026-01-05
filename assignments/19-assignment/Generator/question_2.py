"""2.  Implement a generator function that yields palindrome numbers. 
Palindromes are numbers that read the same backward as forward 
(e.g., 121, 1331). Generate palindromes lazily and infinitely."""

"""n = 121
print(str(n)[::-1])
if str(n) == str(n)[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")"""

""" 
n = 0
while True:
        temp = n
        rev = 0
        while temp > 0:
            last_digit = temp % 10
            rev = rev * 10 + last_digit
            temp = temp // 10
"""

def palindrome_generator():
    n = 0
    while True:
        temp = n
        rev = 0
        while temp > 0:
                last_digit = temp % 10
                rev = rev * 10 + last_digit
                temp = temp // 10
        
        if n == rev:
                yield n
        n += 1
    

# Example usage:
gen = palindrome_generator()    
for _ in range(100):
    print(next(gen))



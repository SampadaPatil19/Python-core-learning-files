# Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit. 

divisible_numbers = [num for num in range(1, 1001) if any(num % digit == 0 for digit in range(1, 10))]

print(divisible_numbers)
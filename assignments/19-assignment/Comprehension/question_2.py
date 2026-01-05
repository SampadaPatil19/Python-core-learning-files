# 2. Find all of the numbers from 1–1000 that have a 6 in them.

numbers_with_six = [num for num in range(1, 1001) if '6' in str(num)]

print(numbers_with_six)
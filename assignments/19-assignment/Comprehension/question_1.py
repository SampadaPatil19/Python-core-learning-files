# 1.  Find all of the numbers from 1–1000 that are divisible by 8.

divisible_by_eight = [num for num in range(1, 1001) if num % 8 == 0]
print(divisible_by_eight)
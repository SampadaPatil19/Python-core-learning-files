try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum_result = num1 + num2

except Exception as e:
    print(f"An error occurred: {e}")

# If no exception occurs, this block will execute
# else block is optional
else:
    print(f"The sum of {num1} and {num2} is {sum_result}")

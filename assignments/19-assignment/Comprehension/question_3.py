# 3.  Count the number of spaces in a string (take input from user).

user_input = input("Enter a string:\n")

space_count = len([char for char in user_input if char == ' '])

print(f"Number of spaces in the given string: {space_count}")
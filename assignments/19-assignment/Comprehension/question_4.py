# 4.  Remove all of the vowels in a string (take input from user).
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    no_vowel_string = ''.join([char for char in string if char not in vowels])

    return no_vowel_string

user_input = input("Enter a string: ")
result = remove_vowels(user_input)
print("String without vowels: ", result)
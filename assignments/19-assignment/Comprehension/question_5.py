# 5. Find all of the words in a string that are less than 5 letters (take input from user).

def find_short_words(string):
    words = string.split()
    print(words)
    short_words = [word for word in words if len(word) < 5]
    return short_words

user_input = input("Enter a string:\n")
result = find_short_words(user_input)
print("Words with less than 5 letters: ", result)
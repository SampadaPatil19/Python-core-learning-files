# 6.  Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

def word_length_dict(string):
    words = string.split()
    length =  {word: len(word) for word in words}
    # length_without_special_chars = {}
    # for word, l in length.items():
    #     cleaned_word = ''.join(char for char in word if char.isalnum())
    #     length_without_special_chars[cleaned_word] = l
    
    return length

user_input = input("enter a Sentence:\n")
result = word_length_dict(user_input)
print("Length of each word in the sentence: ", result)
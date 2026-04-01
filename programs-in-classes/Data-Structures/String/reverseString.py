def revString(str):
    rev_str = ''
    for char in str:
        rev_str = char + rev_str
    
    return rev_str

str = 'Firstbit Solutions'
str = revString(str)
print(str)


# Homework - Try using indexing

def reverseStr(str1):
    reverse_str = ''

    for i in range(len(str1)-1, -1, -1):
        reverse_str += str1[i]
    
    return reverse_str

str1 = 'Firstbit Solutions'
str1 = reverseStr(str1)
print(str1)

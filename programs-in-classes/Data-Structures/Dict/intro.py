# Structure : {} => {key : value} pair
dict = {1: 'Python', 2:'Java', 3: 'C', 'a': 345}

"""Type of Data: Heterogeneous
- key and value both can have heterogeneous data
"""
print(dict)


# Sequence: Ordered - original sequence of data doesn't change after printing the data
print(dict)


"""Changable: 
- Key is Immutable
- Value is Mutable
"""

dict['a'] = 999
print(dict)

dict['b'] = 1000
print(dict)


dict2 = {(1, 2, 3): 'First Value', [10, 20, 30]: 'Second Value'}
print(dict2)
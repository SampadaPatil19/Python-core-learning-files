# Tuple

# 1. Structure: ()
tu = (10,)
print(type(tu))


# 2. Type of data: Heterogeneous
tu = (10, 30, 'abs')


# 3. Sequence of Data: Ordered Data
print(tu) #it will print the same data


# 4. Changable: Immutable
# tu.count()
# tu.index()

# only two methods. can't add elements or remove them


# 5. Speed: Faster than List
# Why
# Tuple is allocated with less memory blocks than list in memory
import sys

tup = ()
print(sys.getsizeof(tup))

li = []
print(sys.getsizeof(li))


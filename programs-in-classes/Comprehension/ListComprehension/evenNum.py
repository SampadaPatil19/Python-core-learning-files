li = [i for i in range(1, 11) if i % 2 == 0]
print(li)

li = []
for i  in range(1, 11):
    if i % 2 == 0:
        li = li + [i]

print(li)


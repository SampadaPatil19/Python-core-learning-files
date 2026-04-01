import time

print("This is first line.")
time.sleep(2)
print("This is second line after 2 seconds delay.")


# for i in range(1, 11):
#     print(i)
#     time.sleep(1)

res = time.localtime()
print(res.tm_mday)
print(res.tm_yday)
print(res.tm_wday) 
# tm_wday - day of the week (0=Monday, 6=Sunday)

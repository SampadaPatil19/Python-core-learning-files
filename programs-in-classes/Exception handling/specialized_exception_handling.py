try:
    li = [10, 20, 30, 40]
    ind = int(input("enter index: "))
    print(f'Value at index {ind} is {li[ind]}')


# Generalized exceptiion handling
except ValueError as e:
    # print("Error: Invalid input. Please enter an integer value for the index.")
    print(f'Error: {e}')

except IndexError as e:
    # print('Error: Index out of range.')
    print(f'Error: {e}')

except TypeError as e:
    # print('Error: Type mismatch encountered.')
    print(f'Error: {e}')

except AttributeError as e:
    # print('Error: Attribute not found.')
    print(f'Error: {e}')

except MemoryError as e:
    # print('error: Memory limit exceeded.')
    print(f'Error: {e}')

# genralized exception handling
except:
    print('An unexpected error occurred.')
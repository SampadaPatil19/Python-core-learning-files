def divide(dividend, divisor):
    try:
        result = dividend / divisor
    
    except Exception as e:
        return f"Error: {e}" 
    
    else:
        return f"result is {result}"
    
    finally:
        return "Execution completed."   

res = divide(10, 0)
print(res)

# Output will be "Execution completed." - finally block's return statement overrides others
# Exception block should have been excutes but its return is overridden so it is not visible even though it runs/executes

# Finally block always executes regardless of whether an exception occured or not.
# If there is a return statement in finally block, it overrides any previous return statements in try or except blocks.
from user_defined_exception import UserException
age = -1

if age <= 0 or age > 120:
    try:
        raise UserException(age)
    
    except Exception as e:
        print(e)

# this will raise an exception bcoz condition is always false
# while using "raise" we give the condition opposite to what we want to check. and if that condition is true, exception is raised.
# here we want to check if the age is valid, so we give the condition for invalid age. if that condition is true, exception is raised.
# the exception should be derived from Base Exception class, but here we are raising a string, so it will give a typeError.

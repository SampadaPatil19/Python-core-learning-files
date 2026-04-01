class UserException(Exception):
    def __init__(self, age):
        self.age = age
    
    def __str__(self):
        return f"{self.age} is an invalid age."

if __name__ == "__main__":
    use = UserException(-8)
    print(use)
    
# 1 base class and 1 derived class

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def getData(self):
        print('Name: ', self.name)
        print('AGE: ', self.age)
        print('EMAIL: ', self.email)

class Employee(Person):
    def __init__(self, name, age, email, emp_id, salary):
        super().__init__(name, age, email)
        self.emp_id = emp_id
        self.salary = salary
    
    def getData(self):
        super().getData()
        print('EMPLOYEE ID: ',self.emp_id)
        print('EMPLOYEE SALARY: ', self.salary)

emp = Employee('Gunjan', 21, 'patil@gmaail.com', 101, 300000)
emp.getData()

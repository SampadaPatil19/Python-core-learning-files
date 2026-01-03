"""
1. Create a class Student with following  
    a. data members :   
        i. StudentId 
        ii. Name 
        iii. Age 
        iv. Percentage 
    b. Add the following methods : 
        i. Parameterized constructor 
        ii. Display 
        iii. Accept 
        iv. Method CalculateRank 
        v. Override __str__ Method
"""

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def display(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}")

    def accept(self):
        print("Accepting student details...")

    def calculateRank(self, percentage):
        if self.percentage >= 90:
            rank = 'A'
        elif self.percentage >= 80:
            rank = 'B'
        elif self.percentage >= 75:
            rank = 'C'
        elif self.percentage >= 60:
            rank = 'D'
        else:
            rank = 'F'
        
        return f"Rank: {rank}"

obj1 = Student(1, "Gunjan Patil", 23, 90.23)
res = obj1.calculateRank(obj1.percentage)
# print(res)
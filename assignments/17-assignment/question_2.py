"""
2. Create a derived class from Student as EnggStudent with : 
    a. Data   members as :  
        i. Branch 
        ii. InternalMarks 
    b. Add the following methods : 
        i. Parameterized constructor 
        ii. Display 
        iii. Accept 
        iv. override Method CalculateRank 
        v. Override __str__ Method 
"""

from question_1 import Student

class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage):
        super().__init__(student_id, name, age, percentage)

    def display(self):
        return super().display()

    def accept(self):
        return super().accept()

    def calculateRank(self):
        return super().calculateRank()

    def __str__(self):
        return super().__str__()
    
obj = EnggStudent(1, "Gunjan Patil", 23, 74.24)
obj.display()
obj.calculateRank()
obj.accept()
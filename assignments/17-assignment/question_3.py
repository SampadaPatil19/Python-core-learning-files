"""3. Create a class MedicalStudent inherited from Student with following 
: 
i. Data members :Specialization 
ii. MarksOfInternship 
 
b. Add the following methods : 
i. Parameterized constructor 
ii. Display 
iii. Accept 
iv. override Method CalculateRank 
v. Override __str__ Method"""

from question_1 import Student

class medicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship
        super().__init__(student_id, name, age, percentage)

    def display(self):
        return super().display()
    
    def accept(self):
        return super().accept()
    
    def calculateRank(self, percentage):
        return super().calculateRank(self.percentage)

stud = medicalStudent(2, "Aarav Sharma", 24, 88.5, 'Computer Science', 95)
print(stud.calculateRank(stud.percentage))
print(stud.display())
print(stud.accept())
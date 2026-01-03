"""4. Create a class College which has collection of students. Add the 
following methods : 
a. Parameteried constructor for number of students. 
b. AddStudent 
c. GetStudent 
d. RemoveStudent 
e. Override __str__ Method """

class College:
    def __init__(self, number_of_students, student_id):
        self.number_of_students = number_of_students
        self.student_id = student_id

    def addStudent(self, student_id):
        print(f"Adding Student: {self.student_id}")

    def getStudent(self, student_id):
        print(f"Getting Student with ID: {self.student_id}")

    def removeStudent(self, student_id):
        print(f"Removing Studetn with ID: {self.student_id}")

    def __str__(self):
        print("College with number of Students: ", self.number_of_students)

col = College(5, 101)
col.addStudent("Gunjan Patil")
col.getStudent(101)
col.removeStudent(101)
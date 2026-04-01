# Static method
"""
1. Class Level Method
2. We don't give self as para
3. Use class name to invoke static method
"""

class Student:
    count = 0
    def __init__(self, name, roll, course):
        Student.count += 1
        self.name = name
        self.roll = roll
        self.course = course

    def getData(self):
        return f'NAME: {self.name}\nROLL_NUM: {self.roll}\nCOURSE: {self.course}'
    
    @staticmethod
    def totalStudent():
        return Student.count

s1 = Student('Sampada', 101, 'Python')
s2 = Student('Gunjan', 102, 'Java')

print('Total Student: ', Student.totalStudent())
print(s1.totalStudent())
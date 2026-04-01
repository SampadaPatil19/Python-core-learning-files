
class Employee:
    def setData(self, id, name, salary, dept):
        self.eid = id
        self.ename = name
        self.salary = salary
        self.dept = dept

    def getData(self):
        print('ID: ', self.eid)
        print('NAME: ', self.ename)
        print('SALARY: ', self.salary)
        print('DEPARTMENT: ', self.dept)

obj1 = Employee()
obj1.setData(101, 'Gunjan', '70000', 'Devlopment')
obj1.getData()


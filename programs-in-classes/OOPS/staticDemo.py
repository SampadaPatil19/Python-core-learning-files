# Static Variables
"""
1. class level variales.
2. only one copy will be created & distributed to all object.

3. Use class name to access thte static variable
"""

# Non-Static Variables
"""
1. Object Level Variables.
2. copies = no. of object created.
3. Use object to access the bject variables
"""

class Account:
    branch = 'SBI'
    def __init__(self, holder_name, account_no, balance):
        self.holder_name = holder_name
        self.account_no = account_no
        self.balance = balance

    def getData(self):
        data = 'BRANCH: ' + Account.branch
        data += '\nACOUNT_HOLDER: ' + self.holder_name
        data += '\nACCOUNT_NUMBER: ' + str(self.account_no)
        data += '\nBALANCE: ' + str(self.balance)
        return data


ac = Account('Gunjan', 123456,1200000)

print(Account.branch)
print(ac.branch) #

print('***************************')
print(ac.getData())

print('--------------------------')

acc = Account('Sampada', 2424899, 1300000)
print(acc.getData())
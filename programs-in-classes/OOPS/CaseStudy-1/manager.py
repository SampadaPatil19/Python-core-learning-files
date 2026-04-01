from saving_account import SavingAccount
from datastore import Datastore

class Manager:
    def __init__(self):
        ch = 0
        self.ds = Datastore()

        while ch != '6':
            print("""
                  -----------MANAGER------------
                    Please Select one Option:
                  1. Create Account
                  2. Check Balance
                  3. Withdrawal
                  4. Deposit
                  5. End Day Report
                  6. Exit                
                """)
            
            ch = input('Which Operation You Want TO Do?\n')
            
            if ch == '1':
                self.createAccount()

            elif ch == '2':
                self.checkBalance()

            elif ch == '3':
                self.withDrawal()

            elif ch == '4':
                self.deposit()
            
            elif ch == '5':
                self.endReport()

            else:
                print('Invalid Input')
            
        def createAccount(self):
            name = input('Enter Holder Name: ')
            acc_no = int(input('Enter the Account Number: '))
            bal = int(input('Enter balance: '))
            status = input('What is the Status?(Active/Inactive): ')
            sav_obj = SavingAccount(name, acc_no, bal, status)
            self.ds.addData(sav_obj)
            print('Data added successfully..')

        def checkBalance(self):
            acc_no = int(input('Enter account number: '))
            acc = self.ds.getData(acc_no)
            print('Balance: ', acc.balance)

        def withDrawal(self):
            pass

        def deposit(self):
            pass

        def endReport(self):
            pass
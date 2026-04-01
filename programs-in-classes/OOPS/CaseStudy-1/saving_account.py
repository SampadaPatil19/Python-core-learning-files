from account import Account

class SavingAccount(Account):
    min_bal = 1000
    def __init__(self, holder_name, acc_no, balance, status):
        super().__init__(holder_name, acc_no, balance, status)
        self.min_bal = SavingAccount.min_bal
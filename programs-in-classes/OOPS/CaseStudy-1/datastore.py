class Datastore:
    def __init__(self):
        self.account_data = {}
        self.report = {}

    def addData(self, account):
        self.account_data[account.acc_no] = account

    def getData(self, acc_no):
        return self.account_data[acc_no]
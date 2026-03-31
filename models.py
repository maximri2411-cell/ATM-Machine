#!Pay attention its only for class Account & Bank

class Accounts:
    
    def __init__(self, account_id, name, PIN, Balance, Status, History):
        self.account_id = account_id
        self.name = name
        self.PIN = PIN
        self.Balance = Balance
        self.Status = Status
        self.History = History
        
        
    def get_info(self):
        print(self.account_id, self.name, self.PIN, self.Balance, self.Status,  self.History)
        

account1 = Accounts(321321, "Grisha", 1234, 50000, "Status", "History")
account2 = Accounts(653421, "Daniel", 4332, 20000, "Status", "History")
account3 = Accounts(132456, "Moshe", 4343, 15000, "Status", "History")
account4 = Accounts(314265, "Michal", 2323, 37000, "Status", "History")
account5 = Accounts(556612, "Dana", 1123, 43000, "Status", "History")
account6 = Accounts(615243, "Shahar", 2121, 29000, "Status", "History")

account1.get_info()
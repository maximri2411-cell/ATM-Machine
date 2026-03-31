#!Pay attention its only for class Account & Bank

class Accounts:
    
    def __init__(self, account_id, name, PIN, Balance, Status, History):
        self.account_id = id
        self.name = name
        self.PIN = PIN
        self.Balance = Balance
        self.Status = Status
        self.History = History
        
        
    def get_info(self):
        return(self.account_id, self.name, self.PIN, self.Balance, self.Status,  self.History)
        

account1 = Accounts(12345, "grisha", 1234, 50000, "Status", "History")

account1.get_info
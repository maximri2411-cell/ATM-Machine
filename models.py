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
        

account1 = Accounts(12345, "Grisha", 1234, 50000, "Activate", "History")

account1.get_info()







#=============== MAXIM ===============
#! Creatin a class of the BAnk' Part 3:

class Bank:
    
    def __init__(self):
        pass
    
    
#Function to create account
    def create_account(self, ):
    
#Function to find an account
    def find_account(self, ):
        
#Function to log a user into the bank
    def login_account(self, ):
        
#Function of the manager
    def manager_login(self, ):
    
#Function for transfer money between accounts
    def transfer(self, ):
        
#Function of list all the accounts we created
    def list_accounts(self, ):
        
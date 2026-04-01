#!Pay attention its only for class Account & Bank

class Accounts:
  
    def __init__(self, account_id, name, PIN, Balance, is_active , History):
        self.account_id = account_id
        self.name = name
        self.PIN = PIN
        self.Balance = Balance
        self.is_active = is_active
        self.History = History
        
        
    def get_info(self):
        print(f"ID:{self.account_id}, Dear {self.name}") 
        if self.is_active == True:
            print("Your account is Active")
        else:
            print("Your account is blocked")
        if self.is_active == True:
            print(f"Your PIN:{self.PIN} Your Balance:{self.Balance} NIS \n{self.History}")
        else:
            print("Can't continue the process, plaese call customer service")



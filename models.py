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


account1 = Accounts(321321, "Grisha", 1234, 50000, True, [])
# account2 = Accounts(653421, "Daniel", 4332, 20000, "True", [])
account3 = Accounts(132456, "Moshe", 4343, 15000, "False", [])
# account4 = Accounts(314265, "Michal", 2323, 37000, "False", [])
# account5 = Accounts(556612, "Dana", 1123, 43000, "True", [])
# account6 = Accounts(615243, "Shahar", 2121, 29000, "False", [])

all_accounts = [account1, account3]

account1.get_info()
# account2.get_info()
account3.get_info()
# account4.get_info()
# account5.get_info()
# account6.get_info()
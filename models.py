# #!Pay attention its only for class Account & Bank

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
        


# account1 = Accounts(12345, "Grisha", 1234, 50000, "Activate", "History")
# =======
# account1 = Accounts(321321, "Grisha", 1234, 50000, "Status", "History")
# account2 = Accounts(653421, "Daniel", 4332, 20000, "Status", "History")
# account3 = Accounts(132456, "Moshe", 4343, 15000, "Status", "History")
# account4 = Accounts(314265, "Michal", 2323, 37000, "Status", "History")
# account5 = Accounts(556612, "Dana", 1123, 43000, "Status", "History")
# account6 = Accounts(615243, "Shahar", 2121, 29000, "Status", "History")

# account1.get_info()




#=======================
# Part 3: Bank manager 
#=======================
import random 


#Creating a class of the Bank Part 3: it will manager all the accounts in the bank
class Bank: 
    
    def __init__(self):
        self.Manager_pin = "admin123456123456" #managers password
        self.Accounts = {} #some kind of dictionary to save all of the accounts
    
    
    #Function to create new account 
    def create_account(self, name, pin):
        account_ID = str(random.randint(100000, 999999)) #!Alex created users ID using 6 digits
    
        while account_ID in self.Accounts:
            account_ID = str(random.randint(100000, 999999))
        
        new_account = Accounts(account_ID, name, pin, 0.0, "Active", []) #creating a user exactly according to the characteristics we created in part 2
        
        self.Accounts[account_ID] = new_account #saving the new account in the dictionary of the bank
        
        print(f"Account has been created! Your ID is: {account_ID}") #input of the creation
        return account_ID

    # #Function to find an account
    # def find_account(self, ):
        
    # #  Function to log a user into the bank
    # def login_account(self, ):
        
    # #Function of the manager
    # def manager_login(self, ):
    
    # #Function for transfer money between accounts
    # def transfer(self, ):
        
    # #Function of list all the accounts we created
    # def list_accounts(self, )ֿ:
    
    
    
    
    
    
    
    
    
# #!Check to see if the create account works
# my_bank = Bank()

# print("--- Testing Account Creation ---")
# new_id = my_bank.create_account("Yossi Levi", "1234")

# if new_id in my_bank.Accounts:
#     print(f"Success! Account {new_id} exists in the bank.")
    
#     user_account = my_bank.Accounts[new_id]
#     print(f"Owner Name: {user_account.name}")
#     print(f"Current Balance: {user_account.Balance}")
# else:
#     print("Failure: Account was not saved in the dictionary.")
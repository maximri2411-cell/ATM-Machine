import random 
from datetime import datetime


#============= Accounts ============
class Accounts: # Creating a class of Accounts
    def __init__(self, account_id, full_name, pin, balance, status , history):
        self.account_id = str(account_id) #! In dict, everthing in a string 
        self.full_name = full_name
        self.pin = str(pin) #! the reason we save as str is so if an account wil have an 0075 pin for example, it will save exactly as it isin int it will be 75 
        self.balance = float(balance) #! Line alignment that the money in the accounts will be a float
        self.status = status
        self.history = history
        
    def j_dict(self): # Creating a simple function-dictionary for json to understand
        return {
            "account_id": self.account_id,
            "full_name": self.full_name,
            "pin": self.pin,
            "balance": self.balance,
            "status": self.status,
            "history": self.history 
        }
    
    
#=============== Bank ==============
class Bank: # Manage all accounts in our project
    
    def __init__(self):
        
        self.manager_full_name = "Super Mario"
        self.manager_pin = "admin123456123456" # Managers password
        self.Accounts = {} # Some kind of dictionary to save all of the accounts


    def create_account(self, full_name, pin): # Function to create new account 
        account_id = str(random.randint(100000, 999999))
    
        while account_id in self.Accounts:
            account_id = str(random.randint(100000, 999999))
        
        new_account = Accounts(account_id, full_name, pin, 0.0, "Active", []) # Creating a user exactly according to the characteristics we created in part 2
        
        self.Accounts[account_id] = new_account # saving the new account in the dictionary of the bank
        
        print(f"Account has been created. \nYour ID is: {account_id}") # output of the creation
        return account_id


    def find_account(self, account_id): # Function to find an account
        
        account_search = self.Accounts.get(str(account_id)) # The get() is to print None in case the ID hasent been found
        
        if account_search:
            print(f"Account ID is found: {account_search.full_name}")
            return account_search
        else:
            print("Error: Account ID not found.")
            return None
        
        
    def login_account(self, account_id, pin): # Function to log a user into the bank
        account = self.find_account(account_id) # Uses the function we created in previos function
        
        # Alex have made a few off those accounts active and blocked
        # We are goin to check if it is blocked, he cannot continue in the proccess
        if account.status == "Blocked":
            print(f"Error: Account {account_id} is BLOCKED. \nPlease call customer service or visit your local bank. \nThank you for understanding.")
            return None
            
        if account:
            if str(account.pin) == str(pin):
                print((f"Login successful. \nWelcome {account.full_name}."))
                return account
            else:
                print(f"Error: Incorerect PIN. \nPlease try again. \nIn case you forgot the PIN, Please call customer service or visit your local bank. \nThank you for understanding.")
                return None
        return None 
        
        
    def manager_login(self, password): # Function of the manager
        if password == self.manager_pin:
            print(f"Manager access passed successfully. \nWelcome {self.manager_full_name}") # We determined in the beginning inside the "Father" 
            return True
        else:
            print(f"Access Denied: Invalid manager password. \nPlease try again. \nIn case you forgot the Password, Contact your local bank for help.")
    
    
    def transfer(self, sender, receiver, amount): # Function for transfer money between accounts
        the_sender = self.find_account(sender)
        the_receiver = self.find_account(receiver)
        
        if the_sender is None: # We want to check first if they even exist in order to countinue forward to sendng the money
            print(f"Error: The Sender account does not exist. \nPlease try again. \nIn case you forgot the ID, contact your local bank.")
            return False
        
        if the_receiver is None:
            print(f"Error: The Receiver account does not exist. \nPlease try again. \nMake sure you put the right ID. \nIn case you having a problem, Contact your local bank.")
            return False
        
        amount_transfer = float(amount) # Creating the value of the amount for the next part
        
        if amount_transfer <= 0: # In case the sender trys to put an 0 or low 
            print("Error: Amount must be positive.")
            return False
        
        if the_sender.balance < amount_transfer: # Now we are goin to check if the sender has enough amount to even send the money
            print(f"Transfer Failed: The {the_sender.full_name} is lack of NIS.")
            print(f"Current Balance in your account: {the_sender.balance} | Transfer request: {amount_transfer}")
            return False
                
            
        #! Make sure everwhere the balanc/amount is goin with 'float' like in real life situation
        # Finishing the proccess of the transfer
        the_sender.balance -= float(amount)
        the_receiver.balance += float(amount)
            
            
        # Creating a date value for the history of the tansfer
        date = datetime.date().strftime("%d/%m/%Y %H:%M")
            
        # Adding to the history the transfer with the date
        the_sender.history.append(f"{date}: Send: {amount_transfer} to {the_receiver.full_name}.")
        the_receiver.history.append(f"{date}: Received: {amount_transfer} from {the_sender.full_name}.")
                    
        print(f"The Transfer of: {amount} NIS has been completed. \nThank you.")
        return True
        
    
    def list_accounts(self): # Function of list all the accounts we created
        print("----- Bank Accounts List ------") # Nice title
        
        for account in self.Accounts.values():
            
            print(f"ID: {account.account_id} | Name: {account.full_name} | Balance: {account.balance}")
        
        print("-------------------------------")
        
        
        
        
         # def account_info(self): #
    #     print(f"ID: {self.account_id}, Dear {self.full_name},")
        
    #     if self.status == "Active" or self.status == True: # In case is True, it will print all the info about the account, if False, nothing
    #         print(f"Your account status: Active. \nPIN: {self.PIN}. \nAccount Balance: {self.balance} NIS \nHistory of the Account: {self.history}.") # For True
    #     else:
    #         print(f"Your account is BLOCKED. \nWe can not continue the process. \nPlease call customer service or visit your local bank. \nThank you for understanding.") # For False
            
    # def accounts_pool():
    #     account1 = Accounts(321321, "Grisha", 1234, 76241.31, True, [])
    #     account2 = Accounts(653421, "Daniel", 4332, 21356.60, True, [])
    #     account3 = Accounts(132456, "Moshe", 4343, 15010.90, False, [])
    #     account4 = Accounts(314265, "Michal", 2323, -4562.0, False, [])
    #     account5 = Accounts(556612, "Dana", 1123, 144222.30, True, [])
    #     account6 = Accounts(615243, "Shahar", 2121, 2341.7, False, [])  
  
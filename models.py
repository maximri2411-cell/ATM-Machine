import random 
import main
from datetime import datetime

class Accounts: # Creating a class of Accounts Part 2  
  
    def __init__(self, account_id, name, PIN, Balance, is_active , History):
        self.account_id = str(account_id) # In dict, everthing in a string 
        self.name = name
        self.PIN = PIN
        self.Balance = float(Balance) #! Line alignment that the money in the account will be a float
        self.is_active = is_active
        self.History = History
        
                
    def get_info(self):
        print(f"ID:{self.account_id}, Dear {self.name}")
             
        if self.is_active:
            print("Your account is Active")
            print(f"Your PIN:{self.PIN} Your Balance:{self.Balance} NIS \n{self.History}")
        else:
            print("Your account is blocked!!!")
            print("We can not continue the process. Plaese call customer service")


    def wit
#============= Maxim ============
class Bank: # Creating a class of the Bank Part 3: it will manager all the accounts in the bank
    
    def __init__(self):
        self.Manager_name = "King-Kong"
        self.Manager_pin = "admin123456123456" # Managers password
        self.Accounts = {} # Some kind of dictionary to save all of the accounts

    
# Creating a class of the Bank Part 3: it will manager all the accounts in the bank
class Bank: 
    
    def __init__(self):
        
        self.Manager_name = "King-Kong"
        self.Manager_pin = "admin123456123456" # Managers password
        self.Accounts = {} # Some kind of dictionary to save all of the accounts


    # Function to create new account 
    def create_account(self, name, pin):
        account_id = str(random.randint(100000, 999999)) #!Alex created users ID using 6 digits
    
        while account_id in self.Accounts:
            account_id = str(random.randint(100000, 999999))
        
        new_account = Accounts(account_id, name, pin, 0.0, "Active", []) # Creating a user exactly according to the characteristics we created in part 2
        
        self.Accounts[account_id] = new_account # saving the new account in the dictionary of the bank
        
        print(f"Account has been created. Your ID is: {account_id}") # input of the creation
        return account_id


    # Function to find an account
    def find_account(self, account_id):
        
        account_search = self.Accounts.get(str(account_id)) # The get() is to print None in case the ID hasent been found
        
        if account_search:
            print(f"User found: {account_search.name}")
            return account_search
        else:
            print("Error: Account ID was not found.")
            return None
        
        
    #  Function to log a user into the bank
    def login_account(self, account_id, pin):
        account = self.find_account(account_id) # Uses the function we created in previos function
        
        # Alex have made a few off those accounts active and blocked
        # We are goin to check if it is blocked, he cannot continue in the proccess
        if account.is_active == False or account.is_active == "False": 
            print(f"Error: Account {account_id} is BLOCKED. \nPlease contact your local bank for help.")
            
        
        if account:
            if int(account.PIN) == int(pin):
                print((f"Login successful. \nWelcome {account.name}."))
                return account
            else:
                print("Error: Incorerect PIN. \nPlease try again. \nIn case you forgot the PIN, Contact your local bank for help.")
                return None
            
        return None 
        
        
    #Function of the manager
    def manager_login(self, password):
        if password == self.Manager_pin:
            print(f"Manager access granted. \nWelcome {self.Manager_name}") # We determined in the beginning inside the "Father" 
            return True
        else:
            print("Access Denied: Invalid manager password. \nPlease try again. \nIn case you forgot the Password, Contact your local bank for help.")
    
    
    # #Function for transfer money between accounts
    def transfer(self, sender, receiver, amount):
        the_sender = self.find_account(sender)
        the_receiver = self.find_account(receiver)
        
        if the_sender is None: # We want to check first if they even exist in order to countinue forward to sendng the money
            print("Error: The Sender account does not exist. \nPlease try again. \nIn case you forgot the ID, contact your local bank.")
            return False
        
        if the_receiver is None:
            print("Error: The Receiver account does not exist. \nPlease try again. \nMake sure you put the right ID. \nIn case you having a problem, Contact your local bank.")
            return False
        
        amount_transfer = float(amount) # Creating the value of the amount for the next part
        
        if the_sender.Balance < amount_transfer: # Now we goon to check if the sender has enough amount to even send the money
            print(f"Transfer Failed: The {the_sender.name} is lack of NIS.")
            print(f"Current Balance in your account: {the_sender.Balance} | Transfer request: {amount_transfer}")
            return False
                
            
        #! Make sure everwhere the balanc/amount is goin with 'float' like in real life situation
        # Finishing the proccess of the transfer
        the_sender.Balance -= float(amount)
        the_receiver.Balance += float(amount)
            
            
        # Creating a date value for the history of the tansfer
        date = datetime.date().strftime("%d/%m/%Y %H:%M")
            
        # adding to the history the transfer with the date
        the_sender.History.append(f"{date}: Send: {amount_transfer} to {the_receiver.name}.")
        the_receiver.History.append(f"{date}: Received: {amount_transfer} from {the_sender.name}.")
                    
        print(f"The Transfer of: {amount} NIS has been completed. \nThank you.")
        return True
        
    
    #Function of list all the accounts we created
    def list_accounts(self):
        print("----- Bank Accounts List ------") # Nice title
        
        for account in self.Accounts.values():
            
            print(f"ID: {account.account_id} | Name: {account.name} | Balance: {account.Balance}")
        
        print("-------------------------------")
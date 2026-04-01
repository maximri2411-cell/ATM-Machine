import random 

# Creating a class of the Bank Part 3: it will manager all the accounts in the bank
class Bank: 
    
    def __init__(self):
        
        self.Manager_name = "King-Kong"
        self.Manager_pin = "admin123456123456" # Managers password
        self.Accounts = {} # Some kind of dictionary to save all of the accounts

class Accounts:
  
    def __init__(self, account_id, name, PIN, Balance, is_active , History):
        self.account_id = account_id
        self.name = name
        self.PIN = PIN
        self.Balance = Balance
        self.is_active = is_active
        self.History = History
    
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
        
        if account:
            if int(account.PIN) == int(pin):
                print((f"Login successful. \nWelcome {account.name}."))
                return account
            else:
                print("Error: Incorerect PIN. \nPlease try again. \nIn case you forgot the PIN, Conntact your local Bank.")
                return None
            
        return None 
        
        
    #Function of the manager
    def manager_login(self, password):
        if password == self.Manager_pin:
            print(f"Manager access granted. \nWelcome {self.Manager_name}") # We determined in the beginning inside the "Father" 
            return True
        else:
            print("Access Denied: Invalid manager password. \nPlease try again. \nIn case you forgot, Contact your management.")
    
    
    # #Function for transfer money between accounts
    # def transfer(self, ):
        
        
    #Function of list all the accounts we created
    def list_accounts(self):
        print("----- Bank Accounts List ------") # Nice title
        
        for account in self.Accounts.values():
            
            print(f"ID: {account.account_id} | Name: {account.name} | Balance: {account.Balance}")
        
        print("-------------------------------")
    
    
    
#!Check to see if the create account works
# 1. יצירת האובייקט של הבנק
my_bank = Bank()

print("New account")
# ניצור חשבון לגרישה. הפונקציה מחזירה לנו את ה-ID שנוצר
grisha_id = my_bank.create_account("Grisha", 1234)

print("\nsearching for account")
my_bank.find_account(grisha_id)

print("\nlogin")
# ננסה להיכנס עם פרטים נכונים
my_bank.login_account(grisha_id, 1234)

print("\nmanager")
# נשתמש בסיסמת המנהל שאלכס הגדיר
my_bank.manager_login("admin123456123456")

print("\nlist all accounts")
my_bank.list_accounts()


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


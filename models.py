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
        



# account1 = Accounts(321321, "Grisha", 1234, 50000, "Status", "History")
# account2 = Accounts(653421, "Daniel", 4332, 20000, "Status", "History")
# account3 = Accounts(132456, "Moshe", 4343, 15000, "Status", "History")
# account4 = Accounts(314265, "Michal", 2323, 37000, "Status", "History")
# account5 = Accounts(556612, "Dana", 1123, 43000, "Status", "History")
# account6 = Accounts(615243, "Shahar", 2121, 29000, "Status", "History")

# account1.get_info()




#=======================
# Part 3: Bank manager #TODO find a way to make it a dic
#=======================
import random 


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
        
        account_search = self.Accounts.get(int(account_id)) # The get() is to print None in case the ID hasent been found
        
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
            if account.pin == int(pin):
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
        print("----- Bank Accounts List -----") # Nice title
        
        for account in self.Accounts.values():
            
            print(f"ID: {account.account_id} | Name: {account.name} | Balance: {account.Balance}")
        
        print("-------------------------------")
    
    
    
    
    
    
    
    
    
#!Check to see if the create account works
my_bank = Bank()

print("")
print("--- Testing Account Creation ---")
print("")
new_id = my_bank.create_account("Yossi Levi", "1234")

if new_id in my_bank.Accounts:
    print(f"Success! Account {new_id} exists in the bank.")
    
    user_account = my_bank.Accounts[new_id]
    print(f"Owner Name: {user_account.name}")
    print(f"Current Balance: {user_account.Balance}")
else:
    print("Failure: Account was not saved in the dictionary.")
    
print("")
    

#! Check if account has beem found
my_bank = Bank()

new_id = my_bank.create_account("Grisha", "1234")

search_result = my_bank.find_account(new_id)

if search_result:
    print(f"The balance for {search_result.name} is: {search_result.Balance}")
    
print("")

my_bank.login_account("123456", "0000") # אמור להצליח
my_bank.login_account("123456", "9999") # אמור להיכשל (PIN טועה)
# For use to this file
import random 
import json


#===================================
#============= Accounts ============
#===================================


class Accounts: # Creating a class of Accounts

    def __init__(self, account_id, full_name, pin, balance, status , history):
        self.account_id = str(account_id) #! In dict, everthing in a string 
        self.full_name = full_name
        self.pin = str(pin) #! the reason we save as str is so if an account wil have an 0075 pin for example, it will save exactly as it isin int it will be 75 
        self.balance = float(balance) #! Line alignment that the money in the accounts will be a float
        self.status = status
        self.history = history

#================================================================================================    
        
    def add_history(self, operation, amount=None, info=""): # Insted of adding evertime by yourself the process, have build an function that doin it for me 
        from datetime import datetime
        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # This will be our manual format for history after oparation
        new_entry = { 
            "operation": operation,
            "date": date,
            "info": info
        }
        if amount is not None: # This will be in sitoation when the amount is not None
            new_entry["amount"] = float(amount)
            new_entry["amount_after"] = self.balance
    
        self.history.append(new_entry) # Add the dictionary to the list
        
#================================================================================================
      
    def deposit(self, amount):
        try: # This and except is for allowing the process move forward without crash
            amount = float(amount)
            if amount <= 0: # In case the account is trying to deposit an 0 or below, it will print an error
                return False, "ERROR: Deposit amount must be positive."

            self.balance += amount # if all good, the process will add to his history with the new balance
            self.add_history(f"Deposit", amount)
            return True, f"Successful deposit with {amount} NIS."
        except ValueError: 
            return False, "Error: Invalid amount entered."
 
#================================================================================================       
        
    def withdraw(self, amount):
        amount = float(amount)
        
        try:
            if amount <= 0: # In case the account is trying to withdraw an 0 or below, it will print an error
                return False, "ERROR: Withdraw amount must be positive."
            
            if amount > self.balance: # If the owner will try to withdraw amount thats above his balance
                return False, f"ERROR: Cannot withdraw above account balance. \nYour balance is {self.balance}."
            
            self.balance -= amount # if all good, the process will add to his history with the new balance
            self.add_history(f"Withdrawn", amount)
            return True, f"Successfully withdraw with {amount} NIS."
        except ValueError:
            return False, "ERROR: Invalid amount entered."
 
#================================================================================================    
    
    def check_balance(self): # In case the owner wats to check his balane 
        print(f"Account Balance: {self.balance}")

#================================================================================================   
        
    def pin_change(self, new_pin):
        
        self.pin = str(new_pin) # Remember that every input is a str but we wanna to make sure it wont brake
        
        self.add_history(f"PIN change", 0, info="New PIN set.")
        return True
        
#================================================================================================ 
     
    def see_history(self): # List all of the history the account have
        if not self.history:
            return []
        return self.history
        
#================================================================================================ 

    def j_dict(self): # Creating a simple function-dictionary for json to understand
        return {
            "account_id": self.account_id,
            "full_name": self.full_name,
            "pin": self.pin,
            "balance": self.balance,
            "status": self.status,
            "history": self.history 
        }

#===================================
#=============== Bank ==============
#===================================
class Bank: # Manage all accounts in our project
    def __init__(self):
        
        self.manager_full_name = "Cristiano Ronaldo"
        self.manager_pin = "admin1234" # Managers password
        self.Accounts = {} # Some kind of dictionary to save all of the accounts

#================================================================================================

    def create_account(self, full_name, pin, amount): # Function to create new account 
        account_id = str(random.randint(100000, 999999))
    
        while account_id in self.Accounts:
            account_id = str(random.randint(100000, 999999))
        
        new_account = Accounts(account_id, full_name, pin, amount, "Active", []) # Creating a user exactly according to the characteristics we created in part 2
        
        self.Accounts[account_id] = new_account # saving the new account in the dictionary of the bank
        
        print(f"Account has been created. \nYour ID is: {account_id}") # output of the creation
        return account_id

#================================================================================================

    def find_account(self, account_id): # Function to find an account
        
        account_search = self.Accounts.get(str(account_id)) # The get() is to print None in case the ID hasent been found
        
        if account_search:
            print(f"Account ID is found: {account_search.full_name}")
            return account_search
        else:
            print("ERROR: Account ID not found.")
            return None # Just for understanding, it returns an None in the terminal and sying like i havent found somthing
        
#================================================================================================        
        
    def login_account(self, account_id, pin): # Function to log a user into the bank
        account = self.find_account(account_id) # Uses the function we created in previos function
        
        # Building a tree of checks to make sure it wont break here.
        
        if not account:
            return None, "ERROR: Account was not found."
        
        if account.status == "Blocked":
            return None, f"ERROR"
        
        if str(account.pin) != str(pin):
            return None, f"ERROR"
        
        return account, f"Login to the account has successed. welcome {account.full_name}"
    
        #! Old version
        # if account.status == "Blocked":
        #     print(f"Error: Account {account_id} is BLOCKED. \nPlease call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #     return None
            
        # if account:
        #     if str(account.pin) == str(pin):
        #         print((f"Login successful. \nWelcome {account.full_name}."))
        #         return account
        #     else:
        #         print(f"Error: Incorerect PIN. \nPlease try again. \nIn case you forgot the PIN, Please call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #         return None
        # return None 
        
#================================================================================================ 
        
    def manager_login(self, password): # Function of the manager
        if password == self.manager_pin:
            return True
        else:
            return False
    
#================================================================================================   

    def transfer(self, sender, receiver, amount): # Function for transfer money between accounts
        the_sender = self.find_account(sender)
        the_receiver = self.find_account(receiver)
        
        # Again we gonna make sure the id is exists and if not it will stop him
        # The not loop will make the code run until the user exit him
        if not the_sender:
            return False, "ERROR: ID of Sender, not found."
        
        if not the_receiver:
            return False, "ERROR: ID of Receiver, not found."
        
        # Stay with me its important: 
        success, msg = the_sender.withdraw(amount)
        
        if success:
            
            the_receiver.balance += float(amount) # If the withdraw has succesed, the receiver gets it
            
            the_receiver.add_history("Transfer In", amount, info=f"From {the_sender.full_name}")  # Updating for both in dict way
            
            the_sender.history[-1]["operation"] = "Transfer - Out" # Updating the user on this transfer and of coure to who
            the_sender.history[-1]["info"] = f"To {the_receiver.full_name}"
            
            return True, f"Transfer of {amount} NIS to {the_receiver.full_name} has completed. \nThank you. goodbye." 
            
        return False, msg # In case everthing has fall it will print an error
    
        #! Old version
        # if the_sender is None: # We want to check first if they even exist in order to countinue forward to sendng the money
        #     print(f"Error: The Sender account does not exist. \nPlease try again. \nIn case you forgot the ID, Please call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #     return False
        
        # if the_receiver is None:
        #     print(f"Error: The Receiver account does not exist \nPlease try again, Make sure you put the right ID. \nIn case you having a problem, Please call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #     return False
        
        # amount_transfer = float(amount) # Creating the value of the amount for the next part
        
        # if amount_transfer <= 0: # In case the sender trys to put an 0 or low 
        #     print("Error: Amount must be positive.")
        #     return False
        
        # if the_sender.balance < amount_transfer: # Now we are goin to check if the sender has enough amount to even send the money
        #     print(f"Transfer Failed: The {the_sender.full_name} is lack of NIS.")
        #     print(f"Current Balance in your account: {the_sender.balance} | Transfer request: {amount_transfer}")
        #     return False
            
#================================================================================================
    
    def list_accounts(self): # Function of list all the accounts we created
        print("----- Bank Accounts List ------") # Nice title
        
        for account in self.Accounts.values():    
            print(f"ID: {account.account_id} | Name: {account.full_name} | Balance: {account.balance}")

#================================================================================================

    def change_pin(self, account_id, new_pin): # Function to change PIN if the user wants
        account = self.find_account(account_id)
        if account:
            account.pin_change(new_pin)
            print(f"Success: PIN for {account.full_name} has been updated.")
            return True
        else:
            print("ERROR: Could not change PIN. Account have noot found.")
            return False
        
#================================================================================================

    def change_status(self, accound_id): # Function to block or delete account in the bank by the manager
        account = self.find_account(accound_id)
        
        if not account:
            return False
        
        if account.status == "Active":
            account.status = "Blocked" # This part is for to change ths status # Pay attention that in pyrhon in order to change status for eample, you need to put only 1 = not ==
        else:
            account.status = "Active"
            
        account.add_history(
            operation="Status Change",
            info=f"Account status change to {account.status} by Admin"
        )    
        return True
    
#================================================================================================

    def delete_account(self, accound_id):
        if accound_id in self.Accounts:
            del self.Accounts[accound_id]
            return True, f"The account {accound_id} was deleted by you. Thank you and goodbye."
        return False, "Accound ID not found."
    
#================================================================================================ 

    def account_history(self, account_id): # The manager can now watch the accounts history
        account = self.find_account(account_id)
        
        if account:
            return account.history
        else:
            return None 
            
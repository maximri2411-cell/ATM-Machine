# For use to run he file with functions and dict on other files
import json                
from models import Bank, Accounts

def load_data():
    bank = Bank() # Creating an empty bank
    
    # TODO Here we put all of the json we have in one value
    data = json.load()
    
    all_accounts = data["Accounts"] # Finding all of the accounts we created/have

    for account_id in all_accounts[account_id]:
        info = all_accounts[account_id]

        new_account = Accounts( #! Creating new account, do not change
            info['account_id'],
            info['full_name'],
            info['pin'],
            info['balance'],
            info['status'],
            info['history']
        )
        
        bank.Accounts[account_id] = new_account # Saving the new account in our bank
        
    return bank
















##! Do not touch

# def all_clients(filename="data.json"):
#     #read the data.json and store client data in data var 
#     with open(filename, "r") as file:
#         data = json.load(file)
#         return data
    
# all_data[key] -> value
# all_data[key][key] - > value 
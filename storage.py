# For use to run he file with functions and dict on other files
import json                
from models import Bank, Accounts

def load_data():
    bank = Bank() # Creating an empty bank
    
    # TODO Here we put all of the json we have in one value
    data = json.load(open('data.json')) #! Important for the python to open the json info and data to translate for himself and work
    
    all_accounts = data["Accounts"] # Finding all of the accounts we created/have

    for account_id in all_accounts: # Going through the entire list of accounts
        info = all_accounts[account_id]

        new_account = Accounts( #! Creating new account, do not change, its base on what we created in data.json
            info['account_id'],
            info['full_name'],
            info['pin'],
            info['balance'],
            info['status'],
            info['history']
        )
        
        bank.Accounts[account_id] = new_account # Saving the new account in our bank
        
    return bank

def save_data(bank): 
    
    data_to_save = {} # This is creating an empty dictionary to translet to json the python objects
    
    for account_id in bank.Accounts:
        account_js = bank.Accounts[account_id] # Withdrawing accounts from current list
        data_to_save[account_id] = account_js.j_dict() # Taking account and trsnslet from python to json

    last_json = {"Accounts": data_to_save} #! All the accounts will be under the Accounts title, pay attention
    
    json_dump(last_json, open('data.json', 'w'), indent=4) # Taking the dictionary into the file that has been created 
    # The w is for write, over write the file to new one, like > in linux
    # indent is for beuty
















##! Do not touch

# def all_clients(filename="data.json"):
#     #read the data.json and store client data in data var 
#     with open(filename, "r") as file:
#         data = json.load(file)
#         return data
    
# all_data[key] -> value
# all_data[key][key] - > value 
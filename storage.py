# For use to run he file with functions and dict on other files
import json              
import os
from models import Bank, Accounts

def load_data():
    bank = Bank() # Creating an empty bank
    filename = "data.json" # In case this file dosent exist
    
    if not os.path.exists(filename):
        print("Test")
        return bank # It will return an empty bank 
    
    try:
        with open("data.json", "r") as f: #! Important for the python to open the json info and data to translate for himself and work, for example take id from some account
                data = json.load(f) 
                
                if "Accounts" not in data:
                    return bank
                all_accounts = data["Accounts"]
                    
                for account_id, info in all_accounts.items():
                    new_account = Accounts( #! Creating new account, do not change, its base on what we created in data.json
                        info["account_id"],
                        info["full_name"],
                        info["pin"],        # It taking the new account and puting all of the info we found in json
                        info["balance"],
                        info["status"],
                        info["history", []]
                    )
                    bank.Accounts[account_id] = new_account
                return bank

    except (FileNotFoundError, json.JSONDecodeError): # This if in case the file dont exist
        print("Start new databse")
        return bank # Remainder that it will return an empty bank

    # Here we put all of the json we have in one value
    
    all_accounts = data["Accounts"] # Finding all of the accounts we created/have from the data file

    for account_id in all_accounts: # Going through the entire list of accounts
        info = all_accounts[account_id]

        bank.Accounts[account_id] = new_account # Saving the new account in our bank
    return bank

#================================================================================================

def save_data(bank): 
    data_to_save = {} # This is creating an empty dictionary to translet to json the python objects
    
    for account_id, account_js in bank.Account.items():
        account_js = bank.Accounts[account_id] # Withdrawing accounts from current list
        data_to_save[account_id] = account_js.j_dict() # Taking account and trsnslet from python to json

    last_json = {"Accounts": data_to_save} #! All the accounts will be under the Accounts title, pay attention
    
    with open("data.json", "w") as f: # Added the with loop so it will "close" the open and make sure the info is saved
        json.dump(last_json, f, indent=4)
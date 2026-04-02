from models import Accounts, Bank
from storage import load_data, save_data

# Maxims lab for accounts and bank

#! deposit test
test_bank = load_data()
account_for_test = test_bank.find_account("321321") # Taking grisha for example

if account_for_test is not None:
    print(f"current balance: {account_for_test.balance}")

    print("test deposit")
    account_for_test.deposit(507.65)
    
    print(f"balance after the deposit: {account_for_test.balance}")

    save_data(test_bank) # Pay attention to that part, it saves the operation in the data json file
    print("saved in json")
    
    
#! withdraw test
    
    
from models import Accounts, Bank

# Maxims lab for accounts and bank
#! do not change somthing without asking him first

account_for_test = Bank.find_account("321321") # Taking grisha for example
if account_for_test:
    print(f"current balance: {account_for_test.balance}")

    print("test deposit")
account_for_test.deposit(507.65)
print(f"balance after the deposit: {account_for_test.balace}")




# #! This is for maxim Checkes for the json and python 
# # Porpose of the test: we take the load.data function from storage file, turning it alive into python 

# from storage import load_data

# print("Test")
# test_bank = load_data()

# grisha_id = "321321"
# if grisha_id in test_bank.Accounts:
#     acc_test = test_bank.Accounts[grisha_id]
#     print(f"found {acc_test.full_name}")
#     print(f"his balance: {acc_test.balance}")
    
# else:
#     print(f"Error: account was not found {grisha_id}.")
    
    
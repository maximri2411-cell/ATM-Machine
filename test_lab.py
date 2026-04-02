
#! This is for maxim Checkes for the json and python 

from storage import load_data

print("Test")
test_bank = load_data()

grisha_id = "321321"
if grisha_id in test_bank.Accounts:
    acc_test = test_bank.Accounts[grisha_id]
    print(f"found {acc_test.full_name}")
    print(f"his balance: {acc_test.balance}")
    
else:
    print(f"Error: account was not found {grisha_id}.")
    
    
# Porpose of the test: we take the load.data function from storage file, turning it alive into python 
#! This is for maxim Checkes for the json and bank 

from storage import load_data, save_data

print("Test")
my_bank = load_data()

grisha_id = "321321"
if grisha_id in my_bank.Accounts:
    user = my_bank.Accounts[grisha_id]
    print(f"found {user.full_name}")
    print(f"his balance: {user.balance}")
    
else:
    print(f"Error: account was not found {grisha_id}.")
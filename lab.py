##! This is for maxim Checkes for the json and bank 

from storage import load_data, save_data

print("--- Loading Bank ---")
my_bank = load_data()

grisha_id = "321321"
if grisha_id in my_bank.Accounts:
    user = my_bank.Accounts[grisha_id]
    print(f"Found User: {user.full_name}")
    print(f"Current Balance: {user.balance}")
    
    print("\n--- Testing Deposit ---")
    user.deposit(100)
    print(f"New Balance in Memory: {user.balance}")
    
    print("\n--- Saving Changes ---")
    save_data(my_bank)
    print("Done! Now go check your data.json file to see the new balance.")

else:
    print(f"Error: Could not find user {grisha_id}. Check your data.json file!")
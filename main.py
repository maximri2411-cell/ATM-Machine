from models import Accounts

print("Welcome to the Passover Project!")
account = int(input("please enter your id:"))
for acc in all_accounts: 
    if acc.account_id == user_id:
        acc.get_info()
    else:
        print("You are out of the system")
from models import Accounts

### account pool ###
def accounts_pool():
    account1 = Accounts(321321, "Grisha", 1234, 50000, True, [])
    account2 = Accounts(653421, "Daniel", 4332, 20000, True, [])
    account3 = Accounts(132456, "Moshe", 4343, 15000, False, [])
    account4 = Accounts(314265, "Michal", 2323, 37000, False, [])
    account5 = Accounts(556612, "Dana", 1123, 43000, True, [])
    account6 = Accounts(615243, "Shahar", 2121, 29000, False, [])
    return [account1, account2, account3, account4, account5, account6]


print("Welcome to the Passover Project!")
all_accounts = accounts_pool()
user_id = int(input("please enter your id:"))    


for user in all_accounts: 
    if user.account_id == user_id:
        user_pin = int(input("Please enter your PIN: "))
        user.get_info(user_pin)
        break
else:
    print("You don't have an account \nYou are out of the system \nPlease connect the bank")
            


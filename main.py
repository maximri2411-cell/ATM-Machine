from models import Accounts
print("Welcome to the Passover Project!")

def accounts_pool():
    account1 = Accounts(321321, "Grisha", 1234, 50000, True, [])
    account2 = Accounts(653421, "Daniel", 4332, 20000, "True", [])
    account3 = Accounts(132456, "Moshe", 4343, 15000, "False", [])
    account4 = Accounts(314265, "Michal", 2323, 37000, "False", [])
    account5 = Accounts(556612, "Dana", 1123, 43000, "True", [])
    account6 = Accounts(615243, "Shahar", 2121, 29000, "False", [])

    all_accounts = [account1, account2, account3, account4, account5, account6]
    rerutn accounts_pool


account = int(input("please enter your id:"))
for acc in all_accounts: 
    if acc.account_id == user_id:
        acc.get_info()
    else:
        print("You are out of the system")
        
      
        
        
        
account1.get_info()
# account2.get_info()
account3.get_info()
# account4.get_info()
# account5.get_info()
# account6.get_info()
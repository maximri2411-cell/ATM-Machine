from models import Accounts, Bank # All of the classes we created in the models.py file


print("Welcome to the Passover Project!") # Opening title


our_bank = Bank() # The class Maxim have creted #! Critical to put all of the accounts into an dictionary


def accounts_pool(): # Creating some random accounts for start
    
    from models import Accounts

### account pool ###
def accounts_pool():
    account1 = Accounts(321321, "Grisha", 1234, 50000, True, [])
    account2 = Accounts(653421, "Daniel", 4332, 20000, True, [])
    account3 = Accounts(132456, "Moshe", 4343, 15000, False, [])
    account4 = Accounts(314265, "Michal", 2323, 37000, False, [])
    account5 = Accounts(556612, "Dana", 1123, 43000, True, [])
    account6 = Accounts(615243, "Shahar", 2121, 29000, False, [])

# all_accounts = [account1, account2, account3, account4, account5, account6]
# return accounts_pool


# account = int(input("Please enter your ID: "))
# for acc in all_accounts: 
#     if acc.account_id == user_id:
#         acc.get_info()
#     else:
#         print("You are out of the system")
        
        
account1.get_info()
# account2.get_info()
account3.get_info()
# account4.get_info()
# account5.get_info()
# account6.get_info()
return [account1, account2, account3, account4, account5, account6]


print("Welcome to the Passover Project!")
all_accounts = accounts_pool()
user_id = int(input("please enter your id:"))    


for user in all_accounts: 
    if user.account_id == user_id:
        user.get_info()
        break
else:
    print("You don't have an account \n You are out of the system \n Please connect the bank")
            



#our_bank = Bank() # The class Maxim have creted #! Critical to put all of the accounts into an dictionary

  # Merging the accounts into the Bank dic
    our_bank.Accounts[account1.account_id] = account1
    our_bank.Accounts[account2.account_id] = account2
    our_bank.Accounts[account3.account_id] = account3   
    our_bank.Accounts[account4.account_id] = account4
    our_bank.Accounts[account5.account_id] = account5
    our_bank.Accounts[account6.account_id] = account6   
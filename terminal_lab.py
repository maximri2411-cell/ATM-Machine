from models import Accounts, Bank
from storage import load_data, save_data

#TODO lab for accounts and bank

#! deposit test
# test_bank = load_data()
# account_for_test = test_bank.find_account("321321") # Taking grisha for example

# if account_for_test is not None:
#     print(f"current balance: {account_for_test.balance}")

#     print("test deposit")
#     account_for_test.deposit(500)
    
#     print(f"balance after the deposit: {account_for_test.balance}")

#     save_data(test_bank) # Pay attention to that part, it saves the operation in the data json file
#     print("saved in json")
    
    
#! withdraw test
# test_bank = load_data()
# account_for_test = test_bank.find_account("556612") # Taking Dana for example

# if account_for_test is not None:
#     print(f"current balance: {account_for_test.balance}")
    
# print("Test withdraw")
# if account_for_test.withdraw(1000):
#     print(f"balance after withdraw: {account_for_test.balance}")
    
# save_data(test_bank)
# print("saved in json")


# #! PIN Change
# test_bank = load_data()
# account_for_test = test_bank.find_account("615243") # Taking King for example

# new_pin = "8762"
# account_for_test.pin_change(new_pin)

# print("New pin changed")

# save_data(test_bank)
# print("PIN have been changed")


#! combined test lab for my models and data
# def test_bank_system():
#     print("Test")
    
#     bank = load_data()
    
#     account_id = bank.create_account("Test account", "0001")
#     owner = bank.find_account(account_id)
    
#     owner.deposit(3020)
#     owner.withdraw(300)
    
#     target_id = bank.create_account("Receiver ID", "0002")
#     success, msg = bank.transfer(account_id, target_id, 700)
#     print(f"Transfer ok: {success}, note: {msg}")
    
#     save_data(bank)
#     print("Finish")

# test_bank_system()


# #! block and active account test 
# def test_manager_skills():
#     bank = load_data()
#     account_for_test = "588300" # new account i created last time
    
#     success, msg = bank.change_status(account_for_test)
#     print(msg)
    
#     save_data(bank)
    
# test_manager_skills()


# #! delete test 
# def test_manager_skills():
#     bank = load_data()
#     account_for_test = "588300" # new account i created last time, now we delete
    
#     success, msg = bank.delete_account(account_for_test)
#     print(msg)
    
#     save_data(bank)
    
# test_manager_skills()


# #! history check
# def manager_test_history():
#     bank = load_data()
#     account_for_test = "321321"
    
#     history = bank.account_history(account_for_test)
    
#     print(history)
    
# manager_test_history()

    
        #! Old version befure buttons
        # # All of the buttons in the menu of user
        # tk.Button(self.root, text="WITHDRAW", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.withdraw_action).pack(pady=20)
        # tk.Button(self.root, text="DEPOSIT", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.deposite_action).pack(pady=20)
        # tk.Button(self.root, text="BALANCE", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.check_balance_action).pack(pady=20)
        # tk.Button(self.root, text="TRANSFER", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.transfer_action).pack(pady=20)
        # tk.Button(self.root, text="CHANGE PIN", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.change_pin).pack(pady=20)
        # tk.Button(self.root, text="HISTORY", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.full_history).pack(pady=20)
        # tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        
#=======================================================
#================== Balance page =======================
#======================================================= 


        #! We dont use that 
    # def check_balance_action(self):
    #     self.cleaning_screen()
    #     tk.Label(self.root, text="Your Balance:", font=("Arial", 28, "bold"), bg="midnight blue", fg="ivory").pack(pady=40)
    #     tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4,command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")   
    #     tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)    
    #     current_balance = self.current_user.balance
    #     tk.Label(self.root, text=f"₪ {current_balance:,.2f}", font=("Arial", 32, "bold"), bg="midnight blue", fg="white").pack(pady=10)
    #     tk.Label(self.root, text="Transaction History:", font=("Arial", 20), bg="midnight blue", fg="ivory").pack(pady=(10, 5))
                 
    #     self.history_list = tk.Listbox(self.root, width=70, height=10, font=("Arial", 10, "bold"), bg="slate gray", fg="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71", justify="center")
    #     self.history_list.pack(pady=10)  
    #     user_history = self.current_user.see_history()
    #     if not user_history:
    #         self.history_list.insert("end", "No operations yet")
    #     else:
    #         for entry in reversed(user_history[-10:]): 
    #             text = f"{entry['date']} | {entry['operation']}: {entry['amount']} NIS | After: {entry['amount_after']}"
    #             self.history_list.insert("end", text)  
         
               
                #! Old version 
        #     messagebox.showerror("Error", "Please enter a positive amount.") 
        #         return
        #     current_balance = self.current_user.balance
        #     if amount > current_balance:
        #         messagebox.showerror("Withdrawal Denied", 
        #             f"The maximum amount you can withdraw is ₪{current_balance:,.2f}")
        #         return
        #     self.current_user.withdraw(amount)
            
        #     save_data(self.bank) # Saving in the data.json
            
        #     messagebox.showinfo("Success", f"₪{amount:,.2f} withdrawn successfully!")
        #     self.withdraw_action() 
        # except ValueError:
        #     messagebox.showerror("Error", "Invalid input! Please enter numbers only.") 
        
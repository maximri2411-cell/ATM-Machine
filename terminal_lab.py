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
        
        #! The old version of changing the pin
     # if old_pin != self.current_user.pin: # Check if the old pin is currect
            #     messagebox.showerror("ERROR", "Your PIN is incorrect")
            #     return

            # if new_pin == old_pin: # Check if the new pin not like the old one
            #     messagebox.showerror("ERROR", "New PIN cant be like the currect PIN")
            #     return

            # if new_pin != acc_pin: # In case the user writh 2 diffrent new pin 
            #     messagebox.showerror("ERROR", "New PINs do not match")
            #     return
            
            # if len(new_pin) == 4 and new_pin.isdigit():
            #     self.current_user.pin = new_pin # Update the new
            
            #! Old version of the transfer in models
        # if the_sender is None: # We want to check first if they even exist in order to countinue forward to sendng the money
        #     print(f"Error: The Sender account does not exist. \nPlease try again. \nIn case you forgot the ID, Please call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #     return False
        
        # if the_receiver is None:
        #     print(f"Error: The Receiver account does not exist \nPlease try again, Make sure you put the right ID. \nIn case you having a problem, Please call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #     return False
        
        # amount_transfer = float(amount) # Creating the value of the amount for the next part
        
        # if amount_transfer <= 0: # In case the sender trys to put an 0 or low 
        #     print("Error: Amount must be positive.")
        #     return False
        
        # if the_sender.balance < amount_transfer: # Now we are goin to check if the sender has enough amount to even send the money
        #     print(f"Transfer Failed: The {the_sender.full_name} is lack of NIS.")
        #     print(f"Current Balance in your account: {the_sender.balance} | Transfer request: {amount_transfer}")
        #     return False
        
        #! Old use that we took for example from google
         # json_dump(last_json, open('data.json', 'w'), indent=4)
    # The w is for write, over write the file to new one, like > in linux
    # indent is for beuty
    
    
        #! the old list box
        # amount = f"₪ {enter['amount']}" if 'amount' in enter else " " # Putting it inside a value to make it easy on me
        #         amount_after = f"₪ {enter['amount_after']}" if 'amount_after' in enter else " "
        #  text = f"{enter['date']} | {enter['operation']} | {amount} | {amount_after} | {enter['info'] }" # We took all of the operation things from models
                
                
        #! Old version of status users
        # if account.status == "Blocked":
        #     print(f"Error: Account {account_id} is BLOCKED. \nPlease call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #     return None
            
        # if account:
        #     if str(account.pin) == str(pin):
        #         print((f"Login successful. \nWelcome {account.full_name}."))
        #         return account
        #     else:
        #         print(f"Error: Incorerect PIN. \nPlease try again. \nIn case you forgot the PIN, Please call customer service or visit your local bank for help. \nThank you for understanding, goodbye.")
        #         return None
        # return None
        
        
        
        #! Old version of create an account
        #         new_id = self.bank.create_account(name, pin, float(amount)) # Calling for the function in models
        #         save_data(self.bank)
        #         messagebox.showinfo("Account successefully created", f"Account created by the name: {name}, \nAccount ID {new_id} with {amount}")
        #         self.admin_menu()
        #     else:
        #         messagebox.showerror("ERROR", "Fill in all the required details.")
        
        
        
        #! Old version pf history
        #   if not account_history:
        #     listbox.insert("end", " " * 15 + "No history recorded in the account")
        # else:
        #     for enter in reversed(account_history):
        #         date = enter["date"]
        #         oper = enter["operation"]
        #         if "amount" in enter:
        #             amount =  f"₪ {enter['amount']:,.0f}"
        #         else:
        #             amount = "---"
        #         if "amount_after" in enter:
        #             after = f"₪{enter['amount_after']:,.0f}"
        #         else:
        #             after = "---"
                
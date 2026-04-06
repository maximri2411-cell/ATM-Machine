#===================================
# All of features we need to make our app great
import tkinter as tk
from tkinter import messagebox, ttk, Scrollbar
from storage import load_data, save_data #! Do not delete it, important for our function to use

# =======================================================
#================ opening screen of the app ============= 
#========================================================

class ATM_app: # Creating the class for the app
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine") # The title
        self.root.geometry("1000x800") # Size of ther title
        self.root.configure(bg="midnight blue") # bg color
        self.bank = load_data() # Here we use all the function we created in the other files
        self.current_user = None 
        self.create_login_screen()
        
    def cleaning_screen(self): # Its important to clean the text after the user use or press the button
        for widget in self.root.winfo_children():
            widget.destroy()
            
    def exit_app(self): # Jusr an exit button in the opening screen
        if messagebox.askyesno("EXIT", "Are you sure you want to exit the app?"):
            self.root.destroy()
        
        
    def create_login_screen(self):
        self.cleaning_screen()
        
        # Simple window just to see if its work with some feature like the type of language
        tk.Label(self.root, text="GTA ATM", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        
        # Adding fild to enter his ID number
        tk.Label(self.root, text="Account ID",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.account_entry = tk.Entry(self.root, width=25, font=("Arial",16), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71" )
        self.account_entry.pack(pady=10, ipady=8)

        # Adding the pin fild
        tk.Label(self.root, text="Enter PIN", font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial",16), justify="center", bg="slate gray",fg="white",insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71")
        self.pin_entry.pack(pady=10, ipady=8)
        
        # Normal user login button
        tk.Button(self.root, text="LOGIN", command=self.normal_login,font=("Arial", 16 , "bold"), width=23, bg="gold", fg="midnight blue", activebackground="#b8962e", borderwidth=0, cursor="hand2" ,  ).pack(pady=(25, 10))
    
        # Admin login button
        tk.Button(self.root, text="Admin Access", command=self.admin_screen,font=("Arial", 16, "bold"), width=23, bg="#2d3e50", fg="white", activebackground="#b8962e", borderwidth=0, cursor="hand2"  ).pack(pady=15)

         # Normal user login button
        tk.Button(self.root, text="EXIT", command=self.exit_app,font=("Arial", 22 , "bold"), width=15, bg="gold", fg="midnight blue", activebackground="#b8962e", borderwidth=0, cursor="hand2" ,  ).pack(side= "bottom", anchor="s" , pady=20)
#                                                                                             

#=======================================================
#================== Login and menu of user ============= #TODO Upgrade the beuty
#=======================================================

    def normal_login(self): # Taking data from GUI fild
        accout_id = self.account_entry.get()
        pin = self.pin_entry.get()
        
        user, message = self.bank.login_account(accout_id, pin)
        
        if user:
            self.current_user = user
            messagebox.showinfo("Success", message)# Line up that every success entry must be like this
            self.account_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
            self.account_entry.delete(0, tk.END) 
            
            self.user_screen() # Moving to the user screen
        else:
            messagebox.showerror("ERROR", message) # Line up thst every fail entry must be like this
            self.pin_entry.delete(0, tk.END)

#=======================================================           
    
    def user_screen(self): # User screen creation
        self.cleaning_screen()
        
        # On top of the screen it will show the deatails about the user how loged in
        top_frame = tk.Frame(self.root, bg="midnight blue", pady=30)
        top_frame.pack(fill="x")
        
        # User owner account name
        tk.Label(top_frame), text=f"Account owner: {self.current_user.full_name}", font=("Arial", 15), bg="midnight blue", fg="white".pack()
        
        # ID 
        tk.Label(top_frame, text=f"Account ID: {self.current_user.id}", font=("Arial", 14), bg="midnight blue", fg="gold").pack()
        
        # This will show the current balance after an operation, making it a value
        self.balance_label = tk.Label(self.root, text=f"₪ {self.current_user.balance:,.2f}", fonr=("Arial", 28, "bold"), bg="midnight blue", fg="white")
        self.balance_label.pack(pady=10)
        
        # Down label frame
        button_frame = tk.Frame(self.root, bg="midnight blue")
        button_frame.pack(fill="both", expand=True)
        
        # All of the buttons in the menu of user
        tk.Button(self.root, text="WITHDRAW", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.withdraw_action).pack(pady=20)
        tk.Button(self.root, text="DEPOSIT", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.deposite_action).pack(pady=20)
        tk.Button(self.root, text="BALANCE", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.check_balance_action).pack(pady=20)
        tk.Button(self.root, text="TRANSFER", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.transfer_action).pack(pady=20)
        tk.Button(self.root, text="CHANGE PIN", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.change_pin).pack(pady=20)
        tk.Button(self.root, text="HISTORY", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.full_history).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        
#=======================================================
#================== Balance page ======================= #! Finished do not touch
#======================================================= #TODO Add some comments next to the code to understand what is goin on  
      
    def check_balance_action(self):
        self.cleaning_screen()
        tk.Label(self.root, text="Your Balance:", font=("Arial", 28, "bold"), bg="midnight blue", fg="ivory").pack(pady=40)
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4,command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")   
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)    
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"₪ {current_balance:,.2f}", font=("Arial", 32, "bold"), bg="midnight blue", fg="white").pack(pady=10)
        tk.Label(self.root, text="Transaction History:", font=("Arial", 20), bg="midnight blue", fg="ivory").pack(pady=(10, 5))
                 
        self.history_list = tk.Listbox(self.root, width=70, height=10, font=("Arial", 10, "bold"), bg="slate gray", fg="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71", justify="center")
        self.history_list.pack(pady=10)  
        user_history = self.current_user.see_history()
        if not user_history:
            self.history_list.insert("end", "No operations yet")
        else:
            for entry in reversed(user_history[-10:]): 
                text = f"{entry['date']} | {entry['operation']}: {entry['amount']} NIS | After: {entry['amount_after']}"
                self.history_list.insert("end", text)       

#========================================================
#================== Withdraw page ======================= #! Finished do not touch
#======================================================== #TODO Add some comments next to the code to understand what is goin on            
    
    def withdraw_action(self):
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(self.root, text="WITHDRAW", font=("Arial", 24, "bold"), bg="midnight blue", fg="ivory").pack(pady=20)
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current Balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="midnight blue", fg="gold").pack(pady=10)
        tk.Label(self.root, text="Amount to withdraw", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(30, 10))
        self.withdraw_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.withdraw_entry.pack(pady=10, ipady=8)
        tk.Button(self.root, text="Confirm action", width=20, font=("Arial", 16, "bold"), bg="gold", fg="midnight blue", command=self.execute_withdraw).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        
    
    def execute_withdraw(self):
        try:
            amount_str = self.withdraw_entry.get()
            if not amount_str:
                return
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showerror("ERROR", "Enter a positive or existing balance amount.")
                return
            current_balance = self.current_user.balance
            if amount > current_balance:
                messagebox.showerror("Withdrawal denied", 
                    f"Maximum amount to withdraw: ₪ {current_balance:,.2f}")
                return
            
            self.current_user.withdraw(amount)
            save_data(self.bank) # Saving in the data.json
            self.balance_label.config(text=f"₪ {self.current_user.balance:,.2f}")
            
            messagebox.showinfo("Success", f"₪ {amount:,.2f} withdrawn successfully.")
            self.withdraw_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("ERROR", "Invalid input, Please enter diginumbers only.")

#========================================================
#================== Deposite page ======================= #! Finished do not touch
#======================================================== #TODO Add some comments next to the code to understand what is goin on  
         
    def deposite_action(self):
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(self.root, text="DEPOSITE", font=("Arial", 24, "bold"), bg="midnight blue", fg="ivory").pack(pady=20)
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="midnight blue", fg="gold").pack(pady=10)
        tk.Label(self.root, text="Amount to deposit", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(30, 10))
        self.withdraw_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.withdraw_entry.pack(pady=10, ipady=8)
        tk.Button(self.root, text="CONFIRM ACTION", width=20, font=("Arial", 16, "bold"), bg="gold", fg="midnight blue", command=self.execute_deposite).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
   
    def execute_deposite(self):
        try:
            amount_user = self.deposit_entry.get()
            if not amount_user: return
            
            amount = float(amount_user)
            self.current_user.deposit(amount) # Calling it to make the action
            
            save_data(self.bank) # Saving data to data.json
            self.balance_label.config(text=f"₪ {self.current_user.balance:,.2f}")
            
            messagebox.showinfo("Success", f"₪{amount_user}")
            self.deposite_entry.delete(0, tk.END) # Back to main menu
        except ValueError:
            messagebox.showerror("ERROR", "Invalid amount or insufficient balance.")
               
#========================================================
#================== Transfer page ======================= #! Finished do not touch
#========================================================                  
               
    def transfer_action(self): # Creation of the transfer between accounts
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne") # Go back button
        tk.Label(self.root, text="TRANSFER BETWEEN ACCOUNTS", font=("Arial", 24, "bold"), bg="midnight blue", fg="ivory").pack(pady=20)
        
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current Balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="midnight blue", fg="gold").pack(pady=10)
        
        # Amount fild
        tk.Label(self.root, text="Transfer amount", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(10))
        self.amount_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.amount_entry.pack(pady=10, ipady=8)
        
        # ID target 
        tk.Label(self.root, text="Enter account ID to transfer", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(10))
        self.target_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.target_entry.pack(pady=10, ipady=8)
        
        # Confirm transfer with PIN again
        tk.Label(self.root, text="PIN for additional verification", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(10))
        self.pin_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.pin_entry.pack(pady=10, ipady=8)
        
        # Last buttons
        tk.Button(self.root, text="CONFIRM TRANSFER", width=20, font=("Arial", 16, "bold"), bg="gold", fg="midnight blue", command=self.execute_transfer).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)              
    
    
    def execute_transfer(self): # Conacting the transfer to the models and data and of course saving it
        try:
            amount = self.amount_entry.get()
            target_id = self.target_entry.get() # Saving the input for the next part of the function
            pin_confirm = self.pin_entry.get()
            
            if not amount or not target_id or not pin_confirm:
                messagebox.showerror("ERROR", "Fill in all the required details.")
            
            amount = float(amount) # Beacuse all of the balance is float
            
            # Checking his balance 
            if amount <=0 or amount > self.current_user.balance:
                messagebox.showerror("ERROR", "Invalid amount or insufficient balance.")
                return
            
            # Verifying the PIN
            if pin_confirm != self.current_user.pin:
                messagebox.showerror("ERROR", "Incorrect PIN, Please try again.")
                return
            
            # Checking if we put the same ID as the sender in this process    
            if target_id == self.current_user.id:
                messagebox.showerror("ERROR", "You cannot transfer money to yourself.")
                return
            
            # We want to check if the target is even exist
            if target_id in self.bank.Accounts:
                target_account = self.bank.Accounts[target_id]
                
                 # Checking if the account is blocked
                if target_account.status == "Blocked":
                    messagebox.showerror("ERROR", "The account is blocked, transfer cannot be made.")
                    return
                    
                self.current_user.withdraw(amount) # Taking from the sender
                target_account.deposit(amount)     # The receiver gets the amount
                
                save_data(self.bank) # Saving in json
                
                messagebox.showinfo("Success", f"₪ {amount:,.2f} transferred to {target_account.full_name}")
                self.user_screen() # Return te menu after finish
            else:
                messagebox.showerror("ERROR", "The account to which the transfer is intended is not found., Please check if the ID is right.")
                
        except ValueError:
            messagebox.showerror("ERROR", "Fill in all the required details.")
                
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
        
        
#========================================================
#==================== Change PIN ======================== 
#========================================================
    def change_pin(self): # New pin
        pin_change = tk.Toplevel(self.root) # Trying again the toplevel thing
        pin_change.title("Change")
        pin_change.geometry("1000x800")
        pin_change.configure(bg="midnight blue")
        
        tk.Button(pin_change, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne") # Go back button
        tk.Label(pin_change, text=" CHANGE PIN", font=("Arial", 24, "bold"), bg="midnight blue", fg="ivory").pack(pady=20) #page title

        tk.Label(pin_change, text="ENTER PIN:",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack(pady=(10, 5))
        new_pin_enter = tk.Entry(pin_change, show="*", width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71") 
        new_pin_enter.pack(pady=10, ipady=8)
       
        tk.Label(pin_change, text="New PIN: (4 digits)",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack(pady=(10, 5))
        new_pin_enter = tk.Entry(pin_change, show="*", width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71") 
        new_pin_enter.pack(pady=10, ipady=8)
       
        tk.Label(pin_change, text="ACCEPT NEW PIN",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack(pady=(10, 5))
        new_pin_enter = tk.Entry(pin_change, show="*", width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71") 
        new_pin_enter.pack(pady=10, ipady=8)
       
        
        def save_new_pin(): # Saving in the json
            new_pin = new_pin_enter.get()
            if len(new_pin) == 4 and new_pin.isdigit():
                self.current_user.pin = new_pin # Update the new
                
                # Saving in the pormat we created in models
                self.current_user.add_history( 
                    operation="PIN Change",
                    amount=0,
                    info="Security update"
                )
                
                save_data(self.bank) # Save to json
                messagebox.showinfo("Success", "PIN changed successfully")
                pin_change.destroy() # Destroy the old pin 
            else:
                messagebox.showerror("ERROR", "PIN must be 4 digits") # In case he dosent put what we asked   
        tk.Button(pin_change, text="ACCEPT CHANGE",width=20, font=("Arial", 16, "bold"), bg="gold", fg="midnight blue", command=save_new_pin).pack(pady=20)
        tk.Button(pin_change,  text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
                          
       
#========================================================
#================== History view ======================== 
#========================================================
###### I used google translet to explain, sorry
    def full_history(self): # Creating the watch history for user
        
        history_top = tk.Toplevel(self.root) # Creating the fluting window
        history_top.title("Transaction history")
        history_top.geometry("1000x800")
        history_top.configure(bg="midnight blue")
        
        
        history_frame = tk.Frame(history_top)
        history_frame.pack(pady=20, padx=20, fill="both", expand=True) # Putting the window inside the origin screen
        
        Scrollbar = tk.Scrollbar(history_frame)
        Scrollbar.pack(side="right", fill="y") # Attach the ruler to the right side of the box and stretch it to the entire height
        
        listbox = tk.Listbox(history_frame, width=50, font=("Arial", 10), yscrollcommand=Scrollbar.set) # Should connect between listbox and scrollbar with yscrollcommand
        listbox.pack(side="left", fill="both", expand=True) # Snaps the list to the left side, lets it fill all the remaining space (fill="both") and allows it to grow if we enlarge the window (expand=True).
        
        Scrollbar.config(command=listbox.yview) 
        
        account_history = self.current_user.see_history()
        if not account_history:
            listbox.insert("end", "No history recorded in the account")
        else:
            for enter in reversed(account_history):
                text = f"{enter['date']} | {enter['operation']} | ₪ {enter['amount']} | {enter['amount_after']} | {enter['info'] }",   # We took all of the operation things from models
                   
                
                #! It seems that putting "" inside f string its not accepteble
                listbox.insert("end", text) # Putting the line to the end of the list
                

#=======================================================
#================ Login and menu of manager ============ #! Finished do not touch
#=======================================================

    def admin_screen(self): # Admin screet creation
        self.cleaning_screen()
        
        # This is our title for the next screen
        tk.Label(self.root, text="ADMIN LOGIN", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        tk.Label(self.root, text="Enter Admin Password:",font=("Arial", 16, "bold"), bg="gold", fg="white"). pack(pady=10)
        
        # Adding * for his password 
        self.admin_pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial", 16, "bold"), bg="gold", fg="white")
        self.admin_pin_entry.pack(pady=10)
    
        # The button for enter confirm
        tk.Button(self.root, text="Verify Access", command=self.check_pin_admin,
                  font=("Arial", 14, "bold"), width=15, bg="black", fg="white", 
                  cursor="hand2").pack(pady=15)
        
        # Buton to return back if he wants
        tk.Button(self.root, text="Back to home page", command=self.create_login_screen,
                  font=("Arial", 10), bg="black", fg="white", borderwidth=0).pack(pady=5)
        
#======================================================= #! Finished do not touch       
        
    def check_pin_admin(self): # Check if the pin is currecct
        pin_admin = self.admin_pin_entry.get()
        
        if self.bank.manager_login(pin_admin): # Checks if the pin is currect
            messagebox.showinfo("Admin permission access passed successfully.", f"Welcome, {self.bank.manager_full_name}")
            
            self.admin_pin_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
            
            self.admin_menu()
        else:
            long_error_message = ( # Apperently you can to a function to some long message
                "Access Denied: Invalid manager password.\n"
                "Please try again.\n"
                "In case you forgot the Password," "Please call customer service.\n"
                "or visit your local bank for help.\n"
                "Thank you for understanding, goodbye."
            )
            messagebox.showerror("Access Denided", long_error_message)
            self.admin_pin_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
 
#======================================================= #! Finished do not touch       
        
    def admin_menu(self): # Creatin the admin menu after the password
        self.cleaning_screen()
        
        # Label on toop od the screen
        tk.Label(self.root, text="ADMIN CONTROL MENU", font=("Arial", 25, "bold"), bg="black", fg="white").pack(pady=40)
        
        # Buttons for the menu
        tk.Button(self.root, text="VIEW ALL ACCOUNTS", command=self.view_accounts, font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
        tk.Button(self.root, text="CREATE NEW ACCOUNT", command=self.create_new_account, font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
        tk.Button(self.root, text="CHANGE ACCOUNT STATUS", command=self.change_status, font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
            
        # Button to exit if he want
        tk.Button(self.root, text="LOGOUT", command=self.create_login_screen, bg="black", fg="white").pack(pady=30)
            
#========================================================
#================== View accounts ======================= #! Finished do not touch
#========================================================  
    def view_accounts(self):
        self.cleaning_screen() # Very important, cleaning the window
            
        columns = ("id", "name", "balance", "status") # Creating a table 
        tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)
        
        # Creating som titles for our tree 
        tree.heading("id", text="Account ID")
        tree.heading("name", text="User name")
        tree.heading("balance", text="Balanse")
        tree.heading("status", text="Status")
        
        for account_id, account in self.bank.Accounts.items(): # Taking all of the info we need to this part from our data.json"
            tree.insert("", tk.END, values=(account_id, account.full_name, f"{account.balance:.2f}", account.status))
            
        tree.pack(pady=20, padx=20, fill="x")
        
        tk.Button(self.root, text="Back to menu", command=self.admin_menu, bg="black", fg="white").pack(pady=10) # Exit button of course
        
#========================================================
#================== Change status ======================= #! Finished do not touch
#========================================================    

    def change_status(self): # Creating the function to change the account status by the admin
        self.cleaning_screen()
        
        tk.Label(self.root, text="ACCOUNT ACTIVATION/BLOCKING", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=10)
        
        tk.Label(self.root, text="Account ID to change status", bg="black", fg="white").pack()
        
        self.entry_id = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry_id.pack(pady=10)
    
        def operation_change():
            account_id = self.entry_id.get()
            
            success, message = self.bank.change_status(account_id) # Connacting the function in models
            
            if success:
                save_data(self.bank) # Saving in json the operation
                messagebox.showinfo("Account status changed", message) # In case it worked
                self.admin_menu() # Back to menu
            else:
                messagebox.showerror("ERROR", message) # In case it didnt work
        
        # Button to accept change
        tk.Button(self.root, text="Confirm action", command=operation_change, bg="black", fg="white", font=("Arial", 12,)).pack(pady=15)
        
        # Button to cancel
        tk.Button(self.root, text="Cancel action", command=self.admin_menu, bg="black", fg="white", font=("Arial", 12,)).pack(pady=15)
        
#========================================================
#=================== New account ======================== #! Finished do not touch
#========================================================   
 
    def create_new_account(self): # Function to create a new account
        self.cleaning_screen() # Remember to clean the window..
            
        tk.Label(self.root, text="CREATE NEW ACCOUNT", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=30) 
            
        # Late tje user pick an name fot his account
        tk.Label(self.root, text="Owner full name", font=("Arial", 14), bg="black", fg="white").pack()
        name_pick = tk.Entry(self.root, font=("Arial, 14"), justify="center")
        name_pick.pack(pady=10)
            
        # Late the user pick pin fot his account
        tk.Label(self.root, text="Select PIN (4 digits)", font=("Arial", 14), bg="black", fg="white").pack() 
        pin_pick = tk.Entry(self.root, font=("Arial, 14"), justify="center", show="*")
        pin_pick.pack(pady=10)
        
        # Put some starting amount
        tk.Label(self.root, text="Starting amount", font=("Arial", 14), bg="black", fg="white").pack() 
        amount_pick = tk.Entry(self.root, font=("Arial, 14"), justify="center")
        amount_pick.pack(pady=10)
            
        def save_account(): # Saving the new account in data.json
            name = name_pick.get()
            pin = pin_pick.get()
            amount = amount_pick.get()
                
            if name and pin and amount:
                new_id = self.bank.create_account(name, pin, float(amount)) # Calling for the function in models
                save_data(self.bank)
                messagebox.showinfo("Account successefully created", f"Account created by the name: {name}, \nAccount ID {new_id} with {amount}")
                self.admin_menu()
            else:
                messagebox.showerror("ERROR", "Fill in all the required details.")
                self.admin_menu()
        
        # Buttons to use to end the proccess
        tk.Button(self.root, text="Confirmation of account creation", command=save_account, bg="gold", fg="black", font=("Arial", 12,)).pack(pady=20)
        tk.Button(self.root, text="Cancellation of account creation", command=self.admin_menu, bg="black", fg="white").pack(pady=10)
                   



#!==========================================================================
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 
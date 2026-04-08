# All of features we need to make our app great
import tkinter as tk
from tkinter import messagebox, ttk, Scrollbar
from storage import load_data, save_data #! Do not delete it, important for our function to use
import hashlib
import time

# =======================================================
#================ opening screen of the app ============= 
#========================================================
#! Its very important to not touch it
def hash_pin(pin): # The hash thing
    return hashlib.sha256(pin.encode()).hexdigest()
#!====================================
class ATM_app: # Creating the class for the app
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine") # The title
        self.root.geometry("1000x800") # Size of ther title
        self.root.configure(bg="#0a192f") # bg color
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
        tk.Label(self.root, text="GTA ATM", font=("Arial", 36, "bold"), bg="#0a192f", fg="ivory").pack(pady=50)
        
        # Adding fild to enter his ID number
        tk.Label(self.root, text="Account ID",font=("Arial", 16, "bold"), bg="#0a192f", fg="ivory").pack()
        self.account_entry = tk.Entry(self.root, width=25, font=("Arial",16), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71" )
        self.account_entry.pack(pady=10, ipady=8)

        # Adding the pin fild
        tk.Label(self.root, text="Enter PIN", font=("Arial", 16, "bold"), bg="#0a192f", fg="ivory").pack()
        self.log_pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial",16), justify="center", bg="slate gray",fg="white",insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71")
        self.log_pin_entry.pack(pady=10, ipady=8)
        
        # Normal user login button
        tk.Button(self.root, text="LOGIN", command=self.normal_login,font=("Arial", 16 , "bold"), width=23, bg="gold", fg="#0a192f", activebackground="#b8962e", borderwidth=0, cursor="hand2" ,  ).pack(pady=(25, 10))
    
        # Admin login button
        tk.Button(self.root, text="Admin Access", command=self.admin_screen,font=("Arial", 16, "bold"), width=23, bg="#2d3e50", fg="black", activebackground="#b8962e", borderwidth=0, cursor="hand2"  ).pack(pady=15)

         # Normal user login button
        tk.Button(self.root, text="EXIT", command=self.exit_app,font=("Arial", 22 , "bold"), width=15, bg="gold", fg="#0a192f", activebackground="#b8962e", borderwidth=0, cursor="hand2" ,  ).pack(side= "bottom", anchor="s" , pady=20)                                                                         

#=======================================================
#================== Login and menu of user ============= 
#=======================================================

    def normal_login(self): # Taking data from GUI fild
        account_id = self.account_entry.get()
        pin = self.log_pin_entry.get()
        hashed_input = hash_pin(pin)
        user, message = self.bank.login_account(account_id, hashed_input)
        save_data(self.bank)
        
        if user:
            self.current_user = user
            messagebox.showinfo("Success", message)# Line up that every success entry must be like this, the message is from models
            self.account_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
            self.log_pin_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
            self.user_screen() # Moving to the user screen
        else:
            messagebox.showerror("ERROR", message) # Line up thst every fail entry must be like this
            self.log_pin_entry.delete(0, tk.END)

#=======================================================           
    
    def user_screen(self): # User screen creation
        self.cleaning_screen()
        
        # On top of the screen it will show the deatails about the user how loged in
        top_frame = tk.Frame(self.root, bg="#0a192f", pady=30)
        top_frame.pack(fill="x")
        
        tk.Label(self.root, text="MAIN MENU", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20)
        # User owner account name
        tk.Label(top_frame, text=f"Account owner: {self.current_user.full_name}", font=("Arial", 15), bg="#0a192f", fg="white").pack()
        
        # ID 
        tk.Label(top_frame, text=f"Account ID: {self.current_user.account_id}", font=("Arial", 14), bg="#0a192f", fg="gold").pack()
        
        # This will show the current balance after an operation, making it a value
        self.balance_label = tk.Label(self.root, text=f"₪ {self.current_user.balance:,.2f}", font=("Arial", 28, "bold"), bg="#0a192f", fg="white")
        self.balance_label.pack(pady=10)
        
        # Down label fram
        button_frame = tk.Frame(self.root, bg="#0a192f")
        button_frame.pack(fill="both", expand=True)
        buttons = [
            ("WITHDRAW", self.withdraw_action),
            ("DEPOSIT", self.deposit_action),
            ("TRANSFER", self.transfer_action),
            ("CHANGE PIN", self.change_pin),
            ("HISTORY", self.full_history)
        ]
        for text, cmd in buttons:
            tk.Button(button_frame, text=text, width=25, font=("Arial", 18), bg="gold", fg="#0a192f", command=cmd).pack(pady=10)
            
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=self.create_login_screen).pack(side="bottom", pady=20)

#========================================================
#================== Withdraw page ======================= 
#========================================================         
    
    def withdraw_action(self):
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="#0a192f", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(self.root, text="WITHDRAW", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20)
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current Balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="#0a192f", fg="gold").pack(pady=10)
        tk.Label(self.root, text="Amount to withdraw", font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(30, 10))
        self.withdraw_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.withdraw_entry.pack(pady=10, ipady=8)
        tk.Button(self.root, text="Confirm action", width=20, font=("Arial", 16, "bold"), bg="gold", fg="#0a192f", command=self.execute_withdraw).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
    
    def execute_withdraw(self):
        try:
            amount_str = self.withdraw_entry.get()
            if not amount_str:
                return
            amount = float(amount_str)
            max_withdraw = 5000
            
            if amount <= 0: # Check if the amount is positive
                messagebox.showerror("ERROR", "Enter a positive or existing balance amount.")
                self.withdraw_entry.delete(0, tk.END)
                return
            if amount > max_withdraw:
                messagebox.showerror("ERROR", f"Maximum withdraw amount: ₪ {max_withdraw:,.0f}")
                self.withdraw_entry.delete(0, tk.END)
                return
            current_balance = self.current_user.balance
            if amount > current_balance: # Check amount of the account
                messagebox.showerror("Withdrawal denied", f"Maximum amount to withdraw: ₪ {current_balance:,.2f}")
                self.withdraw_entry.delete(0, tk.END)
                return
            
            self.current_user.withdraw(amount) # Doin the operation
            save_data(self.bank) # Saving in the data.json
            messagebox.showinfo("Success", f"₪ {amount:,.2f} withdrawn successfully") # Final message
            self.user_screen() # Back to the menu
        except ValueError:
            messagebox.showerror("ERROR", "Invalid input, Please enter diginumbers only")
            self.withdraw_entry.delete(0, tk.END)

#========================================================
#================== Deposite page ======================= #! Finished do not touch
#======================================================== 
         
    def deposit_action(self):
        self.cleaning_screen()
        
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="#0a192f", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(self.root, text="DEPOSITE", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20)
        current_balance = self.current_user.balance
        
        tk.Label(self.root, text=f"Current balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="#0a192f", fg="gold").pack(pady=10)
        tk.Label(self.root, text="Amount to deposit", font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(30, 10))

        self.deposit_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.deposit_entry.pack(pady=10, ipady=8)
        
        tk.Button(self.root, text="Confirm action", width=20, font=("Arial", 16, "bold"), bg="gold", fg="#0a192f", command=self.execute_deposit).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
   
    def execute_deposit(self):
        try:
            amount_user = self.deposit_entry.get()
            if not amount_user:
                return
            
            amount = float(amount_user) # In case the user gonna enter - number
            max_deposit = 50000 # Deposit amount limit
            
            if amount <= 0:
                messagebox.showerror("ERROR", "Enter a positive amount")
                self.deposit_entry.delete(0, tk.END)
                return
            if amount > max_deposit:
                messagebox.showerror("ERROR", f"Maximum deposit amount: ₪ {max_deposit:,.0f}")
                self.deposit_entry.delete(0, tk.END)
                return
            
            self.current_user.deposit(amount) # Calling it to make the action
            save_data(self.bank) # Saving data to data.json
            messagebox.showinfo("Success", f"₪ {amount:,.2f} deposited successfully")
            self.user_screen() # Back to main menu
        except ValueError:
            messagebox.showerror("ERROR", "Invalid amount or insufficient balance")
            self.deposit_entry.delete(0, tk.END)
               
#========================================================
#================== Transfer page ======================= 
#========================================================                  
               
    def transfer_action(self): # Creation of the transfer between accounts
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="#0a192f", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne") # Go back button
        tk.Label(self.root, text="TRANSFER BETWEEN ACCOUNTS", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20)
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current Balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="#0a192f", fg="gold").pack(pady=10)
        
        # Amount fild
        tk.Label(self.root, text="Transfer amount", font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(10))
        self.amount_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.amount_entry.pack(pady=10, ipady=8)
        
        # ID target 
        tk.Label(self.root, text="Account ID to transfer", font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(10))
        self.target_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.target_entry.pack(pady=10, ipady=8)
        
        # Confirm transfer with PIN again
        tk.Label(self.root, text="PIN for additional verification", font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(10))
        self.tran_pin_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, show="*")
        self.tran_pin_entry.pack(pady=10, ipady=8)
        
        # Last buttons
        tk.Button(self.root, text="CONFIRM TRANSFER", width=20, font=("Arial", 16, "bold"), bg="gold", fg="#0a192f", command=self.execute_transfer).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)              
    
    def execute_transfer(self): # Conacting the transfer to the models and data and of course saving it
        def clear_fields():
            self.amount_entry.delete(0, tk.END)
            self.target_entry.delete(0, tk.END)
            self.tran_pin_entry.delete(0, tk.END)
        try:
            amount_input = self.amount_entry.get()
            target_id = self.target_entry.get()     # Saving the input for the next part of the function
            pin_confirm = self.tran_pin_entry.get()
            
            if not amount_input or not target_id or not pin_confirm: # Check if all the fileds are full
                messagebox.showerror("ERROR", "Fill in all the required details")
                clear_fields()
                return
            
            hashed_confirm = hash_pin(pin_confirm) #The hash thing
            if hashed_confirm != self.current_user.pin:
                messagebox.showerror("ERROR", "Incorrect PIN, cannot continue the process")
                clear_fields()
                return
                
            try:
                amount = float(amount_input)
                if amount <= 0: # Check if the user entered 0 or below
                    messagebox.showerror("ERROR", "Enter a positive amount")
                    clear_fields()
                    return
                max_transfer = 75000
                if amount > max_transfer:
                    messagebox.showerror("ERROR", f"Maximum transfer allowed is ₪ {max_transfer:,.0f}")
                    self.amount_entry.delete(0, tk.END)
                    return
            except ValueError:
                messagebox.showerror("ERROR", "Enter digits only")
                clear_fields()
                return
            
            if not pin_confirm.isdigit(): # Check if the pin contains words
                messagebox.showerror("ERROR", "PIN need to contain digits only")
                clear_fields()
                return
            
            if amount > self.current_user.balance: # Checking his balance
                messagebox.showerror("ERROR", "Invalid amount or insufficient balance")
                clear_fields()
                return  
            
            if target_id == self.current_user.account_id: # Checking if we put the same ID as the sender in this process 
                messagebox.showerror("ERROR", "You cannot transfer money to yourself")
                clear_fields()
                return
            
            if target_id not in self.bank.Accounts: # ID of the target if its even exist
                messagebox.showerror("ERROR", "Account ID not found")
                clear_fields()
                return
            target_account = self.bank.Accounts[target_id]
                
            if target_account.status == "Blocked": # Checking if the account is blocked
                messagebox.showerror("ERROR", "The account is blocked, transfer cannot be made")
                clear_fields()
                return
            
            sender_msg = f"Sent to {target_account.full_name}"
            self.current_user.withdraw(amount, info=sender_msg, operation="Transfer out") # Taking from the sender
            
            receiver_msg = f"Received from {self.current_user.full_name}"
            target_account.deposit(amount, info=receiver_msg, operation="Transfer in") # The receiver gets the amount
            
            save_data(self.bank) # Saving in json
            messagebox.showinfo("Success", f"₪ {amount:,.2f} transferred to {target_account.full_name}")
            self.user_screen() # Return te menu after finish
        except Exception as e:
            messagebox.showerror("System Error", "An unexpected error occurred. Please try again.")
            clear_fields()
        
#========================================================
#==================== Change PIN ======================== 
#========================================================

    def change_pin(self): # New pin
        pin_change = tk.Toplevel(self.root) # Trying again the toplevel thing
        pin_change.title("Change")
        pin_change.geometry("1000x800")
        pin_change.configure(bg="#0a192f")
        
        tk.Button(pin_change, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="#0a192f", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(pin_change, text=" CHANGE PIN", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20) #page title
        tk.Label(pin_change, text="Enter PIN:",font=("Arial", 16, "bold"), bg="#0a192f", fg="ivory").pack(pady=(10, 5))
        old_pin_enter = tk.Entry(pin_change, show="*", width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71") 
        old_pin_enter.pack(pady=10, ipady=8)
       
        tk.Label(pin_change, text="New PIN (4 digits)",font=("Arial", 16, "bold"), bg="#0a192f", fg="ivory").pack(pady=(10, 5))
        new_pin_enter = tk.Entry(pin_change, show="*", width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71") 
        new_pin_enter.pack(pady=10, ipady=8)
       
        tk.Label(pin_change, text="Verify new password",font=("Arial", 16, "bold"), bg="#0a192f", fg="ivory").pack(pady=(10, 5))
        acc_pin_enter = tk.Entry(pin_change, show="*", width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71") 
        acc_pin_enter.pack(pady=10, ipady=8)
        
        def save_new_pin(): # Saving in the json
            old_pin = old_pin_enter.get()
            new_pin = new_pin_enter.get()
            acc_pin = acc_pin_enter.get()
                        
            def clear_fields(): # We want to clear the the buttons if the password is incoract
                old_pin_enter.delete(0, tk.END)
                new_pin_enter.delete(0, tk.END)
                acc_pin_enter.delete(0, tk.END)

            if not old_pin or not new_pin or not acc_pin:
                clear_fields()
                messagebox.showerror("ERROR", "Fill in the required details")
                return 
            
            if hash_pin(old_pin) != self.current_user.pin: # checking if the old pin is right with hash
                clear_fields() # The cleaner
                messagebox.showerror("ERROR", "Your PIN is incorrect")
                return
            
            if new_pin == old_pin: # Check if the new is like the old
                clear_fields() # The cleaner
                messagebox.showerror("ERROR", "New PIN cant be like the currect PIN")
                return
            
            if new_pin != acc_pin: # Check if the verifying pin is like the new
                clear_fields() # The cleaner
                messagebox.showerror("ERROR", "New PINs do not match")
                return
        
            if len(new_pin) == 4 and new_pin.isdigit(): # Check if the pin is 4 digit number
                self.current_user.pin = hash_pin(new_pin) # Save as hash
                
                self.current_user.add_history( # What is goin to be in the history
                    operation="PIN Change",
                    info="Security update"
                )
                save_data(self.bank) # Save to json
                messagebox.showinfo("Success", "PIN changed successfully")
                pin_change.destroy() # Destroy the old pin 
            else:
                clear_fields()
                messagebox.showerror("ERROR", "PIN must be 4 digits") # In case he dosent put what we asked     
                              
        tk.Button(pin_change, text="Confirm action",width=20, font=("Arial", 16, "bold"), bg="gold", fg="#0a192f", command=save_new_pin).pack(pady=20)
        tk.Button(pin_change, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=lambda: [pin_change.destroy(), self.create_login_screen()]).pack(side= "bottom", anchor="s" , pady=20)
        # The lambda is for delete the old pin and close the window
                          
#========================================================
#================== History view ======================== 
#========================================================

###### I used google translet to explain, sorry
    def full_history(self): # Creating the watch history for user
        history_top = tk.Toplevel(self.root) # Creating the other window
        history_top.title("Transaction history")
        history_top.geometry("1000x800")
        history_top.configure(bg="#0a192f")
        
        tk.Label(history_top, text="ACCOUNT HISTORY ", font=("Arial", 30, "bold"), bg="#0a192f", fg="gold").pack(pady=(25, 10))
        tk.Button(history_top, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="#0a192f", width=4, command=history_top.destroy).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Button(history_top, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        tk.Button(history_top, text="REFRESH", width=15, font=("Arial", 22, "bold"), bg="gold", fg="#0a192f", command=lambda: update_list()).pack(side= "bottom", anchor="s" , pady=40)
        
        history_frame = tk.Frame(history_top, bg="gold", bd=2)
        history_frame.pack(pady=15, padx=30, fill="both", expand=True) # Putting the window inside the origin screen
         #! Roller
        Scrollbar = tk.Scrollbar(history_frame)
        Scrollbar.pack(side="right", fill="y") # Attach the ruler to the right side of the box and stretch it to the entire height
        
        listbox = tk.Listbox(history_frame, width=30, font=("Courier New", 14, "bold"), bg="#0a192f", fg="white", selectbackground="gold", selectforeground="#0a192f", borderwidth=0, highlightthickness=0, yscrollcommand=Scrollbar.set) # Should connect between listbox and scrollbar with yscrollcommand
        listbox.pack(side="left", fill="both", expand=True) # Snaps the list to the left side, lets it fill all the remaining space (fill="both") and allows it to grow if we enlarge the window (expand=True).
        Scrollbar.config(command=listbox.yview) 
        
        #! It seems that putting "" inside f string its not accepteble
        def update_list(): # This creating our beuty table
            listbox.delete(0, tk.END) # Clean
            header = f"{'Date':<22} | {'Operation':<15} | {'Amount':<12} | {'Balance'}" # The format on top
            listbox.insert("end", "") 
            listbox.insert("end", header)
            listbox.insert("end", "=" * 120)
            account_history = self.current_user.see_history()
            
            if not account_history:
                listbox.insert("end", "")
                listbox.insert("end", " " * 20 + "No history recorded") # If it is a new account it will print this
            else:
                for i, enter in enumerate(reversed(account_history)): # Format if there is a history for that account
                    date = enter.get("date", "---")
                    oper = enter.get("operation", "---")
                    amount = f"₪ {enter['amount']:,.0f}" if "amount" in enter else "---"
                    after = f"₪ {enter['amount_after']:,.0f}" if "amount_after" in enter else "---"
                    
                    line = f"{date:<21} | {oper:<14} | {amount:<11} | {after}"
                    listbox.insert("end", line) # Putting the line to the end of the list
                    
                    if i % 2 == 0:
                        listbox.itemconfig(listbox.size() - 1, bg="SkyBlue3")
                    else:
                        listbox.itemconfig(listbox.size() - 1, bg="#0a192f")
                listbox.insert('end", ""')
        
        update_list()
        
#=======================================================
#================ Login and menu of manager ============ 
#=======================================================

    def admin_screen(self): # Admin screet creation
        self.cleaning_screen()
        
        # This is our title for the next screen
        tk.Label(self.root, text="ADMIN LOGIN", font=("Arial", 36, "bold"), justify="center", bg="#0a192f", fg="white").pack(pady=50)
        tk.Label(self.root, text="Enter Admin Password:",font=("Arial", 16, "bold"), justify="center", bg="#0a192f", fg="ivory").pack()
        
        # Adding * for his password 
        self.admin_pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial",16), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71" )
        self.admin_pin_entry.pack(pady=10, ipady=8)
        
        # The button for enter confirm
        tk.Button(self.root, text="Verify Access", command=self.check_pin_admin, font=("Arial", 16, "bold"), width=23, bg="gold", fg="#0a192f", activebackground="#b8962e", borderwidth=0, cursor="hand2").pack(pady=(25, 10))
        
        # Buton to return back if he wants
        tk.Button(self.root, text="Home Page", command=self.create_login_screen, font=("Arial", 22 , "bold"), width=15, bg="gold", fg="#0a192f", activebackground="#b8962e", borderwidth=0, cursor="hand2").pack(side= "bottom", anchor="s" , pady=20)
                                                                   
#=======================================================     
        
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
 
#=======================================================       
        
    def admin_menu(self): # Creatin the admin menu after the password
        self.cleaning_screen()
        
        # Label on toop od the screen
        tk.Label(self.root, text="ADMIN CONTROL MENU", font=("Arial", 36, "bold"), justify="center", bg="#0a192f", fg="white").pack(pady=50)
         
        
        button_frame = tk.Frame(self.root, bg="#0a192f")
        button_frame.pack(fill="both", expand=True)
        buttons = [
            ("VIEW ALL ACCOUNTS", self.view_accounts),
            ("CREATE NEW ACCOUNT", self.create_new_account),
            ("CHANGE ACCOUNT STATUS", self.change_status),
        ]
        for text, cmd in buttons:
            tk.Button(button_frame, text=text, width=25, font=("Arial", 18), bg="gold", fg="#0a192f", command=cmd).pack(pady=10)
            
        # Button to exit if he want
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="#0a192f", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        
#========================================================     
#================== View accounts ======================= 
#======================================================== 
 
    def view_accounts(self):
        self.cleaning_screen() # Very important, cleaning the window
       
        history_top = tk.Frame(self.root, bg="#0a192f")
        history_top.pack(fill="x")
        tk.Label(history_top, text="ACCOUNT MANAGMENT ", font=("Arial", 30, "bold"), bg="#0a192f", fg="gold").pack(pady=(25, 10))
        
        columns = ("id", "name", "balance", "status") # Creating a table 
        tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)
        
        # Creating som titles for our tree 
        tree.heading("id", text="Account ID")
        tree.heading("name", text="User name")
        tree.heading("balance", text="Balance")
        tree.heading("status", text="Status")
        
        for account_id, account in self.bank.Accounts.items(): # Taking all of the info we need to this part from our data.json"
            tree.insert("", tk.END, values=(account_id, account.full_name, f"{account.balance:.2f}", account.status))  
        tree.pack(pady=20, padx=20, fill="x")
        tk.Button(self.root,text="REFRESH", font=("Arial", 14, "bold"),width=25, command=self.view_accounts, bg="gold", fg="#0a192f", ).pack(pady=10)
        tk.Button(self.root, text="BACK TO MENU",  font=("Arial", 22), bg="gold", fg="#0a192f", width=15, command=self.admin_menu,).pack(side= "bottom", anchor="s" , pady=20) # Exit button of course
        
#========================================================
#================== Change status ======================= 
#========================================================    

    def change_status(self): # Creating the function to change the account status by the admin
        self.cleaning_screen()
        self.root.configure(bg="#0a192f")
        
        tk.Label(self.root, text="ACCOUNT ACTIVATION/BLOCKING", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20) #page title
        tk.Label(self.root, text="Enter account ID to change status", font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(30, 10))
        
        self.entry_id = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.entry_id.pack(pady=10, ipady=8)
    
        def operation_change():
            account_id = self.entry_id.get()
            if not account_id:
                messagebox.showwarning("ERROR", "Please enter an account ID")
                return
            
            success, message = self.bank.change_status(account_id) # Connacting the function in models
            
            if success:
                save_data(self.bank) # Saving in json the operation
                messagebox.showinfo("Account status changed", message) # In case it worked
                self.admin_menu() # Back to menu
            else:
                messagebox.showerror("ERROR", message) # In case it didnt work
                self.entry_id.delete(0, tk.END) # Rember that it cleans our window if there is an error
        
        # Button to accept change
        tk.Button(self.root, text="Confirm action", command=operation_change,width=20, font=("Arial", 16, "bold"), bg="gold", fg="#0a192f").pack(pady=20)
        
        # Button to cancel
        tk.Button(self.root, text="BACK TO MENU",  font=("Arial", 22), bg="gold", fg="#0a192f", width=15, command=self.admin_menu,).pack(side= "bottom", anchor="s" , pady=20) # Exit button of course
#========================================================
#=================== New account ======================== 
#========================================================   
 
    def create_new_account(self): # Function to create a new account
        self.cleaning_screen() # Remember to clean the window..
            
        tk.Label(self.root, text="CREATE NEW ACCOUNT", font=("Arial", 30, "bold"), bg="#0a192f", fg="ivory").pack(pady=20) #page title
            
        # Late tje user pick an name fot his account
        tk.Label(self.root, text="Owner full name",font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(30, 10))
        name_pick = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        name_pick.pack(pady=10, ipady=8)
            
        # Late the user pick pin fot his account
        tk.Label(self.root, text="Select PIN (4 digits)",font=("Arial", 14, "bold"), bg="#0a192f", fg="white").pack(pady=(30, 10))
        pin_pick = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        pin_pick.pack(pady=10, ipady=8)
            
        def save_account(): # Saving the new account in data.json
            name = name_pick.get()
            pin = pin_pick.get() # PIN is public
                            
            if not name or not pin: # Created a checko if not the name or pin was writh in the windows
                messagebox.showerror("Missing data", "Fill in all the required details")
                return
            if any(char.isdigit() for char in name): # Not allowing to put numbers in the name
                messagebox.showerror("ERROR", "Name cannot contain numbers!")
                pin_pick.delete(0, 'end') 
                return

            if not pin.isdigit() or len(pin) != 4: # Just to be ready if the pin is incoract
                messagebox.showerror("ERROR", "PIN must be 4 digits")
                pin_pick.delete(0, 'end') 
                return
            final_pin = hash_pin(pin)
            new_id = self.bank.create_account(name, final_pin, 0.0, "Active", []) # Amount with 0 on the start
            save_data(self.bank)
            
            success_msg = (
                f"Account Created Successfully:\n"
                f"Owner: {name}\n"
                f"Account ID: {new_id}\n"
                f"Starting Balance: ₪ 0.00\n"
                f"PIN: {pin} (Secured)\n"
                "Please note to yourself the details"
            )
            messagebox.showinfo("Success", success_msg)
            self.admin_menu()
        
        # Buttons to use to end the proccess
        tk.Button(self.root, text="CONFIRM", command=save_account, width=20, font=("Arial", 16, "bold"), bg="gold", fg="#0a192f").pack(pady=20)
        tk.Button(self.root, text="BACK TO MENU",  font=("Arial", 22), bg="gold", fg="#0a192f", width=15, command=self.admin_menu,).pack(side= "bottom", anchor="s" , pady=20) # Exit button of course
#!==========================================================================
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop()
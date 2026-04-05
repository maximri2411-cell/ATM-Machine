#===================================
# All of features we need to make our app great
import tkinter as tk
from tkinter import messagebox, ttk
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
        
    def create_login_screen(self):
        self.cleaning_screen()
        
        # Simple window just to see if its work with some feature like the type of language
        tk.Label(self.root, text="WELCOME TO COCOBONGO ATM", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        
        # Adding fild to enter his ID number
        tk.Label(self.root, text="Account ID: ",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.account_entry = tk.Entry(self.root, width=25, font=("Arial",16), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71" )
        self.account_entry.pack(pady=10, ipady=8)

        # Adding the pin fild
        tk.Label(self.root, text="Enter PIN: ", font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial",16), justify="center", bg="slate gray",fg="white",insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71")
        self.pin_entry.pack(pady=10, ipady=8)
        
        # Normal user login button
        tk.Button(self.root, text="LOGIN", command=self.normal_login,font=("Arial", 11 , "bold"), width=15, activebackground="#b8962e", cursor="hand2" , bg="gold", fg="midnight blue" ).pack(pady=(25, 10))
    
        # Admin login button
        tk.Button(self.root, text="Admin Access", command=self.admin_screen,font=("Arial", 11, "bold"), bg="#2d3e50", fg="white", borderwidth=0, cursor="hand2"  ).pack(pady=5)
  


#=======================================================
#================== Login and menu of user =============
#=======================================================

    def normal_login(self): # Taking data from GUI fild
        accout_id = self.account_entry.get()
        pin = self.pin_entry.get()
        
        user, message = self.bank.login_account(accout_id, pin)
        
        if user:
            self.current_user = user
            messagebox.showinfo("SUCCESS", message)# Line up that every success entry must be like this
            self.account_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
            self.account_entry.delete(0, tk.END) 
            
            self.user_screen() # Moving to the user screen
        else:
            messagebox.showerror("ERROR: Login Failed", message) # Line up thst every fail entry must be like this
            self.pin_entry.delete(0, tk.END)

#=======================================================            
    
    def user_screen(self): # User screen creation
        self.cleaning_screen()
        tk.Label(self.root, text=f"Welcome back {self.current_user.full_name}", font=("Arial", 28, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        tk.Button(self.root, text="WITHDRAW", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.withdraw_action).pack(pady=20)
        tk.Button(self.root, text="DEPOSIT", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.deposite_action).pack(pady=20)
        tk.Button(self.root, text="BALANCE", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.check_balance_action).pack(pady=20)
        tk.Button(self.root, text="Trancfer", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", ).pack(pady=20)
        tk.Button(self.root, text="Change PIN", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", ).pack(pady=20)
        tk.Button(self.root, text="History", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", ).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        
       
      
#=======================================================
#================== Balance page =======================
#======================================================= 
      
    def check_balance_action(self):
        self.cleaning_screen()
        tk.Label(self.root, text=f"{self.current_user.full_name} Your Balance:", font=("Arial", 28, "bold"), bg="midnight blue", fg="ivory").pack(pady=40)
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4,command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")   
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)    
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"₪ {current_balance:,.2f}", font=("Arial", 32, "bold"), bg="midnight blue", fg="white").pack(pady=10)
        tk.Label(self.root, text="Transaction History: ", font=("Arial", 20), bg="midnight blue", fg="ivory").pack(pady=(10, 5))
                 
        self.history_list = tk.Listbox(self.root, width=70, height=10, font=("Arial", 10, "bold"), bg="slate gray", fg="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71", justify="center")
        self.history_list.pack(pady=10)  
        user_history = self.current_user.see_history()
        if not user_history:
            self.history_list.insert("end", "No operations yet")
        else:
            for entry in reversed(user_history): 
                text = f"{entry['date']} | {entry['operation']}: {entry['amount']} NIS | After: {entry['amount_after']}"
                self.history_list.insert("end", text)       

#========================================================
#================== Withdraw page =======================
#========================================================             
    
    def withdraw_action(self):
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(self.root, text=f"{self.current_user.full_name}\nWITHDRAW", font=("Arial", 24, "bold"), bg="midnight blue", fg="ivory").pack(pady=20)
        
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current Balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="midnight blue", fg="gold").pack(pady=10)
        tk.Label(self.root, text="HOW MUCH WOULD YOU LIKE TO WITHDRAW:", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(30, 10))
        self.withdraw_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.withdraw_entry.pack(pady=10, ipady=8)
        tk.Button(self.root, text="ACCEPT THE DRAW", width=20, font=("Arial", 16, "bold"), bg="gold", fg="midnight blue", command=self.execute_withdraw).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=20)
        
    
    def execute_withdraw(self):
        try:
            amount_str = self.withdraw_entry.get()
            if not amount_str:
                return
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showerror("Error", "Please enter a positive amount.")
                return
            current_balance = self.current_user.balance
            if amount > current_balance:
                messagebox.showerror("Withdrawal Denied", 
                    f"The maximum amount you can withdraw is ₪{current_balance:,.2f}")
                return
            self.current_user.withdraw(amount)
            
            save_data(self.bank) # Saving in the data.json
            
            messagebox.showinfo("Success", f"₪{amount:,.2f} withdrawn successfully!")
            self.withdraw_action() 
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numbers only.")
        
    
#========================================================
#================== Deposite page =======================
#========================================================    
         
    def deposite_action(self):
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4, command=self.user_screen).place(relx=0.95, rely=0.05, anchor="ne")
        tk.Label(self.root, text=f"{self.current_user.full_name}\nDEPOSITE", font=("Arial", 24, "bold"), bg="midnight blue", fg="ivory").pack(pady=20)
        
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"Current Balance: ₪ {current_balance:,.2f}", font=("Arial", 18), bg="midnight blue", fg="gold").pack(pady=10)
        tk.Label(self.root, text="HOW MUCH WOULD YOU LIKE TO DEPOSITE:", font=("Arial", 14, "bold"), bg="midnight blue", fg="white").pack(pady=(30, 10))
        self.withdraw_entry = tk.Entry(self.root, width=20, font=("Arial", 18), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0)
        self.withdraw_entry.pack(pady=10, ipady=8)
        tk.Button(self.root, text="ACCEPT THE DEPOSITE", width=20, font=("Arial", 16, "bold"), bg="gold", fg="midnight blue", command=self.execute_deposite).pack(pady=20)
        tk.Button(self.root, text="LOGOUT", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=40)
   
    def execute_deposite(self):
        try:
            amount_user = self.withdraw_entry.get()
            if not amount_user: return
            
            amount = float(amount_user)
            self.current_user.deposit(amount) # Calling it to make the action
            
            save_data(self.bank) # Saving data to data.json
            
            messagebox.showinfo("Success", f"₪{amount_user}")
            self.user_screen() # Back to main menu
        except ValueError:
            messagebox.showerror("ERROR", "Enrter a vilid number")
               
               
#=======================================================
#================ Login and menu of manager ============
#=======================================================

    def admin_screen(self): # Admin screet creation
        self.cleaning_screen()
        
        # This is our title for the next screen
        tk.Label(self.root, text="Manager Login", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
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
        
#=======================================================        
        
    def check_pin_admin(self): # Check if the pin is currecct
        pin_admin = self.admin_pin_entry.get()
        
        if self.bank.manager_login(pin_admin): # Checks if the pin is currect
            messagebox.showinfo("Admin access passed successfully", f"Welcome, {self.bank.manager_full_name}")
            
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
        tk.Label(self.root, text="ADMIN CONTROL MENU", font=("Arial", 25, "bold"), bg="black", fg="white").pack(pady=40)
        
        # Buttons for the menu
        tk.Button(self.root, text="VIEW ALL ACCOUNTS", command=self.view_accounts, font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
        tk.Button(self.root, text="CREATE NEW ACCOUNT", command=self.create_new_account, font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
        tk.Button(self.root, text="CHANGE ACCOUNT STATUS", command=self.change_status, font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
            
        # Button to exit if he want
        tk.Button(self.root, text="LOGOUT", command=self.create_login_screen, bg="black", fg="white").pack(pady=30)
            
#=======================================================    

    def view_accounts(self):
        self.cleaning_screen() # Very important, cleaning the window
            
        columns = ("id", "name", "balance", "status") # Creating a table 
        tree = ttk.Treeview(self.root, columns=columns, show="headings", height=15)
        
        # Creating som titles for our tree 
        tree.heading("id", text="Account ID: ")
        tree.heading("name", text="User name: ")
        tree.heading("balance", text="Balanse: ")
        tree.heading("status", text="Status: ")
        
        for account_id, account in self.bank.Accounts.items(): # Taking all of the info we need to this part from our data.json"
            tree.insert("", tk.END, values=(account_id, account.full_name, f"{account.balance:.2f}", account.status))
            
        tree.pack(pady=20, padx=20, fill="x")
        
        tk.Button(self.root, text="Back to menu", command=self.admin_menu, bg="black", fg="white").pack(pady=10) # Exit button of course
        
#=======================================================  

    def change_status(self): # Creating the function to change the account status by the admin
        self.cleaning_screen()
        
        tk.Label(self.root, text="Active - Block account", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=10)
        
        tk.Label(self.root, text="Enter ID account you want to change status: ", bg="black", fg="white").pack()
        
        self.entry_id = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry_id.pack(pady=10)
    
        def operation_change():
            account_id = self.entry_id.get()
            
            success, message = self.bank.change_status(account_id) # Connacting the function in models
            
            if success:
                save_data(self.bank) # Saving in json the operation
                messagebox.showinfo("Status changed", message) # In case it worked
                self.admin_menu() # Back to menu
            else:
                messagebox.showerror("ERROR", message) # In case it didnt work
        
        # Button to accept change
        tk.Button(self.root, text="Change status", command=operation_change, bg="black", fg="white", font=("Arial", 12,)).pack(pady=15)
        
        # Button to cancel
        tk.Button(self.root, text="Cancel status", command=self.admin_menu, bg="black", fg="white", font=("Arial", 12,)).pack(pady=15)
        
 #=======================================================  
 
    def create_new_account(self): # Function to create a new account
        self.cleaning_screen() # Remember to clean the window..
            
        tk.Label(self.root, text="Create new account", font=("Arial", 18, "bold"), bg="black", fg="white").pack(pady=30) 
            
        # Late tje user pick an name fot his account
        tk.Label(self.root, text="Owner full name", font=("Arial", 14), bg="black", fg="white").pack()
        name_pick = tk.Entry(self.root, font=("Arial, 14"), justify="center")
        name_pick.pack(pady=10)
            
        # Late the user pick pin fot his account
        tk.Label(self.root, text="Select PIN (4 digits)", font=("Arial", 14), bg="black", fg="white").pack() 
        pin_pick = tk.Entry(self.root, font=("Arial, 14"), justify="center", show="*")
        pin_pick.pack(pady=10)
        
        # Put some starting amount
        tk.Label(self.root, text="First deposit", font=("Arial", 14), bg="black", fg="white").pack() 
        amount_pick = tk.Entry(self.root, font=("Arial, 14"), justify="center")
        amount_pick.pack(pady=10)
            
        def save_account(): # Saving the new account in data.json
            name = name_pick.get()
            pin = pin_pick.get()
            amount = amount_pick.get()
                
            if name and pin and amount:
                new_id = self.bank.create_account(name, pin, float(amount)) # Calling for the function in models
                save_data(self.bank)
                messagebox.showinfo("Account successefully created", f"Account created account by name {name}, \nAccount ID {new_id} with {amount}")
                self.admin_menu()
            else:
                messagebox.showerror("ERROR", "Fill in all the requairds fileds")
                self.admin_menu()
        
        # Buttons to use to end the proccess
        tk.Button(self.root, text="Confirm createing", command=save_account, bg="gold", fg="black", font=("Arial", 12,)).pack(pady=20)
        tk.Button(self.root, text="Cancel creating", command=self.admin_menu, bg="black", fg="white").pack(pady=10)
                   
#!======================================================
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 
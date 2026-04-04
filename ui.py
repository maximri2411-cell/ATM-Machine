#===================================
# All of features we need to make our app great
import tkinter as tk
from tkinter import messagebox
from storage import load_data, save_data #! Do not delete it, important for our function to use

# =======================================================
#================ opening screen of the app =============
#========================================================

class ATM_app: # Creating the class for the app
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Machine") # The title
        self.root.geometry("800x600") # Size of ther title
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
        tk.Label(self.root, text="Welcome To X ATM", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        
        # Adding fild to enter his ID number
        tk.Label(self.root, text="Account ID: ",font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.account_entry = tk.Entry(self.root, width=25, font=("Arial",16), justify="center", bg="slate gray", fg="white", insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71" )
        self.account_entry.pack(pady=10, ipady=8)

        # Adding the pin fild
        tk.Label(self.root, text="Enter PIN: ", font=("Arial", 16, "bold"), bg="midnight blue", fg="ivory").pack()
        self.pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial",16), justify="center", bg="slate gray",fg="white",insertbackground="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71")
        self.pin_entry.pack(pady=10, ipady=8)
        
        # Normal user login button
        tk.Button(self.root, text="Login", command=self.normal_login,font=("Arial", 11 , "bold"), width=15, activebackground="#b8962e", cursor="hand2" , bg="gold", fg="midnight blue" ).pack(pady=(25, 10))
    
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
            messagebox.showinfo("Success", message)# Line up that every success entry must be like this
            self.account_entry.delete(0, tk.END) # instead of the user will delete by himself the line, it doin for him
            self.account_entry.delete(0, tk.END) 
            
            self.user_screen() # Moving to the user screen
        else:
            messagebox.showerror("ERROR: Login Failed", message) # Line up thst every fail entry must be like this
            self.user_pin_entry.delete(0, tk.END)

#=======================================================            
    
    def user_screen(self): # User screen creation
        self.cleaning_screen()
        tk.Label(self.root, text=f"Welcome back,{self.current_user.full_name}", font=("Arial", 20, "bold"), bg="midnight blue", fg="ivory").pack(pady=15)
        tk.Button(self.root, text="Withdraw", width=25, font=("Arial", 18), bg="gold", fg="midnight blue").pack(pady=20)
        tk.Button(self.root, text="Deposit", width=25, font=("Arial", 18), bg="gold", fg="midnight blue").pack(pady=20)
        tk.Button(self.root, text="Balance", width=25, font=("Arial", 18), bg="gold", fg="midnight blue", command=self.check_balance_action).pack(pady=20)
        tk.Button(self.root, text="Logout", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side= "bottom", anchor="s" , pady=40)
       
      
#=======================================================
#================== Balance page =======================
#======================================================= 
      
    def check_balance_action(self):
        self.cleaning_screen()
        tk.Button(self.root, text="⬅", font=("Arial", 14, "bold"), bg="gold", fg="midnight blue", width=4,command=self.user_screen).place(x=740, y=20)       
        
        current_balance = self.current_user.balance
        tk.Label(self.root, text=f"₪ {current_balance:,.2f}", font=("Arial", 32, "bold"), bg="midnight blue", fg="white").pack(pady=20)
        tk.Label(self.root, text="Transaction History:", font=("Arial", 14), bg="midnight blue", fg="ivory").pack(pady=(20, 5))
                 
        history_list = tk.Listbox(self.root, width=70, height=10, font=("Arial", 10), bg="slate gray", fg="white", borderwidth=0, highlightthickness=1, highlightbackground="#4a5a71", justify="center").pack(pady=10)  
        user_history = self.current_user.see_history()
        if not user_history:
            history_list.insert("end", "No operations yet")
        else:
            for entry in reversed(user_history): 
                text = f"{entry['date']} | {entry['operation']}: {entry['amount']} NIS | After: {entry['amount_after']}"
            history_list.insert("end", text)
            tk.Button(self.root, text="Back to Menu", width=20, font=("Arial", 12, "bold"), bg="gold", fg="midnight blue", command=self.user_screen).pack(side="bottom", pady=40)
        tk.Button(self.root, text="Logout", width=15, font=("Arial", 22), bg="gold", fg="midnight blue", command=self.create_login_screen).pack(side="bottom", anchor="s", pady=40)
           
        tk.Label(self.root, text=f"Welcome back, \n{self.current_user.full_name}", font=("Ariel", 13)).pack(pady=15)
        tk.Button(self.root, text="Logout", command=self.create_login_screen, bg="black", fg="white").pack(pady=30)

#=======================================================
#================ Login and menu of manager ============
#=======================================================

    def admin_screen(self): # Admin screet creation
        self.cleaning_screen()
        
        # This is our title for the next screen
        tk.Label(self.root, text="Manager Login", font=("Arial", 36, "bold"), bg="midnight blue", fg="ivory").pack(pady=50)
        tk.Label(self.root, text="Enter Admin Password:",font=("Arial", 16, "bold"), bg="gold", fg="white"). pack(pady=10)
        
        # Adding * for his password 
        self.admin_pin_entry = tk.Entry(self.root, show="*", width=25, font=("Arial", 16, "bold"), bg="gold", fg="white").pack(pady=10)
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
            messagebox.showinfo("Manager access passed successfully", f"Welcome, {self.bank.manager_full_name}")
            
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
        tk.Label(self.root, text="Admin control menu", font=("Arial", 25, "bold"), 
                 bg="black", fg="white").pack(pady=40)
        
        # Buttons for the menu
        tk.Button(self.root, text="View all accounts", font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
        tk.Button(self.root, text="Create new account", font=("Arial", 12), width=30, bg="black", fg="white").pack(pady=10)
            
        # Button to exit if he want
        tk.Button(self.root, text="Logout", command=self.create_login_screen, bg="black", fg="white").pack(pady=30)
            
        
#!======================================================
if __name__ == "__main__": #! This will run our app evertime we run the code
    root = tk.Tk()
    app = ATM_app(root)
    root.mainloop() 